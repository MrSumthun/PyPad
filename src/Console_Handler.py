from os import system
import sys
import time
import platform
from src.File_Worker import log_event, delete_log
from colorama import Fore, Style

 
# This file handles any console output and OS Detection for PyPad.
# Also handles status labels in the GUI.

# Version Number
version_number = "0.2"

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
def init():
    delete_log()
    clear_screen()

    print(Fore.GREEN + " *** PyPad Version: " + version_number + " ***")
    print(Style.RESET_ALL)

    log_event("Program Started - Version: " + version_number)
    log_event("Detected OS: " + detect_os())

def exit_():
    log_event("Program Exited by User at: " + time.ctime())
    print(Fore.RED + " *** Exiting PyPad... ***")
    sys.exit(0)




