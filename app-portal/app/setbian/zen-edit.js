/* ZenEdit Script */
console.log('ZenEdit Page Loaded');

function startDownload() {
    // Simulate download
    const btn = document.getElementById('downloadBtn');
    const originalText = btn.innerText;
    btn.innerText = 'Downloading...';
    btn.style.opacity = '0.7';

    setTimeout(() => {
        btn.innerText = 'Download Started';
        btn.style.opacity = '1';
        setTimeout(() => {
            btn.innerText = originalText;
        }, 2000);
    }, 1000);
}
