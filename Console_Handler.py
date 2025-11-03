from os import system
import sys
import time
import platform

## TODO: Implement logging functionality
## TODO: Implement more robust OS Detection
## TODO: Implement more console features (eg colored text, etc)
## TODO: Research truncation, verify this is a good way to clear file? (This is what I get for not using Java)

# This file handles any console output and OS Detection for PyPad.
# Also handles status labels in the GUI.

# Version Number
version_number = "0.2"

# Where are we?
def detect_os():
    return platform.system()

# Clears console based on OS function, again since Windows has to be different.
def clear_screen():
    if detect_os() == "Windows":
        system("cls")
    else:
        system("clear")

# Initializes console on program start.
def init():
    clear_screen()
    print(" *** PyPad Version: " + version_number + " ***")
    print("Running on: " + detect_os())
    print("Started at: " + time.ctime())

# print_user is for avoiding cyclic import (because Python sucks).

def print_user(x):
    print(x) 

def exit_():
    sys.exit(0)
    print("User has exited, closing....")



