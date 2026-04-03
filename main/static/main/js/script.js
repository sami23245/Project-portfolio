// Theme Toggle Logic
function toggleTheme() {
    const body = document.body;
    const isDay = body.getAttribute('data-theme') === 'day';
    
    if (isDay) {
        body.setAttribute('data-theme', 'night');
        localStorage.setItem('portfolio-theme', 'night');
    } else {
        body.setAttribute('data-theme', 'day');
        localStorage.setItem('portfolio-theme', 'day');
    }
}

// Load Saved Theme on Startup
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('portfolio-theme') || 'night';
    document.body.setAttribute('data-theme', savedTheme);
});