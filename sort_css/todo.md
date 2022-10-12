# TODO list for "sort_css":

## Create requirements.txt

---

## Flags:

### --write
1. Function to rewrite the same file with the output.
---

### --only_selectors
[x] Sort only the selector and their properties grouped and alphabetically.

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
[solved] - Keep the corresponding comments of the declarations.
