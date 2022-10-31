import bs4  # type: ignore
from typing import Any,Dict,List, Generator
from itertools import chain


def read_html(path: str) -> str:
    """Reads the html file."""

    with open(path, "r", encoding="UTF-8") as file:
        html_content = file.read()

    return html_content


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

    html_content: str = read_html(path)
    return parse(html_content)


# def get_identifiers_in_order(html_dict: Dict[str, List[Any]]):
#     ''' Recursively parses the html element hierarchy, and yields out the tags, ids and classes.
#     '''

#     start_node = html_dict

#     if 'html' in html_dict.keys():
#         start_node = html_dict['html'][0]['body'][0]

#     for k, v in start_node.items():

#         elem_collector: list[str] = [k]

#         if isinstance(v, list):
            
#             for elem in v:
#                 if isinstance(elem, dict):
#                     if 'attributes' in elem:

#                         if 'id' in elem['attributes']:
#                             elem_collector += f"#{elem['attributes']['id']}",

#                         if 'class' in elem['attributes']:
#                             elem_collector += elem['attributes']['class'],
#                     else:
#                         elem_collector += list(elem.keys())

            
#             yield elem_collector
#             yield from get_identifiers_in_order(v[0])


def get_identifiers_in_order(html_dict: Dict[str, List[Any]]):
    
    
    start_node = html_dict

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



def remove_duplicates_order_safe(identifiers_in_order):
    return tuple(dict.fromkeys(identifiers_in_order))


def get_html_element_order(path: str) -> Generator[str, None, None]:
    html_dict: Dict[str, List[str | Dict[str, Any]] | Dict[str, str | List[Any]]] = convert_html_to_dict(path)
    identifiers_in_order = get_identifiers_in_order(html_dict)
    
    return remove_duplicates_order_safe(identifiers_in_order )

if __name__ == "__main__":
    t = get_html_element_order("../test/dummy_data/sample.html")
    print(t)
