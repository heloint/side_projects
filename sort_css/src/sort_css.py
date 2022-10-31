import argparse

import re
import cssutils
import logging
from typing import Generator, Dict
import bs4  # type: ignore
from typing import Any,Dict,List, Generator, Tuple

# To silence the warnings and error messages in stdout while using cssutils.parseString.
# It's not informative, doesn't affect the funcionality
# of the stylesheet and unnecessarly verbose.
cssutils.log.setLevel(logging.CRITICAL) #type: ignore

def recurse(
    html_groups: list[bs4.BeautifulSoup | Any],
    collector_dict: Dict[Any, Any],
) -> Dict[str, List[str | Dict[str, Any]] | Dict[str, str | List[Any]]]:
    """Recursively iterates the BeautifulSoup4.html_parse return."""

    for group in html_groups:
        if not isinstance(group, str):

            if not group.name in collector_dict:
                collector_dict[group.name] = []

            tmp_collector: dict[str, Any] = {}

            if group.attrs:
                tmp_collector = {"attributes": group.attrs}

            collector_dict[group.name] += (recurse(group, tmp_collector),)  # type: ignore

    return collector_dict


def parse(html_string: str) -> Dict[str, List[str | Dict[str, Any]] | Dict[str, str | List[Any]]]:
    """Recursively parses the html_groups from BeautifulSoup4.html_parse and
    fetches to a hierarchical dictionary."""

    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(html_string, "html.parser")

    child_ls: list[bs4.PageElement] = [child for child in soup.contents]

    return recurse(child_ls, {})


def convert_html_to_dict(path: str) -> Dict[str, List[str | Dict[str, Any]] | Dict[str, str | List[Any]]]:
    """Converts html to dictionary."""
    return parse(read_file(path))


def get_identifiers_in_order(html_dict: Dict[str, List[Any]]):
    start_node: Dict[str, List[Any]] = html_dict

    if isinstance(start_node, dict) and 'html' in html_dict.keys():
        start_node = html_dict['html'][0]['body']

    for dictionary in start_node:
        for key, value in dictionary.items():

            if key == 'attributes':
                if 'id' in value:
                    yield f"#{value['id']}"
                if 'class' in value:
                    for class_name in value['class']:
                        yield f".{class_name}"

            yield key 

            if isinstance(value, list):
                yield from get_identifiers_in_order(value)


def get_html_element_order(path: str) -> Tuple[str, ...]:

    html_dict: Dict[str, List[str | Dict[str, Any]] | Dict[str, str | List[Any]]] = convert_html_to_dict(path)
    identifiers_in_order = get_identifiers_in_order(html_dict)
    identifiers_without_dups: Tuple[str, ...] = tuple(dict.fromkeys(identifiers_in_order))

    return identifiers_without_dups

# =================================================

def read_file(path: str) -> str:
    "Reads css.."

    with open(path, "r", encoding="UTF-8") as file:
        css_content = file.read()

    return css_content


def css_to_dict(css_content: str) -> dict[str, dict[str, str]]:
    "Reads, parses, converts css to dictionary."

    css_dict: dict[str, dict[str, str]] = {}
    sheet: cssutils.css.cssstylesheet.CSSStyleSheet = cssutils.parseString(css_content)

    comment = ""
    for rule in sheet.cssRules:

        if type(rule) == cssutils.css.csscomment.CSSComment:
            comment = rule.cssText
        else:
            if rule.selectorText not in css_dict.keys():
                css_dict.setdefault(rule.selectorText, {"comment": "", "props": ""})

            css_dict[rule.selectorText]["comment"] = comment
            css_dict[rule.selectorText]["props"] = rule.style.cssText

            comment = ""

    return css_dict


def format_css_dict(
    css_dict: dict[str, dict[str, str]]
) -> dict[str, dict[str, str | list[str]]]:
    "Separates the str dump of properties into a list[str]."

    formated_css_dict: dict[str, dict[str, str | list[str]]] = {}
    for selectors, values in css_dict.items():
        split_properties: list[str] = re.split(";", values["props"])
        split_properties = [prop.replace("\n", "").strip() for prop in split_properties]

        for selector in selectors.split(","):
            selector = selector.strip()

            if selector not in formated_css_dict:
                formated_css_dict.setdefault(
                    selector, {"comment": values["comment"], "props": split_properties}
                )
            else:
                formated_css_dict[selector]["comment"] += values["comment"]
                formated_css_dict[selector]["props"] += split_properties

    return {
        key: {"comment": value["comment"], "props": sorted(value["props"])}
        for key, value in formated_css_dict.items()
    }


def sort_css_by_keys(css_dict) -> Dict[str, Dict[str, str]]:
    
    return {key: css_dict[key] for key in sorted(css_dict)}



def sort_css_by_html(css_dict, html_element_order):

    result = {}
    order_collector = []
    for html_elem in html_element_order:
        for css, value in css_dict.items():

            if (
                list(filter(None, re.split(" |:", css)))[0].strip() == html_elem
                and css not in result
            ):
                order_collector.append(css)
                result[css] = value

    return result

def generate_output_str(css_by_html: Dict[str, Dict[str, str]]) -> str:
    
    result_str: str = ''

    for key, value in css_by_html.items():

        if value['comment']:
            result_str += f"\n{value['comment']}\n"
        else:
            result_str += '\n'

        result_str += f"{key} {{\n"

        for prop in value['props']:
            result_str += f"    {prop};\n"

        result_str += "}\n"

    return result_str

# ====================
def main():

    parser = argparse.ArgumentParser(
        prog="sort_css", description="Sorts css declarations."
    )
    parser.add_argument(
        "filenames", metavar="target", nargs='*', help="CSS file's path."
    )
    parser.add_argument(
        "--by_html",
        action="store",
        type=str,
        help="Order CSS declarations by HTML's order.",
    )
    parser.add_argument(
        "-i",
        "--in_place",
        action="store_true",
        help="Edits file in-place.",
    )

    args = parser.parse_args()

    filenames = args.filenames
    by_html = args.by_html
    in_place = args.in_place

    for file_path in filenames:
        css_content = read_file(file_path)

        css_dict: dict[str, dict[str, str]] = css_to_dict(css_content)
        formated_css_dict: dict[str, dict[str, str | list[str]]] = format_css_dict(css_dict)
        
        # ===============================
        if by_html:
            ordered_html_elems: Tuple[str, ...] = get_html_element_order(by_html)
            sorted_css: Dict[str, Dict[str, str]] = sort_css_by_html(formated_css_dict, ordered_html_elems )
        else:
            sorted_css: Dict[str, Dict[str, str]]= sort_css_by_keys(formated_css_dict)
        # ===============================

        css_output = generate_output_str(sorted_css)

        # ===============================
        if in_place:
            with open(file_path, 'w', encoding='UTF-8') as file:
                file.write(css_output)
        else:
            print(css_output)
        # ===============================

if __name__ == '__main__':
    main()
