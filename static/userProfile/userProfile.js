var allList = document.querySelectorAll(".dashboard .list-box > li");
var allMenu = document.querySelectorAll(".user-page");
for (i = 0; i < 6; i++) {
    allList[i].onclick = changeMenu;
}

function changeMenu() {
    let name = this.id;
    let menuName = document.querySelector(`#${name} a span`).innerText;
    menuName = menuName.toLowerCase()
    for (i = 0; i < allMenu.length; i++) {
        allMenu[i].classList.add("hidden");
    }
    document.getElementById(menuName).classList.remove("hidden");
    console.log(menuName)
}