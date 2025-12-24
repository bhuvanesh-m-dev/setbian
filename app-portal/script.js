document.addEventListener('DOMContentLoaded', () => {
    const appGrid = document.getElementById('app-grid');
    const searchInput = document.getElementById('app-search');
    const noResults = document.getElementById('no-results');

    let allApps = [];

    // Fetch App Data
    async function loadApps() {
        try {
            const registryResponse = await fetch('data/apps.json');
            if (!registryResponse.ok) throw new Error('Failed to load registry');
            const registry = await registryResponse.json();

            // Fetch details for each app
            const appPromises = registry.map(entry => fetch(entry.path).then(res => res.json()));
            allApps = await Promise.all(appPromises);

            renderApps(allApps);
        } catch (error) {
            console.error('Error loading apps:', error);
            appGrid.innerHTML = '<p>Error loading application store. Please check console.</p>';
        }
    }

    // Render App Cards
    function renderApps(apps) {
        appGrid.innerHTML = '';
        if (apps.length === 0) {
            noResults.classList.remove('hidden');
            return;
        }
        noResults.classList.add('hidden');

        apps.forEach(app => {
            const card = document.createElement('a');
            card.className = 'app-card';
            card.href = app.aboutPage; // Link to independent about page

            card.innerHTML = `
                <img src="${app.icon}" alt="${app.name} Icon" class="app-icon" onerror="this.src='/assets/icons/default.png'">
                <h2 class="app-name">${app.name}</h2>
                <div class="app-category">${app.category}</div>
                <p class="app-tagline">${app.tagline}</p>
                <button class="view-details-btn">View Details</button>
            `;

            appGrid.appendChild(card);
        });
    }

    // Live Search
    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();

        const filteredApps = allApps.filter(app => {
            const matchName = app.name.toLowerCase().includes(query);
            const matchTagline = app.tagline.toLowerCase().includes(query);
            const matchCategory = app.category.toLowerCase().includes(query);
            const matchKeywords = app.keywords && app.keywords.some(k => k.toLowerCase().includes(query));

            return matchName || matchTagline || matchCategory || matchKeywords;
        });

        renderApps(filteredApps);
    });

    // Initialize
    loadApps();
});
