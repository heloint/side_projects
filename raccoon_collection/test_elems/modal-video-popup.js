function stopVideo(modal) {
  let currentIframe = modal.querySelector('.modal-content > iframe');
  currentIframe.src = currentIframe.src;
}

function activateModalElement(modalElementID, triggerButtonID, modalCloseButtonID){

    let modalElement     = document.querySelector(`${modalElementID}`);
    let triggerButton    = document.querySelector(`${triggerButtonID}`);
    let modalCloseButton = document.querySelector(`${modalCloseButtonID}`);

    // When the user clicks the button, open the videoModal 
    triggerButton.addEventListener('click', () => {
        console.log(modalElement);
        modalElement.style.display = "block";
    })

    // When the user clicks on <span> (x), close the videoModal
    modalCloseButton.addEventListener('click', () => {
        modalElement.style.display = "none";
        stopVideo(modalElement);
    })

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
      if (event.target == modalElement){
        modalElement.style.display = "none";
        stopVideo(modalElement);
      }
    }
}

activateModalElement('#videoModal', '#videoBtn', '#videoClose');
