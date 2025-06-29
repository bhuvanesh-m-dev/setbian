#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox
import subprocess
import socket

# Check for internet connection before launching the main UI
def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 53), timeout=3)
        return True
    except OSError:
        return False

# Function to install selected packages
def install_selected():
    selected = [pkg for name, pkg in available_apps.items() if vars_check[name].get()]
    
    if not selected:
        messagebox.showinfo("No Selection", "Please select at least one app to install.")
        return

    for pkg in selected:
        try:
            subprocess.run(
                ["sudo", "apt", "install", "-y", pkg],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except subprocess.CalledProcessError:
            messagebox.showerror("Installation Error", f"Failed to install {pkg}")
            return

    messagebox.showinfo("Success", "Selected apps installed successfully.")

# Launch GUI only if internet is connected
if is_connected():
    # Define available packages
    available_apps = {
        "Git": "git",
        "Curl": "curl",
        "VLC Media Player": "vlc",
        "GIMP": "gimp",
        "VS Code": "code",
        "FireFox":"firefox-esr",
        "Google Chromium":"chromium",
        "Mpv":'mpv',
        "Telegram":"telegram-desktop",
    }

    # GUI setup
    root = tk.Tk()
    root.title("Setbian - Smart Debian App Installer")
    root.geometry("400x350")
    root.resizable(False, False)

    tk.Label(root, text="Select Apps to Install:", font=("Arial", 14, "bold")).pack(pady=10)

    # Create checkboxes dynamically
    vars_check = {}
    for app in available_apps:
        var = tk.BooleanVar()
        chk = tk.Checkbutton(root, text=app, variable=var, font=("Arial", 12))
        chk.pack(anchor='w', padx=40)
        vars_check[app] = var

    # Install button
    install_btn = tk.Button(
        root,
        text="Install Selected",
        font=("Arial", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        command=install_selected
    )
    install_btn.pack(pady=20)

    # Run the app
    root.mainloop()

else:
    # Show internet error popup
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showerror(
        "No Internet Connection",
        "Please connect to the internet via Ethernet or Wi-Fi and relaunch Setbian.\n\nThank you!"
    )
