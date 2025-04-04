document.addEventListener('DOMContentLoaded', function() {
    // Add heart animation
    const loveButton = document.getElementById('loveButton');
    if (loveButton) {
        // Restore liked state from localStorage
        if (localStorage.getItem('likedMemory') === 'true') {
            loveButton.classList.add('active');
        }

        loveButton.addEventListener('click', function() {
            this.classList.toggle('active');
            localStorage.setItem('likedMemory', this.classList.contains('active'));

            // Create heart animation
            if (this.classList.contains('active')) {
                createHeartAnimation();
            }
        });
    }

    // Autoplay videos on hover for memory thumbnails
    const memoryItems = document.querySelectorAll('.memory-item');

    memoryItems.forEach(item => {
        const video = item.querySelector('video');

        item.addEventListener('mouseenter', function() {
            this.style.transition = 'transform 0.3s ease';
            setTimeout(() => {
                this.style.transform = 'scale(1.1)';
                this.style.zIndex = '10';

                const overlay = this.querySelector('.play-overlay');
                if (overlay) {
                    overlay.style.opacity = '1';
                }
                if (video) {
                    video.play();
                }
            }, 100);
        });

        item.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
            this.style.zIndex = '1';

            const overlay = this.querySelector('.play-overlay');
            if (overlay) {
                overlay.style.opacity = '0';
            }
            if (video) {
                video.pause();
                video.currentTime = 0;
            }
        });
    });

    // Smooth scroll for memory sliders with mouse and touch support
    const sliders = document.querySelectorAll('.memory-slider');

    sliders.forEach(slider => {
        let isDown = false;
        let startX;
        let scrollLeft;

        slider.addEventListener('mousedown', (e) => {
            isDown = true;
            slider.style.cursor = 'grabbing';
            startX = e.pageX - slider.offsetLeft;
            scrollLeft = slider.scrollLeft;
        });

        slider.addEventListener('mouseleave', () => {
            isDown = false;
            slider.style.cursor = 'grab';
        });

        slider.addEventListener('mouseup', () => {
            isDown = false;
            slider.style.cursor = 'grab';
        });

        slider.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            e.preventDefault();
            const x = e.pageX - slider.offsetLeft;
            const walk = (x - startX) * 2;
            slider.scrollLeft = scrollLeft - walk;
        });

        // Touch Support
        slider.addEventListener('touchstart', (e) => {
            isDown = true;
            startX = e.touches[0].pageX - slider.offsetLeft;
            scrollLeft = slider.scrollLeft;
        });

        slider.addEventListener('touchend', () => {
            isDown = false;
        });

        slider.addEventListener('touchmove', (e) => {
            if (!isDown) return;
            const x = e.touches[0].pageX - slider.offsetLeft;
            const walk = (x - startX) * 2;
            slider.scrollLeft = scrollLeft - walk;
        });
    });

    //Splash Screen
    const splashScreen = document.getElementById('splash-screen');
    const mainContent = document.getElementById('main-content');
    const splashVideo = document.getElementById('splash-video');

    if (splashVideo) {
        splashVideo.onended = function() {
            splashScreen.style.display = 'none';
            mainContent.style.display = 'block';
        };
    }
});

// Function to create floating hearts animation
function createHeartAnimation() {
    const memoryDetails = document.querySelector('.memory-details');
    if (!memoryDetails) return;

    for (let i = 0; i < 15; i++) {
        const heart = document.createElement('div');
        heart.classList.add('floating-heart');
        heart.innerHTML = '♥';
        heart.style.color = '#e50914';
        heart.style.position = 'absolute';
        heart.style.fontSize = `${Math.random() * 20 + 10}px`;
        heart.style.left = `${Math.random() * 100}%`;
        heart.style.top = '100%';
        heart.style.opacity = 1;
        heart.style.transition = 'transform 2s ease-out, opacity 2s ease-out';

        memoryDetails.appendChild(heart);

        setTimeout(() => {
            heart.style.transform = `translateY(-100vh)`;
            heart.style.opacity = 0;
        }, 100);

        setTimeout(() => {
            heart.remove();
        }, 2000);
    }
}
