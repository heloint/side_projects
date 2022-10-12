import re

with open('./test/dummy_data/sample.html', 'r', encoding='utf-8') as file:
    data = file.read()

# Find html tags
# ==================================
regex_tags = re.compile(r'<(.*?)>')
tags_content = regex_tags.findall(data)
# print(tags_content)

# Find classes
# ==================================
regex_classes = re.compile(r'class="(.*?)"')
classes = regex_classes.findall(data)
# print(classes)


# Find ids
# ==================================
regex_ids = re.compile(r'id="(.*?)"')
ids = regex_ids.findall(data)
# print(ids)
