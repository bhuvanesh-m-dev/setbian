// Data Store
const appData = [
    {
        id: 1,
        name: "Setbian",
        description: "The core lightweight graphical tool for post-installation setup. Optimize your Debian system in seconds.",
        category: "tools",
        featured: true,
        version: "0.0.5",
        downloads: 1248,
        updated: "2023-10-15",
        license: "MIT",
        compatibility: ["Debian 11/12", "Ubuntu 22.04+"],
        downloadUrl: "#",
        icon: "🛠️"
    },
    {
        id: 2,
        name: "Setbian Term",
        description: "GPU-accelerated terminal emulator with built-in theming, ligatures, and split panes.",
        category: "utilities",
        featured: true,
        version: "1.2.0",
        downloads: 892,
        updated: "2023-10-10",
        license: "GPLv3",
        compatibility: ["All Linux"],
        downloadUrl: null,
        icon: "💻"
    }
];

// Init
document.addEventListener('DOMContentLoaded', () => {
    // Scroll Reveal Observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

    // Load Data
    setTimeout(() => {
        document.getElementById('loadingIndicator').style.display = 'none';
        updateStats();
        renderApps(appData);
    }, 800);
});

// App Rendering
function renderApps(apps) {
    const grid = document.getElementById('appGrid');
    grid.innerHTML = '';

    if (apps.length === 0) {
        grid.innerHTML = `
            <div style="grid-column: 1/-1; text-align: center; padding: 4rem; color: var(--text-secondary);">
                <h3>No apps found</h3>
                <p>Adjust your search filters</p>
            </div>`;
        return;
    }

    apps.forEach(app => {
        const card = document.createElement('div');
        card.className = 'app-card reveal active';

        // SVG generation based on emoji placeholder
        let svgContent = '';
        if (app.icon === '🛠️') svgContent = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>';
        else if (app.icon === '💻') svgContent = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>';
        else if (app.icon === '📝') svgContent = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>';
        else svgContent = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>';

        card.innerHTML = `
            <div class="app-header">
                <div class="app-icon" style="color: ${app.featured ? 'var(--accent-primary)' : 'white'}">
                    ${svgContent}
                </div>
                <div class="app-title-block">
                    ${app.featured ? '<span class="app-badge">Featured</span>' : ''}
                    <div class="app-name">${app.name}</div>
                    <div class="app-meta">v${app.version}</div>
                </div>
            </div>
            <div class="app-desc">${app.description}</div>
            <div class="card-actions">
                <button class="btn btn-primary" ${!app.downloadUrl ? 'disabled style="opacity:0.5; cursor:not-allowed;"' : ''} onclick="window.open('${app.downloadUrl}')">
                    ${app.downloadUrl ? 'Install' : 'Soon'}
                </button>
                <button class="btn btn-glass" onclick="showAppDetail(${app.id})">Details</button>
            </div>
        `;
        grid.appendChild(card);
    });
}

// Search & Filter Logic
let currentFilter = 'all';
const searchInput = document.getElementById('searchInput');

function filterLogic() {
    const term = searchInput.value.toLowerCase();
    const filtered = appData.filter(app => {
        const matchesSearch = app.name.toLowerCase().includes(term) || app.description.toLowerCase().includes(term);
        const matchesCat = currentFilter === 'all'
            ? true
            : (currentFilter === 'featured' ? app.featured : app.category === currentFilter);
        return matchesSearch && matchesCat;
    });
    renderApps(filtered);
}

function filterApps(category) {
    currentFilter = category;
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    event.target.classList.add('active');
    filterLogic();
}

searchInput.addEventListener('input', filterLogic);

// Stats Logic
function updateStats() {
    document.getElementById('total-apps').textContent = appData.length;
    document.getElementById('updated-today').textContent = appData.filter(a => a.updated === '2023-10-15').length; // Sim date

    let count = 0;
    const el = document.getElementById('active-contributors');
    const target = 42;
    const interval = setInterval(() => {
        count++;
        el.textContent = count;
        if (count >= target) clearInterval(interval);
    }, 30);
}

// Modals
function showAppDetail(id) {
    const app = appData.find(a => a.id === id);
    const content = document.getElementById('modalContent');
    content.innerHTML = `
        <div style="display:flex; gap:1.5rem; margin-bottom:2rem; align-items:center;">
            <div style="width:80px; height:80px; background:#222; border-radius:20px; display:flex; align-items:center; justify-content:center; font-size:2rem; border:1px solid var(--glass-border); box-shadow:0 0 20px var(--accent-glow);">
                ${app.icon}
            </div>
            <div>
                <h2 style="font-size:2rem; line-height:1.2;">${app.name}</h2>
                <span style="color:var(--accent-primary); font-family:'JetBrains Mono';">v${app.version}</span>
            </div>
        </div>
        
        <p style="font-size:1.1rem; margin-bottom:2rem; color:var(--text-primary);">${app.description}</p>
        
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:2rem;">
            <div class="modal-section">
                <h4>Details</h4>
                <div style="color:var(--text-secondary);">
                    <p>License: ${app.license}</p>
                    <p>Updated: ${app.updated}</p>
                    <p>Downloads: ${app.downloads.toLocaleString()}</p>
                </div>
            </div>
            <div class="modal-section">
                <h4>Compatibility</h4>
                <div style="display:flex; flex-wrap:wrap; gap:0.5rem;">
                    ${app.compatibility.map(c => `<span style="background:rgba(255,255,255,0.1); padding:4px 8px; border-radius:4px; font-size:0.8rem;">${c}</span>`).join('')}
                </div>
            </div>
        </div>
        
        <button class="btn btn-primary" style="width:100%; margin-top:1rem;" onclick="alert('Starting download for ${app.name}...')">Download .deb Package</button>
    `;
    document.getElementById('appModal').classList.add('active');
}

function showModal(type) {
    const titles = {
        vision: "Our Vision",
        publish: "Publish on Setbian",
        contribute: "Contribute Code"
    };
    const contents = {
        vision: "<p>We believe in a Linux that is powerful yet accessible. Setbian bridges the gap between the terminal and the GUI.</p>",
        publish: "<p>Developers can submit their .deb packages or repositories via our GitHub. We perform automated security checks before listing.</p>",
        contribute: "<p>Check our GitHub issues for 'good first issue' tags. We welcome PRs for both the core utility and this web portal.</p>"
    };

    document.getElementById('infoModalTitle').textContent = titles[type] || "Information";
    document.getElementById('infoModalContent').innerHTML = contents[type] || "<p>Content loading...</p>";
    document.getElementById('infoModal').classList.add('active');
}

function closeModal() { document.getElementById('appModal').classList.remove('active'); }
function closeInfoModal() { document.getElementById('infoModal').classList.remove('active'); }

window.onclick = function (e) {
    if (e.target.classList.contains('modal-overlay')) {
        closeModal();
        closeInfoModal();
    }
}
