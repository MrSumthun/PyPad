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


