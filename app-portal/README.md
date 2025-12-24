# Setbian App Portal

Welcome to the Setbian App Portal, a modern, App Store–style web portal for discovering and learning about applications available on Setbian Linux. This project is built with simplicity and contributor-friendliness in mind, using only vanilla HTML, CSS, and JavaScript.

## 🎯 Project Vision

Our goal is to create a clean, beautiful, and dynamic showcase for Setbian apps. The portal is designed to be fully decentralized—each application manages its own metadata, allowing for a scalable and easy-to-maintain system.

-   **Dynamic & Fast:** The portal loads app data asynchronously and features a live, as-you-type search.
-   **Contributor-Friendly:** Adding your app is as simple as creating a folder and a JSON file. No complex build steps required.
-   **Independent Apps:** Each app's information is self-contained, preventing changes to one app from affecting others.

## 🏗️ Folder & File Structure

The project uses a simple, intuitive file structure.

```
setbian-portal/
│
├── index.html          # Main landing page (the app store grid)
├── style.css           # Main stylesheet for the portal
├── script.js           # Core logic for loading apps and search
│
├── data/
│   └── apps.json       # The central registry of all apps
│
├── app/
│   └── <app-name>/     # Folder for a single application
│       ├── about.html  # The app's dedicated details page
│       ├── about.css   # Specific styles for the about page
│       ├── about.js    # Specific scripts for the about page
│       └── meta.json   # Single source of truth for the app's metadata
│
├── assets/
│   ├── icons/          # App icons (e.g., firefox.png)
│   └── images/         # Optional app screenshots or promotional images
│
└── README.md           # This file
```

## ✍️ How to Contribute & Add Your App

Adding a new application to the portal is designed to be extremely easy.

### Step 1: Create Your App Folder

Create a new folder for your app inside the `/app/` directory. The folder name should be simple, lowercase, and URL-friendly (e.g., `vlc`, `gimp`).

### Step 2: Add Your App's Metadata

Inside your new app folder, create a file named `meta.json`. This file contains all the information that will be displayed on the main grid.

**Example `meta.json`:**
```json
{
  "id": "your-app-id",
  "name": "Your App Name",
  "tagline": "A short, catchy tagline.",
  "category": "Productivity",
  "keywords": ["notes", "text-editor", "markdown"],
  "icon": "/assets/icons/your-app-icon.png",
  "aboutPage": "/app/your-app-id/about.html",
  "license": "GPL-3.0-or-later",
  "copyright": "© Your Name or Company"
}
```

-   **`icon`**: Add your app's icon (preferably a 256x256 PNG) to the `/assets/icons/` directory.
-   **`aboutPage`**: This path should point to the `about.html` you will create in the next step.

### Step 3: Create the "About" Page

Create the `about.html`, `about.css`, and `about.js` files inside your app's folder. This page will contain detailed information like feature lists, screenshots, and installation instructions. You can use the existing `app/firefox/` files as a template.

### Step 4: Register Your App

The final step is to add your app to the central registry. Open `/data/apps.json` and add a new entry pointing to your `meta.json` file.

**Example `data/apps.json`:**
```json
[
  { "path": "/app/firefox/meta.json" },
  { "path": "/app/your-app-id/meta.json" }
]
```

That's it! Your app will now automatically appear in the Setbian App Portal.

## 🚀 Local Development

No special tools are needed. Simply serve the `setbian-portal` directory with a local web server. A simple one can be run with Python:

```bash
# From inside the setbian-portal directory
python3 -m http.server
```

Then, open your browser to `http://localhost:8000`.

---

> “If you believe in developers, build for Linux.”
