import bs4  # type: ignore
from typing import Any


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


if __name__ == "__main__":
    html_dict: dict[str, list[Any] | dict[Any, Any]] = convert_html_to_dict(
                                                "../test/dummy_data/sample.html"
                                                )
