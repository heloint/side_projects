import re
from typing import Generator

with open('../test/dummy_data/sample.html', 'r', encoding='utf-8') as file:
    data = file.read()

# Find html tags
# ==================================
# regex_tags = re.compile(r'<([^/].*?)>')
# tags = regex_tags.findall(data)


# Find classes
# ==================================
# regex_classes = re.compile(r'class="(.*?)"')
# classes = regex_classes.findall(data)
# print(classes)


# Find ids
# ==================================
# regex_ids = re.compile(r'id="(.*?)"')
# ids = regex_ids.findall(data)
# print(ids)

# CURRENT
###############################

regex_ids_classes = re.compile(r'(?:id=".*?"|class=".*?")')
ids_and_classes = regex_ids_classes.findall(data)

def test(ids_and_classes: list[str]) -> Generator[str, None, None]:
    
    for attribute in ids_and_classes:

        attr_split: list[str] = attribute.split('=')
        attr_name:   str = attr_split[0]

        attr_value: Generator[str, None, None] = (attr.replace("'", '').replace('"', '') 
                                                        for attr in attr_split[1].split(' '))

        if attr_name.lower() == 'class':
            yield from (f'.{attr}' for attr in attr_value)
        elif attr_name.lower() == 'id':
            yield from (f'#{attr}' for attr in attr_value)


t = list(test(ids_and_classes))
# print(t)
