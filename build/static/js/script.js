function typeEffect(element, speed) {
    const text = element.innerHTML;
    element.innerHTML = '';
    let i = 0;
    const timer = setInterval(function() {
        if (i < text.length) {
            element.append(text.charAt(i));
            i++;
        } else {
            clearInterval(timer);
            element.classList.add('typing-effect');
        }
    }, speed);
}



document.addEventListener('DOMContentLoaded', function() {
    const h1 = document.querySelector('.hero h1');
    typeEffect(h1, 100);
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });

                // Add highlight effect
                targetElement.classList.add('highlight');
                setTimeout(() => {
                    targetElement.classList.remove('highlight');
                }, 1000);
            }
        });
    });

    const sections = document.querySelectorAll('section');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, { threshold: 0.1 });

    sections.forEach(section => {
        observer.observe(section);
    });

    // Lazy loading for the hero image
    const heroSection = document.querySelector('.hero');
    if (heroSection) {
        const img = new Image();
        img.src = getComputedStyle(heroSection).backgroundImage.slice(4, -1).replace(/"/g, "");
        img.onload = function() {
            heroSection.style.backgroundImage = `url(${img.src})`;
            heroSection.classList.add('loaded');
        };
    }

    // Add animation to timeline items
    const timelineItems = document.querySelectorAll('.timeline-item');
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    // const observer = new IntersectionObserver((entries, observer) => {
    //     entries.forEach(entry => {
    //         if (entry.isIntersecting) {
    //             entry.target.classList.add('animate');
    //             observer.unobserve(entry.target);
    //         }
    //     });
    // }, observerOptions);

    timelineItems.forEach(item => {
        observer.observe(item);
    });
});