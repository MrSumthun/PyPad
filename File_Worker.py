import tkinter as tk
# Currently this file is a placeholder and will be implemented
# Need to add fancy file r/w with file creation and a seperate window

background_color = "#36013f"

def Open_File_Handler():
    window = tk.Tk()
    title_label = tk.Label(window, text="File Manager", fg="white")
    title_label.pack(side="top")
    

    window.geometry("640x480")
    window.mainloop()
    