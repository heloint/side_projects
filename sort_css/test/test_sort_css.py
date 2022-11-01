import sys

sys.path.append("../src/sort_css")

import sort_css
from typing import Generator
from .expected_output_vars import EXPECTED_HTML_DICT 
from .expected_output_vars import EXPECTED_INCOMPLETE_HTML_DICT 

from .expected_output_vars import EXPECTED_HTML_ELEMS_ORDER 
from .expected_output_vars import EXPECTED_INCOMPLETE_HTML_ELEMS_ORDER

from .expected_output_vars import EXPECTED_ORDERED_HTML_ELEMS

# from .expected_output_vars import EXPECTED_ORDERED_INCOMPLETE_HTML_ELEMS

from .expected_output_vars import EXPECTED_CSS_DICT 

TEST_CSS_PATH = "./test_data/test_css.css"
TEST_HTML_PATH = "./test_data/test_html.html"
TEST_INCOMPLETE_HTML_PATH = "./test_data/test_incomplete_html.html"


def test_read_file():
    data = sort_css.read_file(TEST_CSS_PATH)
    assert isinstance(data, str)


def test_parse():

    with open(TEST_HTML_PATH, 'r', encoding='UTF-8') as file:
        html_str = file.read()

    test_output_dict = sort_css._parse(html_str)

    assert test_output_dict == EXPECTED_HTML_DICT 


def test_convert_html_to_dict():
    test_output_dict = sort_css.convert_html_to_dict(TEST_HTML_PATH)
    
    assert test_output_dict == EXPECTED_HTML_DICT

# PARAMETRIZE IT!
def test_get_identifiers_in_order():
    test_output_generator_complete = sort_css.get_identifiers_in_order(EXPECTED_HTML_DICT['html'])

    assert isinstance(test_output_generator_complete, Generator)
    assert tuple(test_output_generator_complete) == EXPECTED_HTML_ELEMS_ORDER


# PARAMETRIZE IT!
def test_get_html_element_order():
    test_output_tuple = sort_css.get_html_element_order(TEST_HTML_PATH)

    assert test_output_tuple == EXPECTED_ORDERED_HTML_ELEMS


def test_css_to_dict():

    TEST_CSS_PATH = "./test_data/test_css.css"

    with open(TEST_CSS_PATH, 'r', encoding='UTF-8') as file:
        css_content = file.read()

        test_output_dict = sort_css.css_to_dict(css_content)

        assert test_output_dict == EXPECTED_CSS_DICT


def test_format_css_dict():
    ...


def test_sort_css_by_keys():
    ...


def test_sort_css_by_html():
    ...


def test_generate_output_str():
    ...


def test_main():
    ...
