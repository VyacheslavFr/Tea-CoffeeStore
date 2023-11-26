let btns = document.querySelectorAll("*[data-user-edit-profile-btn]")

for(let i = 0; i<btns.length; i++) {
    btns[i].addEventListener('click', function() {
        let name = btns[i].getAttribute('data-user-edit-profile-btn');
        let modal = document.querySelector("[data-user-edit-profile-window='"+name+"']");
        modal.style.display = "block";
        let close = modal.querySelector(".close_user_edit_profile_window");
        close.addEventListener('click', function () {
            modal.style.display = "none";
        })
    })
}

window.onclick = function (e) {
    if(e.target.hasAttribute('data-user-edit-profile-window')) {
        let modals = document.querySelectorAll("*[data-user-edit-profile-window]");
        for(let i = 0; i<modals.length; i++) {
            modals[i].style.display = "none";
        }
    }
}