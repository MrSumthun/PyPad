import os

## TODO: Fix File Not Found excepetion when program is ran outside of its folder
## TODO: Implement Save As functionality
## TODO: Implement file dialog for choosing file location
## TODO: Implement file format options (eg .md, .txt, .rtf)

## File Worker handles all file reading and writing for PyPad

# Set up file path and file object
file_name = "PyPad"
file_path = file_name + ".txt"
file = open(file_path, "r+")

# Here we read
def read_file():
    file.seek(0)
    file_text = file.read()
    return file_text

# And here we write
def write_file(x):
    file.seek(0)
    file.write(x)
    file.flush()

# Here we verify the file hasn't had an extenstial crisis
def check_for_file():
    if os.path.exists(file_path):
        return "File Exists!"
    else:
        return "File does not Exist!" 

# Erases all content in the file via truncation
def clear():
    file.truncate(0)        


