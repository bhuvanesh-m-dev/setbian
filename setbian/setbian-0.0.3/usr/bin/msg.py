#!/usr/bin/python3
import tkinter as tk

def msg(pkg_name, status):
    
    if not hasattr(msg, "popup"):
        msg.popup = tk.Toplevel()
        msg.popup.title("Installation Progress")
        msg.popup.geometry("350x100")
        msg.label = tk.Label(msg.popup, text="", font=("Arial", 12))
        msg.label.pack(pady=20)
        msg.popup.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable close

    msg.label.config(text=f"{pkg_name}: {status}")
    msg.popup.update()

def msg_progress(pkg_name, phase, percent):
    
    if not hasattr(msg_progress, "popup"):
        msg_progress.popup = tk.Toplevel()
        msg_progress.popup.title("Installation Progress")
        msg_progress.popup.geometry("350x100")
        msg_progress.label = tk.Label(msg_progress.popup, text="", font=("Arial", 12))
        msg_progress.label.pack(pady=20)
        msg_progress.popup.protocol("WM_DELETE_WINDOW", lambda: None)

    msg_progress.label.config(text=f"{pkg_name}: {phase}... {percent}%")
    msg_progress.popup.update()

def close_progress():
    if hasattr(msg_progress, "popup"):
        msg_progress.popup.destroy()
        del msg_progress.popup

def sudo_password_prompt():
    """
    Show a popup window indicating that sudo password is required.
    """
    if not hasattr(sudo_password_prompt, "popup"):
        sudo_password_prompt.popup = tk.Toplevel()
        sudo_password_prompt.popup.title("Sudo Password Required")
        sudo_password_prompt.popup.geometry("350x100")
        label = tk.Label(
            sudo_password_prompt.popup,
            text="Please enter your sudo password in the terminal...",
            font=("Arial", 12),
            fg="red"
        )
        label.pack(pady=20)
        sudo_password_prompt.popup.protocol("WM_DELETE_WINDOW", lambda: None)
        sudo_password_prompt.popup.update()
        # Auto-close after 8 seconds
        sudo_password_prompt.popup.after(8000, close_sudo_prompt)

def close_sudo_prompt():
    if hasattr(sudo_password_prompt, "popup"):
        sudo_password_prompt.popup.destroy()
        del sudo_password_prompt.popup

def close_msg():
    if hasattr(msg, "popup"):
        msg.popup.destroy()
        del msg.popup
    close_progress()
    close_sudo_prompt()

