import tkinter as tk
from tkinter import filedialog, messagebox
import os
from src.Handler import init_console, log_event, exit_program_gracefully, detect_os, version_number
import src.Settings as settings
import pyperclip

root = tk.Tk()
init_console()

global bg_color

# Load settings
default_window_size = "1200x800"
cfg = settings.load_settings()
root.geometry(cfg.get("geometry", default_window_size))
bg_color = cfg.get("theme", "white" if detect_os() == "Windows" else "black")
userOS = detect_os()

# Initializing our commonly used variables
program_name = "PyPad 2.0 - A Lightweight Text Editor | "
root.title(program_name)
version_number = version_number

text_widget = tk.Text(root, height=20, width=100, bg="white")
# Graceful exit function that saves settings before exiting, with confirmation dialog
def exit_program():
    if(messagebox.askokcancel("Exit", "Do you really want to exit?")):
        on_close()
        exit_program_gracefully()
    else:
        log_event("Exit cancelled by user.")

# Open file dialog and load selected file into text widget
def open_file():
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select a file",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )

    if file_path:
        #DEBUG: print(f"Selected file: {file_path}")
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                text_widget.delete("1.0", tk.END)  # Clear existing content
                text_widget.insert(tk.END, content)  # Insert new content
                status("File Loaded Successfully")
                log_event(f"File opened: {file_path}")
        except Exception as e:
            status(f"Error loading file: {e}")
            log_event(f"Error loading file {file_path}: {e}")
    else:
        print("No file selected.")
        log_event("Open file operation cancelled by user.")

# Save As dialog to save current text widget content to a new file
def save_file_as():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",  # Default extension if none is provided
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")], # Filter file types
        title="Save As"  # Title of the dialog window
    )
    if file_path:  # If a file path was selected (not cancelled)
        # DEBUG: print(f"Selected file path: {file_path}")
        with open(file_path, 'w') as f:
            f.write(get_text())
        status("File Saved Successfully")
        log_event(f"File saved to {file_path}")
        text_widget.delete("1.0", tk.END)  # Clear text area after saving
    else:
        status("Save As operation cancelled.")
        log_event("Save As operation cancelled by user.")

# Menubar setup
menubar = tk.Menu(root)
root.config(menu=menubar)
file_menu = tk.Menu(menubar, tearoff=False)
edit_menu = tk.Menu(menubar, tearoff=False)

# File Menu Commands
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save As...", command=save_file_as)
file_menu.add_separator()  # Add a visual separator
file_menu.add_command(label="Exit", command=exit_program)

# Edit Menu Commands, including Pyperclip functionality
def cut_content_to_clipboard():
    selected_text = text_widget.get("sel.first", "sel.last")
    pyperclip.copy(selected_text)
    text_widget.delete("sel.first", "sel.last")
    status("Cut to Clipboard")

def copy_content_to_clipboard():
    selected_text = text_widget.get("sel.first", "sel.last")
    pyperclip.copy(selected_text)
    status("Copied to Clipboard")

edit_menu.add_command(label="Cut", command=cut_content_to_clipboard)
edit_menu.add_command(label="Copy", command=copy_content_to_clipboard)

# Labels
title_label = tk.Label(root, text="Version: " + version_number + " | "+ " Running on: " + userOS, fg="white")
status_label = tk.Label(root, width=20, height=5)

# Save settings on close
def on_close():
    # Gather minimal state to persist
    cfg["geometry"] = root.winfo_geometry()
    cfg["theme"] = bg_color 
    settings.save_settings(cfg)
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

# Toggles theme between light and dark modes
def toggle_theme():
    global bg_color  # Add global declaration
    new_bg = "white" if text_widget.cget("bg") == "black" else "black"
    text_widget.config(bg=new_bg)
    bg_color = new_bg  # Update the global bg_color
    cfg["theme"] = new_bg
    settings.save_settings(cfg)
    status(f"Theme changed to {'Light' if new_bg == 'white' else 'Dark'}")

# Reverts status label back to null
def revert_status():
    status_label.config(text="")

# Controls status label
def status(x):
    label_erase_delay = 1200  # milliseconds
    label_text = str(x)
    status_label.config(text=label_text)
    status_label.after(label_erase_delay, revert_status)

# GIMME DAT TEXT
def get_text():
    text = text_widget.get("1.0", "end-1c")
    return text

# Prints textarea to console
def console_print():
    print(str(get_text()))    
    text_widget.delete("1.0", tk.END)
    status("Printed to Console")

# Nulls out the text area     
def clear_text_area():
    text_widget.delete("1.0", tk.END)
    status("Cleared")

# Here we handle window resizing
def resize_window():
    resize_window = tk.Toplevel()
    resize_window.title("Resize Window |" + program_name)
    resize_window.geometry("300x250")
    width_label = tk.Label(resize_window, text="Width:")
    width_label.pack()
    width_entry = tk.Entry(resize_window)
    width_entry.pack()
    height_label = tk.Label(resize_window, text="Height:")
    height_label.pack()
    height_entry = tk.Entry(resize_window)
    height_entry.pack()
    apply_button = tk.Button(resize_window, text="Apply", command=lambda: apply_resize(width_entry.get(), height_entry.get()))
    apply_button.pack()

    def apply_resize(width, height):
        try:
            width_int = int(width)
            height_int = int(height)
            root.geometry(f"{width_int}x{height_int}")
            status("Window Resized")
            resize_window.destroy()
        except ValueError:
            log_event("Invalid dimensions entered for resize.")
            status("Invalid dimensions")
    # Reverts to saved size from settings
    def revert_resize():
        root.geometry(cfg.get("geometry", "780x434"))
        status("Reverted to Saved Size")
        resize_window.destroy()
    # Reverts to default size per original app size
    def default_window_resize():
        root.geometry(default_window_size)
        status("Reverted to Default Size")
        resize_window.destroy()

    revert_button = tk.Button(resize_window, text="Revert to Saved Size", command=revert_resize)
    revert_button.pack()
    revert_factory_button = tk.Button(resize_window, text="Revert to Default Size", command=default_window_resize)
    revert_factory_button.pack()
    close_button = tk.Button(resize_window, text="Close", command=resize_window.destroy)
    close_button.pack()

def settings_window():
    root.title("Settings |" + program_name)
    settings_win = tk.Toplevel(root)
    settings_win.geometry("250x160")
    theme_button = tk.Button(settings_win, text="Toggle Theme", command=toggle_theme)
    theme_button.pack()
    resize_button = tk.Button(settings_win, text="Resize Window", command=resize_window)
    resize_button.pack()
    back_button = tk.Button(settings_win, text="Back", command=settings_win.destroy)
    back_button.pack()


#Declare button and called upon functions
view_log_button = tk.Button(root, text="View Log", command=lambda: os.startfile("PyPad_Log.txt") if userOS == "Windows" else os.system("open PyPad_Log.txt") if userOS == "MacOS" else os.system("xdg-open PyPad_Log.txt"))
exit_button = tk.Button(root, text="Exit", command=exit_program)    
print_button = tk.Button(root, text="Print to Console", command=console_print)
clear_text_button = tk.Button(root, text="Clear", command=clear_text_area)
settings_button = tk.Button(root, text="Settings", command=settings_window)


# Sets placement of all elements
status_label.pack(side="bottom")
title_label.pack(side="top")
text_widget.pack(side ="top", fill="both", expand=True) 
print_button.pack(side="left")
clear_text_button.pack(side="right")
exit_button.pack(side="right")
settings_button.pack(side="right")
view_log_button.pack(side="left")
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)

root.mainloop()
