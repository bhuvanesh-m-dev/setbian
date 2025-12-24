// This file can be used for any interactive elements on the app's about page.
// For this example, it includes a simple console log to confirm loading and can be extended
// for features such as copying the Google Chrome installation command to the clipboard.
console.log("Google Chrome about page script loaded.");

// Example: Function to copy the Chrome installation command (optional enhancement)
// Uncomment and implement if a "Copy Install Command" button is present in about.html
/*
document.addEventListener('DOMContentLoaded', () => {
    const copyButton = document.getElementById('copy-install-command');
    if (copyButton) {
        copyButton.addEventListener('click', async () => {
            const installCommand = 'sudo apt install ./google-chrome-stable_current_amd64.deb';
            try {
                await navigator.clipboard.writeText(installCommand);
                copyButton.textContent = 'Copied!';
                setTimeout(() => { copyButton.textContent = 'Copy Install Command'; }, 2000);
            } catch (err) {
                console.error('Failed to copy text: ', err);
            }
        });
    }
});
*/