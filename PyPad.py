import tkinter as tk
import src.Console_Handler as Console_Handler
import src.File_Worker as File_Worker
import src.Settings as settings


window = tk.Tk()
Console_Handler.init()

# Initializing our commonly used variables
program_name = "PyPad"
window.title(program_name)
version_number = Console_Handler.version_number
userOS = Console_Handler.detect_os()

# Labels
title_label = tk.Label(window, text=program_name + "Version: " + version_number + " | "+ " Running on: " + userOS, fg="white")
status_label = tk.Label(window, width=20, height=5)

# Load settings
cfg = settings.load_settings()
window.geometry(cfg.get("geometry", "780x434"))

# theme resolution: saved preference overrides auto-detect
theme = cfg.get("theme", "auto")
if theme == "auto":
    if userOS == "Windows":
        bgColorPerOS = "white"
    else:
        bgColorPerOS = "black"
elif theme == "light":
    bgColorPerOS = "white"
else:
    bgColorPerOS = "black"

# Save settings on close
def on_close():
    # gather minimal state to persist
    cfg["geometry"] = window.winfo_geometry()
    cfg["theme"] = theme
    settings.save_settings(cfg)
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_close)

# Text area needs to change color because Windows has to be different
# TODO: Implement user switchable dark/light mode
if userOS == "Windows":
    bgColorPerOS = "white"
else:
    bgColorPerOS = "black"

# DEBUG: print("Automatic Background Detection: " + bgColorPerOS)
text_widget = tk.Text(window, height=20, width=100, bg=bgColorPerOS)

# Reverts status label back to null
def revert_status():
    status_label.config(text="")

# Controls status label
def status(x):
    label_text = str(x)
    status_label.config(text=label_text)
    status_label.after(1000, revert_status)

# Controls nabbing text from the textarea
def get_text():
    text = text_widget.get("1.0", "end-1c")
    return text

# Prints textarea to console
def console_print():
    print(str(get_text()))    
    text_widget.delete("1.0", tk.END)
    status("Printed to Console")

# Utilizes File_Worker to write using get_text() function call
def print_to_file():
    status("Write Success!")
    File_Worker.write_file(get_text())

# Utilizes File_Worker to read file, and call status function to alert user
def read_from_file():
    file_contents = File_Worker.read_file()
    if file_contents == "":
        status("File is Empty")
        text_widget.insert(tk.END, file_contents)
    else:
        text_widget.insert(tk.END, file_contents)
        status("Read Success!")

# Nulls out the text area     
def clear_text_area():
    text_widget.delete("1.0", tk.END)
    status("Cleared")

def clear_file():
    File_Worker.clear()
    status("File Cleared")

def resize_window():
    resize_window = tk.Toplevel()
    resize_window.title("Resize Window - PyPad")
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
            window.geometry(f"{width_int}x{height_int}")
            status("Window Resized")
            resize_window.destroy()
        except ValueError:
            Console_Handler.log_event("Invalid dimensions entered for resize.")
            status("Invalid dimensions")
# Reverts to saved size from settings
    def revert_resize():
        window.geometry(cfg.get("geometry", "780x434"))
        status("Reverted to Saved Size")
        resize_window.destroy()
# Reverts to default size per original app size
    def default_window_resize():
        window.geometry("780x434")
        status("Reverted to Default Size")
        resize_window.destroy()

    revert_button = tk.Button(resize_window, text="Revert to Saved Size", command=revert_resize)
    revert_button.pack()
    revert_factory_button = tk.Button(resize_window, text="Revert to Default Size", command=default_window_resize)
    revert_factory_button.pack()
    close_button = tk.Button(resize_window, text="Close", command=resize_window.destroy)
    close_button.pack()


def settings_window():
    window.title("Settings - PyPad")
    settings_win = tk.Toplevel(window)
    settings_win.geometry("250x160")
    resize_button = tk.Button(settings_win, text="Resize Window", command=resize_window)
    resize_button.pack()
    back_button = tk.Button(settings_win, text="Back", command=settings_win.destroy)
    back_button.pack()


#Declare button and called upon functions
exit_button = tk.Button(window, text="Exit", command=Console_Handler.exit_program_gracefully)    

print_button = tk.Button(window, text="Print to Console", command=console_print)

write_file_button = tk.Button(window, text="Print to File", command=print_to_file)

read_file_button = tk.Button(window, text="Read from File", command=read_from_file)

clear_text_button = tk.Button(window, text="Clear Text Area", command=clear_text_area)

clear_file_button = tk.Button(window, text="Clear File Contents", command=clear_file)

settings_button = tk.Button(window, text="Settings", command=settings_window)


# Sets placement of all elements
status_label.pack(side="bottom")
title_label.pack(side="top")

# Unecessary to declare side, defaults to middle in this placement
text_widget.pack() 

print_button.pack(side="left")
write_file_button.pack(side="left")
read_file_button.pack(side="left")

clear_file_button.pack(side="right")
clear_text_button.pack(side="right")

settings_button.pack(side="bottom")
exit_button.pack(side="bottom")



window.mainloop()
