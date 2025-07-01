#!/usr/bin/python3
import socket

# Check for internet connection before launching the main UI

def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 53), timeout=3)
        return True
    except OSError:
        return False
