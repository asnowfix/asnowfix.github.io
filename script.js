document.addEventListener('DOMContentLoaded', function() {
    // Typed.js for dynamic text
    new Typed('#typed-text', {
        strings: [
            'Senior Software Architect',
            'Cloud Automation Expert',
            'System Software Developer'
        ],
        typeSpeed: 50,
        backSpeed: 50,
        loop: true
    });

    // Smooth scrolling for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Contact form submission (placeholder)
    const contactForm = document.getElementById('contactForm');
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('Thank you for your message! I will get back to you soon.');
        contactForm.reset();
    });
});
