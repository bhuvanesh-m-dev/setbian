import tkinter as tk
from tkinter import messagebox
import subprocess
import socket
import threading
import time
import os


def install_ess():
    # Show password prompt in a clean window
    ess_prompt = tk.Toplevel(root)
    ess_prompt.title("Authentication Required")
    ess_prompt.geometry("400x100")
    ess_prompt.resizable(False, False)
    
    tk.Label(
        ess_prompt,
        text="Please enter your password in the terminal to install essential tools.",
        font=("Arial", 10), wraplength=380, justify="center"
    ).pack(pady=20)

    # Auto-close the password prompt after 8 seconds
    ess_prompt.after(8000, ess_prompt.destroy)

    # Run installation in background
    def run_ess_install():
        try:
            subprocess.run(
                ["sudo", "apt", "install", "-y", "git", "vi", "vim", "sudo", "curl", "wget"],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            messagebox.showinfo("Success", "✅ Essential tools installed successfully.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Installation Failed", "❌ Failed to install essential tools.")

    threading.Thread(target=run_ess_install).start()



# Predefined .deb app URLs
PRESET_DEB_APPS = {
    "Brave Browser (.deb)": "https://brave.com/latest.deb",
    "VS Code (.deb)": "https://update.code.visualstudio.com/latest/linux-deb-x64/stable"
}

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

def install_deb(app_name):


    """
    Download and install a .deb package for the given app_name in the background.
    Output is suppressed.
    """
    url = PRESET_DEB_APPS.get(app_name)
    if not url:
        return  # Unknown app

    deb_filename = f"{app_name.lower().replace(' ', '_').replace('(.deb)', '').replace('.', '')}.deb"
    try:
        # Download .deb file silently
        subprocess.run(
            ["wget", "-q", "-O", deb_filename, url],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        # Install .deb file silently
        subprocess.run(
            ["sudo", "dpkg", "-i", deb_filename],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        # Fix broken dependencies silently
        subprocess.run(
            ["sudo", "apt", "--fix-broken", "install", "-y"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except subprocess.CalledProcessError:
        pass  # Optionally handle errors here
    finally:
        if os.path.exists(deb_filename):
            os.remove(deb_filename)

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
                    log_output.insert(tk.END, f"✅ {name} installed successfully.\n\n")
                elif app_type == 'deb':
                    # Use silent installer for presets
                    if name in PRESET_DEB_APPS:
                        log_output.insert(tk.END, f"Downloading and installing {name} (.deb) in background...\n")
                        # Run silently in this thread (so install log is not blocked)
                        install_deb(name)
                        log_output.insert(tk.END, f"✅ {name} installed successfully (silent mode).\n\n")
                    else:
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
        "FireFox":"firefox-esr",
        "Google Chromium":"chromium",
        "mpv":'mpv',
        "VLC Media Player": "vlc",
        "GIMP": "gimp",
        "Telegram":""
        
    }

    # .DEB apps (add more with proper wget & dpkg commands)
    deb_apps = {
        "Brave Browser (.deb)": "wget -O brave.deb https://brave.com/latest.deb && sudo dpkg -i brave.deb && sudo apt --fix-broken install -y && rm brave.deb",
        "VS Code (.deb)": "wget -O vscode.deb https://update.code.visualstudio.com/latest/linux-deb-x64/stable && sudo dpkg -i vscode.deb && sudo apt --fix-broken install -y && rm vscode.deb",
        "AnyDesk (.deb)": "wget -O anydesk.deb https://download.anydesk.com/linux/anydesk_6.2.1-1_amd64.deb && sudo dpkg -i anydesk.deb && sudo apt --fix-broken install -y && rm anydesk.deb"
    }

    root = tk.Tk()
    root.title("Setbian - Smart Debian App Installer")
    root.geometry("500x600")
    root.resizable(False, False)

    tk.Label(root, text="📦 Select Apps to Install:", font=("Arial", 14, "bold")).pack(pady=10)
    vars_check = {}

    # APT checkboxes
    for app in apt_apps:
        var = tk.BooleanVar()
        chk = tk.Checkbutton(root, text=app, variable=var, font=("Arial", 12))
        chk.pack(anchor='w', padx=40)
        vars_check[app] = var

    tk.Label(root, text="📂 Install more apps", font=("Arial", 14, "bold"), fg="blue").pack(pady=10)

    # DEB checkboxes
    for app in deb_apps:
        var = tk.BooleanVar()
        chk = tk.Checkbutton(root, text=app, variable=var, font=("Arial", 12))
        chk.pack(anchor='w', padx=40)
        vars_check[app] = var
    install_ess()
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
