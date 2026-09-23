"""Main application module.

This module provides a simple function to display a "Hello World"
alert using tkinter. The function is designed to be called from
other parts of the application or from tests.
"""

import tkinter as tk
from tkinter import messagebox

__all__ = ["show_hello_world"]


def show_hello_world():
    """Display a modal "Hello World" alert.

    The function creates a hidden Tk root window, shows the
    messagebox, and then destroys the root. This keeps the
    function self‑contained and safe to call from scripts or
    tests.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Hello", "Hello World")
    root.destroy()
