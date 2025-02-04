import tkinter as tk
import Console_Handler
import os

file_name = "PyPad"
file_path = file_name + ".txt"
file = open(file_path, "r+")

def read_file():
    file.seek(0)
    file_text = file.read()
    return file_text

def write_file(x):
    file.seek(0)
    file.write(x)
    file.flush()

def check_for_file():
    if os.path.exists(file_path):
        return "File Exists!"
    else:
        return "File does not Exist!" 

def clear():
    file.truncate(0)        

def Open_File_Handler():
    window = tk.Tk()
    title_label = tk.Label(window, text="File Manager", fg="white")
    exit_button = tk.Button(window, text="Exit", command=window.destroy)
    import_button = tk.Button(window, text="Import from File", command=check_for_file)
    export_button = tk.Button(window, text="Export to File")
    file_exists_label = tk.Label(window, fg="white")

    file_exists_label.config(text=check_for_file())

    title_label.grid(row=0, column=0)
    import_button.grid(row=1, column=2, padx=10, pady=10)
    export_button.grid(row=2, column=2, padx=10, pady=10)
    exit_button.grid(row=3, column=2, padx=10, pady=10)
    file_exists_label.grid(row=1, column=1, padx=10, pady=10)
    
    window.geometry("640x320")
    window.mainloop()
