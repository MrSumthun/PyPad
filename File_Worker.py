import tkinter as tk
import Console_Handler

file_name = "PyPad"
file = open(file_name + ".txt", "r+")

def read_file():
    file.seek(0)
    file_text = file.read()
    return file_text

def write_file(x):
    file.seek(0)
    file.write(x)
    file.flush()

def clear_file():
    file.truncate(0)

def import_from_file():
    return

def export_to_file():
    return    

def Open_File_Handler():
    window = tk.Tk()
    title_label = tk.Label(window, text="File Manager", fg="white")
    exit_button = tk.Button(window, text="Exit", command=window.destroy)
    import_button = tk.Button(window, text="Import from File", command=import_from_file)
    export_button = tk.Button(window, text="Export to File", command=export_to_file)

    title_label.pack(side="top")
    exit_button.pack(side="bottom")
    import_button.pack(side="left")
    export_button.pack(side="left")
    window.geometry("640x480")
    window.mainloop()
