// Navbar

document.querySelector(function () {
    document.querySelector(document).click(function (event) {
        var clickover = document.querySelector(event.target);
        var _opened = document.querySelector(".navbar-collapse").classList.contains("navbar-collapse collapse show");
        if (_opened === true && !clickover.classList.contains("navbar-toggler")) {
            document.querySelector("button.navbar-toggler").click();
        }
    });
});
