# TODO list for "sort_css":

## Create requirements.txt

---

## Flags:

### --write
1. Function to rewrite the same file with the output.
---

### --only_selectors
Sort only the selector and their properties grouped and alphabetically.

1. Read css (css_file_path: str) -> css_content: str
2. Parse css (css_content: str)  -> dict[str, str]
3. Format dict. to "selector: list of props -> dict[str, list[str]]
4. Format props in dict. values => "key: value,"
5. Parse dictionary and do the following:
    - init empty dict.
    - for loop the dict. keys as "for current_key, next_key in dict.keys() ..."
    - compare current_key, next_key values:
        1. similarity = set(dict[current_key]) - set(dict[next_key])
        2. current_key_leftover = list(set(dict[current_key]) - similarity)
        3. next_key_leftover = list(set(dict[next_key]) - similarity)
        4.1. if len(list(similarity)) != 0: 
            - Format "merged key" string from the curr. and next key.
            - empty_dict['merged_key'] = list(similarity)
        4.2. After if statement..
                - empty_dict[current_key] = current_key_leftover
                - empty_dict[next_key] = next_key_leftover
6. grouped_dict. = empty_dict
7. Sort values: list[str] alphabetically.
8. Pretty-print grouped_dict.

---

### --sort_by_html
Alphabetize selectors in groups of increasing specificity (i.e., tags > classes > ids).

NOTE: Don't use external libs like 'xmltodict/xmltojson'. Too much overhead and
way too sensible its tokenization. Use simple regex...

1. Read html file.
2. Parse html file to dictionary.
3. Parse dictionary and extract each keys (if key is in the keys of the selectors dictionary).
   Using yield will give a generator with the exact order corresponding to the html file's tags.
   Extract only: tags, classes, ids.
4. Order the already sorted selectors to their place.
5. Pretty-print result.

EXTRA: If there's time and energy to do:
    - Would be nice the availability to get html html from URL and not just local.

---

## Problems to be looked up:
- Keep the corresponding comments of the declarations.
