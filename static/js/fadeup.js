
// Function to detect the scroll event
window.addEventListener('scroll', function () {
    const elements = document.querySelectorAll('.fade-up');

    elements.forEach(function (element) {
        // Check if the element is in the viewport
        const rect = element.getBoundingClientRect();
        if (rect.top <= window.innerHeight && rect.bottom >= 0) {
            // Add the "visible" class to trigger the fade-up animation
            element.classList.add('visible');
        }
    });
});

// Initially trigger the scroll event to check if elements are already visible
window.dispatchEvent(new Event('scroll'));
