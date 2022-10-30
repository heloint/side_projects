import bs4  # type: ignore
from typing import Any
from itertools import chain


def read_html(path: str) -> str:
    """Reads the html file."""

    with open(path, "r", encoding="UTF-8") as file:
        html_content = file.read()

    return html_content


def recurse(
    html_groups: list[bs4.BeautifulSoup | Any],
    collector_dict: dict[str, list[str | dict] | dict[str, str | list]],
) -> dict[str, list[str | dict] | dict[Any, Any]]:
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


def parse(html_string: str) -> dict[str, list[Any] | dict[Any, Any]]:
    """Recursively parses the html_groups from BeautifulSoup4.html_parse and
    fetches to a hierarchical dictionary."""

    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(html_string, "html.parser")

    child_ls: list[bs4.PageElement] = [child for child in soup.contents]

    return recurse(child_ls, {})


def convert_html_to_dict(path: str) -> dict[str, list[Any] | dict[Any, Any]]:
    """Converts html to dictionary."""

    html_content: str = read_html(path)
    html_dict = parse(html_content)

    return html_dict

def get_identifiers_in_order(html_dict: dict[str, list[Any]]):
   

    start_node = html_dict

    if 'html' in html_dict.keys():
        start_node = html_dict['html'][0]['body'][0]

    for k, v in start_node.items():

        elem_collector: list[str] = [k]

        if isinstance(v, list):
            
            if 'attributes' in v[0]:
                if 'id' in v[0]['attributes']:
                    elem_collector += v[0]['attributes']['id'],
                if 'class' in v[0]['attributes']:
                    elem_collector += v[0]['attributes']['class'],
            
            yield elem_collector
            yield from get_identifiers_in_order(v[0])

def reformat_multidim_ls(ids_in_order):

    duplicate_checker: set = set()

    for identifier in chain(*ids_in_order):

        if isinstance(identifier, list):
            for elem in identifier:
                if elem not in duplicate_checker:
                    duplicate_checker.add(elem)
                    yield elem
        else:
            if identifier not in duplicate_checker:
                duplicate_checker.add(identifier)
                yield identifier

if __name__ == "__main__":
    html_dict: dict[str, list[Any] | dict[Any, Any]] = convert_html_to_dict(
                                                "../test/dummy_data/sample.html"
                                                )
    
    ids_in_order = tuple(get_identifiers_in_order(html_dict))
    flattened_id_ls = tuple(reformat_multidim_ls(ids_in_order))
    print(flattened_id_ls)
