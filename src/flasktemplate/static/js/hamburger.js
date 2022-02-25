// Toggle between adding and removing the "responsive" class to topnav when the user clicks the icon

document.addEventListener("DOMContentLoaded", () => {
    document.getElementsByClassName("icon")[0].addEventListener("click", () => {
        let nav = document.getElementById("topnav");
    if (nav.className === "topnav") {
        nav.className += " responsive";
    } else {
        nav.className = "topnav";
    }
    })
})
