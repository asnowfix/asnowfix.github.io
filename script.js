document.addEventListener('DOMContentLoaded', function() {
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Initialize AOS (skipped when the visitor prefers reduced motion)
    AOS.init({
        disable: reduceMotion,
        duration: 800,
        easing: 'ease-out-cubic',
        once: true,
        offset: 50
    });

    // Footer year
    document.getElementById('year').textContent = new Date().getFullYear();

    // Smooth scrolling for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: reduceMotion ? 'auto' : 'smooth'
            });
        });
    });

    // Navbar background on scroll
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(15, 23, 42, 0.98)';
        } else {
            navbar.style.background = 'rgba(15, 23, 42, 0.95)';
        }
    });
});
