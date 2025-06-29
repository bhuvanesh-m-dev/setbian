import tkinter as tk
from tkinter import messagebox
import subprocess
import socket
import threading
import time

# Check for internet connection
def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 53), timeout=3)
        return True
    except OSError:
        return False

# Password prompt
def show_password_prompt():
    prompt = tk.Toplevel()
    prompt.title("Authentication Required")
    prompt.geometry("350x100")
    prompt.resizable(False, False)
    tk.Label(prompt, text="Please enter your password in the terminal...", font=("Arial", 11)).pack(pady=20)
    prompt.after(8000, prompt.destroy)

# Log window
def show_install_log():
    log_window = tk.Toplevel()
    log_window.title("Installation Progress")
    log_window.geometry("500x350")
    log_window.resizable(False, False)
    log_text = tk.Text(log_window, wrap=tk.WORD, font=("Arial", 11))
    log_text.pack(expand=True, fill='both')
    return log_text

# Install selected apps
def install_selected():
    selected_apps = []
    
    # Collect selected apt apps
    for name in apt_apps:
        if vars_check[name].get():
            selected_apps.append((name, 'apt', apt_apps[name]))
    
    # Collect selected deb apps
    for name in deb_apps:
        if vars_check[name].get():
            selected_apps.append((name, 'deb', deb_apps[name]))
    
    if not selected_apps:
        messagebox.showinfo("No Selection", "Please select at least one app to install.")
        return

    show_password_prompt()
    log_output = show_install_log()

    def run_installation():
        for name, app_type, cmd in selected_apps:
            try:
                log_output.insert(tk.END, f"📦 Starting {name}...\n")
                log_output.see(tk.END)

                if app_type == 'apt':
                    log_output.insert(tk.END, f"Installing {name} using APT...\n")
                    subprocess.run(["sudo", "apt", "install", "-y", cmd], check=True)
                elif app_type == 'deb':
                    log_output.insert(tk.END, f"Downloading and installing {name} (.deb)...\n")
                    subprocess.run(cmd, shell=True, check=True)

                log_output.insert(tk.END, f"✅ {name} installed successfully.\n\n")
            except subprocess.CalledProcessError:
                log_output.insert(tk.END, f"❌ Failed to install {name}\n\n")

            log_output.see(tk.END)

        log_output.insert(tk.END, "🎉 All installations attempted.\n")
        log_output.see(tk.END)

    threading.Thread(target=run_installation).start()

# Launch GUI if internet is available
if is_connected():
    # APT apps
    apt_apps = {
        "Git": "git",
        "Curl": "curl",
        "VLC Media Player": "vlc",
        "GIMP": "gimp",
        "VS Code (if repo added)": "code"
    }

    # .DEB apps (add more with proper wget & dpkg commands)
    deb_apps = {
        "Brave Browser (.deb)": "wget -O brave.deb https://brave.com/latest.deb && sudo dpkg -i brave.deb && sudo apt --fix-broken install -y && rm brave.deb",
        "AnyDesk (.deb)": "wget -O anydesk.deb https://download.anydesk.com/linux/anydesk_6.2.1-1_amd64.deb && sudo dpkg -i anydesk.deb && sudo apt --fix-broken install -y && rm anydesk.deb"
    }

    root = tk.Tk()
    root.title("Setbian - Smart Debian App Installer")
    root.geometry("500x600")
    root.resizable(False, False)

    tk.Label(root, text="📦 Select APT Apps to Install:", font=("Arial", 14, "bold")).pack(pady=10)
    vars_check = {}

    # APT checkboxes
    for app in apt_apps:
        var = tk.BooleanVar()
        chk = tk.Checkbutton(root, text=app, variable=var, font=("Arial", 12))
        chk.pack(anchor='w', padx=40)
        vars_check[app] = var

    tk.Label(root, text="📂 Install from .deb Files:", font=("Arial", 14, "bold"), fg="blue").pack(pady=10)

    # DEB checkboxes
    for app in deb_apps:
        var = tk.BooleanVar()
        chk = tk.Checkbutton(root, text=app, variable=var, font=("Arial", 12))
        chk.pack(anchor='w', padx=40)
        vars_check[app] = var

    # Install button
    install_btn = tk.Button(
        root, text="Install Selected", font=("Arial", 12, "bold"),
        bg="#4CAF50", fg="white", command=install_selected
    )
    install_btn.pack(pady=20)

    root.mainloop()

else:
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "No Internet Connection",
        "Please connect to the internet and relaunch Setbian.\n\nThank you!"
    )
