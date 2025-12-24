document.addEventListener('DOMContentLoaded', () => {
    console.log('Firefox About Page Loaded');

    // Example independent behavior
    const installBtn = document.querySelector('.btn-install');
    installBtn.addEventListener('click', () => {
        alert('Setbian Package Manager: Installing Firefox...');
        // Mock install process
        installBtn.textContent = 'Installing...';
        setTimeout(() => {
            installBtn.textContent = 'Installed';
            installBtn.style.backgroundColor = '#28a745';
        }, 1500);
    });
});
