document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const button = document.getElementById('analyze-btn');
    const textarea = document.getElementById('content');
    const resultOverlay = document.querySelector('.result-overlay');
    const logo = document.querySelector('.logo');

    // Logo click reloads the page
    logo.addEventListener('click', (e) => {
        // Only if it's the home link or a reload
        // We use preventDefault and then reload to ensure a clean state
        e.preventDefault();
        window.location.href = '/';
    });

    // Handle form submission and loading state
    form.addEventListener('submit', () => {
        button.disabled = true;
        button.style.opacity = '0.7';
        button.innerHTML = `
            <svg class="animate-spin" style="width: 24px; height: 24px; border: 2px solid #fff; border-top-color: transparent; border-radius: 50%;" viewBox="0 0 24 24"></svg>
            Analyzing...
        `;
    });

    // Auto-focus on textarea
    textarea.focus();

    // Fade in result if it exists and scroll to it
    if (resultOverlay) {
        resultOverlay.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    // Optional: Add hotkey (Ctrl + Enter to submit)
    textarea.addEventListener('keydown', (e) => {
        if (e.ctrlKey && e.key === 'Enter') {
            form.submit();
        }
    });
});
