import os 
from os import system
import sys
import time
import platform
 
# This file handles any console output, logging, and OS Detection for PyPad.

# Version Number
version_number = "2.0.1"

# Set up log file path and log file object
log_file_name = "PyPad_Log"
log_file_path = log_file_name + ".txt"
log_file = open(log_file_path, "a+")

# Here we log events to a log file
def log_event(x):
    print(x)
    log_file.seek(0, os.SEEK_END)
    log_file.write(time.ctime() + " - " + x + "\n")
    log_file.flush()

# Here we delete the log file contents
def delete_log():
    log_file.truncate(0)

# Where are we?
def detect_os():
    if platform.system() == "Darwin":
        return "MacOS"
    elif platform.system() == "Linux":
        return "Linux - Hackerman"
    else:
        return "Windows"

# Clears console based on OS function, again since Windows has to be different.
def clear_screen():
    if detect_os() == "Windows":
        system("cls")
    else:
        system("clear")

# Initializes console on program start.
def init_console():
    delete_log()
    clear_screen()
    print(" *** PyPad Version: " + version_number + " ***")
    log_event("Program Started - Version: " + version_number)
    log_event("Detected OS: " + detect_os())

def exit_program_gracefully():
    log_event("Program Exited by User at: " + time.ctime())
    print(" *** Exiting PyPad... ***")
    sys.exit(0)




