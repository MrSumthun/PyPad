import tkinter as tk
import sys

window = tk.Tk()
window.geometry("1280x720")

file = open("pypad.txt", "r+")

label = tk.Label(window, text="Basic Notepad")
label.pack()

text_widget = tk.Text(window, height=20, width=80)
text_widget.pack()
def exit():
    sys.exit(0)

exit_button = tk.Button(window, text="Exit", command=exit)

def get_text():
    text = text_widget.get("1.0", "end-1c")
    return text

def console_print():
    print(str(get_text()))    

print_button = tk.Button(window, text="Print to Console", command=console_print)

def print_to_file():
    file.seek(0)
    file.write(get_text())
    print("Write successful")
    file.flush()
    

write_file_button = tk.Button(window, text="Print to File", command=print_to_file)

def read_from_file():
    file.seek(0)
    file_text = file.read()
    text_widget.insert(tk.END, file_text)
    print("Read from file!")

read_file_button = tk.Button(window, text="Read from file", command=read_from_file)

def clear_text_area():
    text_widget.delete("1.0", tk.END)

clear_text_button = tk.Button(window, text="Clear Text Area", command=clear_text_area)

def clear_file():
    file.truncate(0)

clear_file_button = tk.Button(window, text="Clear File Contents", command=clear_file)


print_button.pack(side="left")
write_file_button.pack(side="left")
read_file_button.pack(side="left")
clear_file_button.pack(side="left")
clear_text_button.pack(side="left")
exit_button.pack(side="left")
window.mainloop()