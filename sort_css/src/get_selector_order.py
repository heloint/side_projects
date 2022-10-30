import parse_html_to_dict
from pprint import pprint

t = parse_html_to_dict.convert_html_to_dict('../test/dummy_data/sample.html')
print(t)

