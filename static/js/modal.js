const open = document.querySelector(".open");
const close = document.querySelector(".modal__closeBtn");
const modal = document.querySelector(".modal");
const bg = document.querySelector(".bg");

function init(){
    open.addEventListener("click", function () {
        console.log(modal.classList);
        modal.classList.remove("hidden");

    });

    close.addEventListener("click", function () {
        modal.classList.add("hidden");
    });

    bg.addEventListener("click", function () {
        modal.classList.add("hidden");
    });

}
init();