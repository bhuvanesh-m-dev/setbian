import subprocess
import os

def img_install():
    install_cmd = "sudo apt install -y python3-pil.imagetk"

    # Detect terminal emulator
    terminals = ["gnome-terminal", "x-terminal-emulator", "xterm", "konsole", "lxterminal"]
    for term in terminals:
        if subprocess.call(f"which {term}", shell=True, stdout=subprocess.DEVNULL) == 0:
            terminal = term
            break
    else:
        print("No compatible terminal emulator found.")
        return

    # Build command to run inside the new terminal
    terminal_cmd = [terminal, "--", "bash", "-c", f"{install_cmd}; exec bash"]

    try:
        subprocess.Popen(terminal_cmd)
    except Exception as e:
        print(f"Failed to open terminal: {e}")

img_install()
