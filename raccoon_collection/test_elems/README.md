![](https://github.com/heloint/raccoon_collection/blob/main/test_elems/sample_img/1-modal-video-popup.png?raw=true)

# Popup embedded video modal.

# Usage

- Download the modal-video-popup.style.css and modal-video-popup.js file.
- Place them into their place in your project. (Example: "./css/", "./js/").

- Link the JS and CSS file to your HTML.
```
<link rel="stylesheet" href="./css/modal-video-popup.style.css">
<script src="./js/modal-video-popup.js" defer></script>
```

- Add this button to trigger.
```
<button id="videoBtn" >Best Openings</button>
```

- Add this DIV wherever you'd like.
```
<!-- The Modal -->
<div id="videoModal" class="modal"> 
    <!-- Modal content -->
    <div class="modal-content">
        <div class="modalClose-wrapper">
            <div id="videoClose">&times;</div>
        </div>
        <iframe class="popup-video"
            src="https://www.youtube.com/embed/zqLEO5tIuYs">
        </iframe>
    </div>
</div>
```
