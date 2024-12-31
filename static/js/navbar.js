document.addEventListener('DOMContentLoaded', function () {
    const navbar = document.getElementById('mainNavbar');
    window.addEventListener('scroll', function () {
        if (window.scrollY > 10) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
});

