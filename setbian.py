#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
import subprocess
import internet
from msg import msg, sudo_password_prompt, close_sudo_prompt, close_msg
from img import load_icon
import os
BASE_IMAGE_PATH = os.path.join(os.path.dirname(__file__), "images")
from install import *

# Ensure PIL is installed for image handling and run setbian's main codes
if img_install():
    def install_selected():
        selected = [pkg for name, pkg in available_apps.items() if vars_check[name].get()]
        if not selected:
            messagebox.showinfo("No Selection", "Please select at least one app to install.")
            return
        for name, pkg in available_apps.items():
            if vars_check[name].get():
                try:
                    msg(name, "Downloading and Installing...")
                    root.update()
                    subprocess.run(
                        ["sudo", "apt", "install", "-y", pkg["package"]],
                        check=True,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL
                        )
                    msg(name, "Installed successfully!")
                except subprocess.CalledProcessError:
                    msg(name, "Failed to install!")
                    messagebox.showerror("Installation Error", f"Failed to install {pkg}")
                    close_msg()
                    return
                close_msg()
                messagebox.showinfo("Success", "Selected apps installed successfully.")
    # Launch GUI only if internet is connected
    if internet.is_connected():
        # Define available packages and their image paths
        available_apps = {
            "Git": {"package": "git", "image": os.path.join(BASE_IMAGE_PATH, "git.png")},
            "Curl": {"package": "curl", "image": os.path.join(BASE_IMAGE_PATH, "curl.png")},
            "VLC Media Player": {"package": "vlc", "image": os.path.join(BASE_IMAGE_PATH, "vlc.png")},
            "GIMP": {"package": "gimp", "image": os.path.join(BASE_IMAGE_PATH, "gimp.png")},
            "VS Code": {"package": "code", "image": os.path.join(BASE_IMAGE_PATH, "vscode.png")},
            "FireFox": {"package": "firefox-esr", "image": os.path.join(BASE_IMAGE_PATH, "firefox.png")},
            "Google Chromium": {"package": "chromium", "image": os.path.join(BASE_IMAGE_PATH, "chromium.png")},
            "Mpv": {"package": "mpv", "image": os.path.join(BASE_IMAGE_PATH, "mpv.png")},
            "Telegram": {"package": "telegram-desktop", "image": os.path.join(BASE_IMAGE_PATH, "telegram-desktop.png")},
            }
        # GUI setup
        root = tk.Tk()
        root.title("Setbian - Smart Debian App Installer")
        root.geometry("400x600")
        root.resizable(False, False)
        tk.Label(root, text="Select Apps to Install:", font=("Arial", 14, "bold")).pack(pady=10)
        # Create icon-based checkboxes dynamically]
        vars_check = {}
        image_refs = {}  # To keep image objects from being garbage collected
        for app, details in available_apps.items():
            var = tk.BooleanVar()
            img = load_icon(details["image"], size=(36, 36))  # You can resize here
            frame = tk.Frame(root)
            frame.pack(anchor='w', padx=20, pady=4)
            if img:
                img_label = tk.Label(frame, image=img)
                img_label.pack(side='left', padx=5)
                image_refs[app] = img
                chk = tk.Checkbutton(frame, text=app, variable=var, font=("Arial", 12))
                chk.pack(side='left')
            else:
                fallback_label = tk.Label(frame, text="📦", font=("Arial", 14))
                fallback_label.pack(side='left', padx=5)
                vars_check[app] = var
                sudo_password_prompt()
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
