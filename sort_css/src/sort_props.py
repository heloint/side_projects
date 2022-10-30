import re
import cssutils  # type: ignore
import logging
from get_html_element_order import get_html_element_order
from typing import Generator, Dict

# To silence the warnings and error messages in stdout while using cssutils.parseString.
# It's not informative, doesn't affect the funcionality 
# of the stylesheet and unnecessarly verbose.
cssutils.log.setLevel(logging.CRITICAL)  # type: ignore

def read_css(path: str) -> str:
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
                css_dict.setdefault(rule.selectorText, {"comment": "", 
                                                        "props": ""
                                                        })

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
        split_properties = re.split(";", values["props"])
        split_properties = [prop.replace("\n", "").strip() 
                                for prop in split_properties]

        for selector in selectors.split(','): 

            formated_css_dict.setdefault(
                selector, {"comment": values["comment"], 
                           "props": sorted(split_properties)}
            )

    return formated_css_dict


def generate_css_strings(
        formated_dict: dict[str, dict[str, str | list[str]]]
                                            ) -> dict[str, str]:
    '''Converts the formated css dictionary 
       into (selector: pretty_string) dictionary.'''

    sorted_properties_dict: dict[str, str] = {}

    for selector, values in formated_dict.items():
        pretty_str: str = f"{values['comment']}\n"
        pretty_str += f"{selector} {{\n"

        for prop in values["props"]:
            pretty_str += f"    {prop};\n"

        pretty_str += "}"

        sorted_properties_dict[selector] = pretty_str

    return sorted_properties_dict



def  reorder_properties_dict(html_elem_order: Generator[str, None, None], properties_dict: Dict[str, str]) -> Dict[str, str]:


    for key, value in properties_dict.items():
        for identifier in html_elem_order:
            if identifier in key:

                try: 
                    yield (key.strip(), value)
                except KeyError:
                    continue




if __name__ == "__main__":

    css_content = read_css("../test/dummy_data/test_css.css")

    css_dict: dict[str, dict[str, str]] = css_to_dict(css_content)

    formated_css_dict: dict[str, 
                            dict[str, 
                                 str | list[str]]] = format_css_dict(css_dict)
   
    # THis part is for that case if the "by_html" flag is used.
    # ================
    t = get_html_element_order("../test/dummy_data/sample.html")

    x = ((key, formated_css_dict[key]) for key in t if any(key in identifier for identifier in formated_css_dict))
    
    for i, j in dict(x).items():
        print('=======')
        print(i, j)
        print('=======')
