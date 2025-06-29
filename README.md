### 🧰 Setbian – Smart Debian Setup Assistant

> Official APT package for Setbian — GUI-based batch installer for essential Debian apps.

---

## 📦 Install via APT

```bash
wget -O setbian.deb https://github.com/bhuvanesh-m-dev/setbian/releases/download/v0.0.1/setbian-0.0.1.deb && \
  sudo dpkg -i setbian.deb || sudo apt --fix-broken install -y || setbian
```

---

# 🧰 Setbian - Debian Setup Made Simple

> *"Because even your system deserves a proper welcome."*

**Setbian** is a lightweight, user-friendly GUI-based setup assistant for freshly installed **Debian** systems. Built with native Python and preinstalled libraries, Setbian helps you choose and install essential software — right after system setup, even **before you open the browser**.

---

## 🚀 Key Features

* ✅ Native Python GUI (no need to install extra libraries)
* ✅ App selection with tick-box interface
* ✅ Batch installation of essential Debian packages
* ✅ Runs on clean Debian install with just internet access
* ✅ Fully open-source and community-driven

---

## 💻 Screenshot Preview

<centre><img src="https://raw.githubusercontent.com/bhuvanesh-m-dev/setbian/refs/heads/main/setbian/screenshot1.png" alt="Setbian Project Preview" width="1000"></centre>

---

## ⚙️ How It Works

1. Boot into a fresh Debian install
2. Open terminal and run Setbian (coming `.deb` support)
3. Select the apps you want using the GUI
4. Hit "Install" — Setbian does the rest

---

## 📦 Example App List (Initial Version)

* Chromium
* VLC Media Player
* GParted
* Neofetch
* Curl
* Git
* VS Code
* And many more...

*You can customize the app list easily in the tick box !*

---

## 🧑‍💻 For Developers

Want to contribute? You're welcome!

```bash
git clone https://github.com/bhuvanesh-m-dev/Setbian.git
cd Setbian
python3 main.py
```

---

## 🔖 Version: `v0.0.1`

### ✅ Now Includes One-Click Install for:

* Git
* Curl
* VLC Media Player
* GIMP
* VS Code
* Firefox
* Google Chromium
* MPV
* Telegram Desktop

---

## 🎯 Key Features

* Simple GUI (Tkinter-based, no extra dependencies)
* Supports both APT and `.deb` package installations
* Password prompt with auto-close popup
* Live progress window with status logs
* Works on fresh Debian installs (only needs internet access)

---

## 🔧 Dev Info

**Maintainer:** Bhuvanesh M
**Email:** [bhuvaneshm.developer@gmail.com](mailto:bhuvaneshm.developer@gmail.com)
**Homepage:** [https://github.com/bhuvanesh-m-dev/Setbian](https://github.com/bhuvanesh-m-dev/Setbian)

License: MIT | Release: Stable
