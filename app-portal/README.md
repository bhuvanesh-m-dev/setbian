# Setbian App Portal

A modern, scalable App Store–style web portal for the Setbian Linux project.

## Project Structure

```
setbian-portal/
├── index.html          # Main portal entry point
├── style.css           # Global styles and app grid
├── script.js           # Dynamic app loader and search logic
├── data/
│   └── apps.json       # Central registry of apps
├── app/
│   ├── firefox/        # Firefox App Component
│   │   ├── meta.json   # Single source of truth for Firefox data
│   │   ├── about.html  # Independent about page
│   │   ├── about.css   # Independent styles
│   │   └── about.js    # Independent logic
│   └── vlc/            # VLC App Component (Placeholder)
└── assets/
    └── icons/          # App icons
```

## How It Works

1. **Dynamic Loading**: `script.js` fetches `data/apps.json`, then iterates through the registry to fetch each app's `meta.json`.
2. **Search**: The live search filters apps based on name, tagline, category, and keywords defined in `meta.json`.
3. **Decentralized Apps**: Each app is self-contained in its own folder in `app/`. Adding a new app requires adding a folder and registering it in `apps.json`.

## How to Contribute

### Adding a New App
1. Create a folder: `app/<app-name>/`.
2. Add `meta.json` with app details.
3. Add `about.html`, `about.css`, and `about.js` for the details page.
4. Add your icon to `assets/icons/`.
5. Register your app in `data/apps.json`.

### Development
- This project uses **Vanilla HTML/CSS/JS**. No build tools required.
- Open `index.html` in any modern web browser to run.

## License
Open Source.
