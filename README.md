### 🧰 Setbian – Smart Debian Setup Assistant

> Official APT package for Setbian — GUI-based batch installer for essential Debian apps.  
[![License](https://img.shields.io/badge/license-MIT-blue.svg )](https://github.com/bhuvanesh-m-dev/setbian/blob/main/document/LICENSE )
![Built with Python](https://img.shields.io/badge/Built%20with-Python-blue)
![Platform](https://img.shields.io/badge/Platform-Debian%20Linux-red)
![GUI](https://img.shields.io/badge/GUI-Tkinter-yellow)
![Latest Release](https://img.shields.io/github/v/release/bhuvanesh-m-dev/setbian)
![Project Status](https://img.shields.io/badge/Status-Active-brightgreen)
![DevOps Friendly](https://img.shields.io/badge/DevOps-Automated%20Builds-orange)
[![Download .deb](https://img.shields.io/badge/Download-.deb-blue)](https://github.com/bhuvanesh-m-dev/setbian/releases/download/v0.0.3/setbian-0.0.3.deb)   


![Setbian Banner](https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif)
## 📦 Install via APT

```bash
wget -O setbian.deb https://github.com/bhuvanesh-m-dev/setbian/releases/download/v0.0.3/setbian-0.0.3.deb && \
sudo dpkg -i setbian.deb || (sudo apt --fix-broken install -y && sudo dpkg -i setbian.deb) && \
setbian

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

<img src="https://raw.githubusercontent.com/bhuvanesh-m-dev/setbian/refs/heads/main/setbian/screenshot2.png" alt="Setbian Project Preview" width="1000">

---

## 🎥 Setbian Demo Video - See It in Action!  
🚀 Experience the power of Setbian in under 2 minutes!
Simplify your Debian system configuration with just a few clicks — no terminal hassle.Watch the full walkthrough and installation guide below:
[![Watch Setbian Demo](https://img.youtube.com/vi/xyKAwq2ITIU/0.jpg)](https://www.youtube.com/watch?v=xyKAwq2ITIU)

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

## 🔖 Version: `v0.0.4`

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
**Homepage:** [github.com/bhuvanesh-m-dev/Setbian](https://github.com/bhuvanesh-m-dev/Setbian)  
**Webpage:** [bhuvaneshm.in/setbian](https://bhuvaneshm.in/setbian)

License: MIT | Release: Stable
