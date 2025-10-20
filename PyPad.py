import tkinter as tk
import Console_Handler
import File_Worker

window = tk.Tk()
Console_Handler.init()

#Initializing our commonly used variables
window.geometry("800x400")
program_name = "PyPad"
version_number = Console_Handler.version_number
userOS = Console_Handler.detect_os()

#Labels
title_label = tk.Label(window, text=program_name + "Version: " + version_number + " | "+ " Running on: " + userOS, fg="white")
status_label = tk.Label(window)

#Text area needs to change color because Windows has to be different
if userOS == "Windows":
    bgColorPerOS = "white"
else:
    bgColorPerOS = "black"

print("Automatic Background Detection: " + bgColorPerOS)
text_widget = tk.Text(window, height=20, width=100, bg=bgColorPerOS)

#Reverts status label back to null
def revert_status():
    status_label.config(text="")

#Controls status label
def status(x):
    label_text = str(x)
    status_label.config(text=label_text)
    status_label.after(1000, revert_status)

def exit():
    Console_Handler.exit_()

#Controls nabbing text from the textarea
def get_text():
    text = text_widget.get("1.0", "end-1c")
    return text

#Prints textarea to console
def console_print():
    Console_Handler.print_user(str(get_text()))    
    text_widget.delete("1.0", tk.END)
    status("Printed to Console")

def print_to_file():
    status("Write Success!")
    File_Worker.write_file(get_text())

def read_from_file():
    file_contents = File_Worker.read_file()
    if file_contents == "":
        status("File is Empty")
        text_widget.insert(tk.END, file_contents)
    else:
        text_widget.insert(tk.END, file_contents)
        status("Read Success!")
    
def clear_text_area():
    text_widget.delete("1.0", tk.END)
    status("Cleared")

def clear_file():
    File_Worker.clear()
    status("File Cleared")

#Declare button and called upon functions
exit_button = tk.Button(window, text="Exit", command=exit)    

print_button = tk.Button(window, text="Print to Console", command=console_print)

write_file_button = tk.Button(window, text="Print to File", command=print_to_file)

read_file_button = tk.Button(window, text="Read from File", command=read_from_file)

clear_text_button = tk.Button(window, text="Clear Text Area", command=clear_text_area)

clear_file_button = tk.Button(window, text="Clear File Contents", command=clear_file)


# Sets placement of all elements
title_label.pack()
text_widget.pack()
print_button.pack(side="left")
write_file_button.pack(side="left")
read_file_button.pack(side="left")
clear_file_button.pack(side="right")
clear_text_button.pack(side="right")
exit_button.pack(side="bottom")
status_label.pack(side="bottom")

window.mainloop()
