function injectDropdownMenu() {
    let dropdownHeaders = document.querySelectorAll('.dd-header');

    dropdownHeaders.forEach(function(header){
        console.log(header);
        header.innerHTML = 
    `
        <div class="dd" data-dropdown>
          <button class="dd-link" data-dropdown-button>Dropdown</button>
          <div class="dd-menu sub-dd-grid">

            <div>
              <div class="dd-heading">Subdropdown title</div>
              <div class="dd-links">
                <a href="#" class="dd-link">Anchor tag</a>
                <a href="#" class="dd-link">Anchor tag</a>
                <a href="#" class="dd-link">Anchor tag</a>
              </div>
            </div>

            <div>
              <div class="dd-heading">Subdropdown title</div>
              <div class="dd-links">
                <a href="#" class="dd-link">Anchor tag</a>
                <a href="#" class="dd-link">Anchor tag</a>
                <a href="#" class="dd-link">Anchor tag</a>
              </div>
            </div>
            
            <div>
              <div class="dd-heading">Subdropdown title</div>
              <div class="dd-links">
                <a href="#" class="dd-link">Anchor tag</a>
                <a href="#" class="dd-link">Anchor tag</a>
                <a href="#" class="dd-link">Anchor tag</a>
              </div>
            </div>
            
            <div>
              <div class="dd-heading">Subdropdown title</div>
              <div class="dd-links">
                <a href="#" class="dd-link">Anchor tag</a>
                <a href="#" class="dd-link">Anchor tag</a>
                <a href="#" class="dd-link">Anchor tag</a>
              </div>
            </div>

          </div>
        </div>
        <a href="#" class="dd-link">Anchor tag</a>
        <div class="dd" data-dropdown>
          <button class="dd-link" data-dropdown-button>Login dropdown</button>
          <div class="dd-menu">
            <form class="dd-login-form">
              <label for="email">Email</label>
              <input type="email" name="email" id="email">
              <label for="password">Password</label>
              <input type="password" name="password" id="password">
              <button type="submit">Login</button>
            </form>
          </div>
        </div>
    `;

    })
}



function activateDropdown(){

    document.addEventListener("click", e => {
      const isDropdownButton = e.target.matches("[data-dropdown-button]")
      if (!isDropdownButton && e.target.closest("[data-dropdown]") != null) return

      let currentDropdown
      if (isDropdownButton) {
        currentDropdown = e.target.closest("[data-dropdown]")
        currentDropdown.classList.toggle("dd-active")
      }

      document.querySelectorAll("[data-dropdown].dd-active").forEach(dropdown => {
        if (dropdown === currentDropdown) return
        dropdown.classList.remove("dd-active")
      })
    })

}

injectDropdownMenu();
activateDropdown();

