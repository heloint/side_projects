# In progress.. Will be a css sorter.

sort_css
========

## Installation
```bash
pip install sort_css
```

## Console scripts

Consult `sort_css --help` for the full set of options.
`sort_css` takes filenames as positional arguments.

Common options:
- `-h, --help`         show this help message and exit
- `--by_html BY_HTML`  Order CSS declarations by HTML's order.
- `-i, --in_place`     Edits file in-place.

## What does it do?


### Without `--by_html` flag.
### Separates block of grouped declarations and reorders them alphabetically the following way.
- General tags, like `<body>, <div>, <h1>, etc...` goes to the top of the file ordered alphabetically.
- Followed by the general tags, come the id or class specified declarations.

```diff
1c1,6
- /*FORM GENERAL*/
---
+ 
+ body {
+     margin: 0;
+     padding: 0;
+ }
+ 
3,9c8,9
- .form-container,
- .form-wrapper,
- .form-wrapper form,
- .form-wrapper form div {
- 	display: grid;
- 	align-items: center;
- 	justify-content: center;
---
+ h1 {
+     color: red;
12,17c12,16
- .form-wrapper {
- 	width: fit-content;
- 	padding: 1rem;
- 	border: 1px solid lightgrey;
- 	border-radius: 5px;
- 	background: linear-gradient(109.6deg, rgb(248,248,248) 30.1%, rgb(144,144,144) 100.2%);
---
+ /* ====================== */
+ .form-container {
+     align-items: center;
+     display: grid;
+     justify-content: center;
20,21c19,28
- .form-wrapper form {
- 	gap: 1rem;
---
+ /* ====================== */
+ .form-wrapper {
+     align-items: center;
+     background: linear-gradient(109.6deg, rgb(248, 248, 248) 30.1%, rgb(144, 144, 144) 100.2%);
+     border-radius: 5px;
+     border: 1px solid lightgrey;
+     display: grid;
+     justify-content: center;
+     padding: 1rem;
+     width: fit-content;
24,26c31,36
- body {
-     margin: 0;
-     padding: 0;
---
+ /* ====================== */
+ .form-wrapper form {
+     align-items: center;
+     display: grid;
+     gap: 1rem;
+     justify-content: center;
28a39
+ /* ====================== */
30c41,44
- 	gap: 0.5rem;
---
+     align-items: center;
+     display: grid;
+     gap: 0.5rem;
+     justify-content: center;
34,35c48,49
- 	text-align: center;
- 	font-weight: 450;
---
+     font-weight: 450;
+     text-align: center;
38,39c52,53
- .form-wrapper form label+input {
- 	font-size: 16px;
---
+ .form-wrapper form label + input {
+     font-size: 16px;
41,42d54
- /* ====================== */
- 
44,46d55
- h1 {
-     color: red;
- }
```
