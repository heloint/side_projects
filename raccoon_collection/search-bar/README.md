![](https://github.com/heloint/raccoon_collection/blob/main/search-bar/sample_img/1-search-bar-img.png?raw=true)

# Search bar with lupa button.

# Usage

- Download the search-bar.style.css and search-button-icon.png file.
- Place them into their place in your project. (Example: "./css/", "./img/").

- Link the CSS file to your HTML.
```
<link rel="stylesheet" href="./css/search-bar.style.css">
```

- Add this DIV wherever you'd like. (Don't forget to change the action attr of the form.)
```
<div class="search-bar">
  <form class="search" action="http://localhost:5000" method="post">
    <input name="searchTerm" type="text" class="searchTerm" placeholder="What are you looking for?">
    <input type="image" class="searchSubmit" src="./img/search-button-icon.png" alt="Submit"  />
  </form>
</div>
```
