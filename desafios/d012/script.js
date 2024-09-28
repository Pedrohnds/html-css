window.addEventListener('resize', function() {
    const images = document.querySelectorAll('.image, .image2');
    if (window.innerWidth <= 250) { 
        images.forEach(el => {
            el.style.backgroundAttachment = 'scroll';
        });
    } else {
        images.forEach(el => {
            el.style.backgroundAttachment = 'fixed';
        });
    }
});

// Chamada inicial
window.dispatchEvent(new Event('resize'));