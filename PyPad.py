import tkinter as tk
import sys
import Console_Handler
import time
import File_Worker

window = tk.Tk()
Console_Handler.init()

#Initializing our commonly used variables
window.geometry("1280x720")
program_name = "PyPad"
version_number = Console_Handler.version_number
file = open(program_name + ".txt", "r+")

title_label = tk.Label(window, text=program_name + "Version: " + version_number + " | "+ " Running on: " + Console_Handler.detect_os(), fg="white")
status_label = tk.Label(window)

#Text area will always have a black background for readability
text_widget = tk.Text(window, height=20, width=100, bg="black")

def revert_status():
    status_label.config(text="")

def status(x):
    label_text = str(x)
    status_label.config(text=label_text)
    status_label.after(1000, revert_status)

def exit():
    Console_Handler.exit_()
    sys.exit(0)

exit_button = tk.Button(window, text="Exit", command=exit)

def get_text():
    text = text_widget.get("1.0", "end-1c")
    return text

def console_print():
    Console_Handler.print_user(str(get_text()))    
    text_widget.delete("1.0", tk.END)
    status("Printed to Console")

print_button = tk.Button(window, text="Print to Console", command=console_print)

def print_to_file():
    file.seek(0)
    file.write(get_text())
    status("Write Success!")
    text_widget.delete("1.0", tk.END)
    file.flush()

write_file_button = tk.Button(window, text="Print to File", command=print_to_file)

def read_from_file():
    file.seek(0)
    file_text = file.read()
    text_widget.insert(tk.END, file_text)
    status("Read Success!")

read_file_button = tk.Button(window, text="Read from File", command=read_from_file)

def clear_text_area():
    text_widget.delete("1.0", tk.END)
    status("Cleared")

clear_text_button = tk.Button(window, text="Clear Text Area", command=clear_text_area)

def clear_file():
    file.truncate(0)
    status("Cleared")

clear_file_button = tk.Button(window, text="Clear File Contents", command=clear_file)

def fileworks():
    File_Worker.Open_File_Handler()

fileworks_button = tk.Button(window, text="File Manager", command=fileworks)


# Sets placement of all elements
title_label.pack()
text_widget.pack()
print_button.pack(side="left")
write_file_button.pack(side="left")
read_file_button.pack(side="left")
clear_file_button.pack(side="right")
clear_text_button.pack(side="right")
fileworks_button.pack(side="right")
exit_button.pack(side="bottom")
status_label.pack(side="bottom")

window.mainloop()