document.addEventListener('DOMContentLoaded', () => {
    const appGrid = document.getElementById('app-grid');
    const searchInput = document.getElementById('searchInput');
    let allApps = []; // To store all app data for filtering

    /**
     * Fetches the app registry and then loads each app's metadata.
     */
    async function loadApps() {
        try {
            const response = await fetch('/data/apps.json');
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            const appRegistry = await response.json();
            
            // Fetch metadata for all apps in parallel
            const appPromises = appRegistry.map(app => fetch(app.path).then(res => res.json()));
            allApps = await Promise.all(appPromises);
            
            renderApps(allApps);
        } catch (error) {
            console.error("Error loading app data:", error);
            appGrid.innerHTML = `<p class="error-message">Could not load app data. Please try again later.</p>`;
        }
    }

    /**
     * Renders an array of app data into the app grid.
     * @param {Array<Object>} apps - The array of app metadata to render.
     */
    function renderApps(apps) {
        appGrid.innerHTML = ''; // Clear existing content
        
        if (apps.length === 0) {
            appGrid.innerHTML = `<p class="no-results-message">No apps found.</p>`;
            return;
        }

        apps.forEach(app => {
            const card = document.createElement('div');
            card.className = 'app-card';
            card.dataset.appId = app.id;

            // Contributor Note: The icon path is from meta.json
            card.innerHTML = `
                <img src="${app.icon}" alt="${app.name} Icon" class="icon">
                <h3>${app.name}</h3>
                <p class="category">${app.category}</p>
                <p class="tagline">${app.tagline}</p>
                <a href="${app.aboutPage}" class="details-btn">View Details</a>
            `;
            
            // Make the whole card clickable
            card.addEventListener('click', (e) => {
                if (e.target.tagName !== 'A') {
                    window.location.href = app.aboutPage;
                }
            });

            appGrid.appendChild(card);
        });
    }

    /**
     * Filters apps based on the search input value.
     */
    function filterApps() {
        const query = searchInput.value.toLowerCase().trim();
        
        const filteredApps = allApps.filter(app => {
            const nameMatch = app.name.toLowerCase().includes(query);
            const taglineMatch = app.tagline.toLowerCase().includes(query);
            const categoryMatch = app.category.toLowerCase().includes(query);
            const keywordsMatch = app.keywords.some(kw => kw.toLowerCase().includes(query));
            
            return nameMatch || taglineMatch || categoryMatch || keywordsMatch;
        });

        renderApps(filteredApps);
    }

    // --- Event Listeners ---
    searchInput.addEventListener('input', filterApps);

    // --- Initial Load ---
    loadApps();
});
