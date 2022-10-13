import bs4
from pprint import pprint

def recurse( html_groups, collector_dict):

    for group in html_groups:
        if not isinstance(group, str):

            if not group.name in collector_dict:
                collector_dict[group.name] = []

            tmp_collector = {}

            if group.attrs:
                tmp_collector = {'attributes': group.attrs}

            collector_dict[group.name] += (recurse( group, tmp_collector),)

    return collector_dict


def parse(html_string):
    """parse the html string to json."""

    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(html_string, 'html.parser')

    l = [child for child in soup.contents]
    return recurse( l, {})

with open('../test/dummy_data/sample.html', 'r', encoding='UTF-8') as file:
    data = file.read()

t = parse(data)
pprint(t)
