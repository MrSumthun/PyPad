from os import system
import sys
import time
import platform

# This file handles any console output and OS Detection
# Also handles status label

version_number = "0.2"

def detect_os():
    return platform.system()

def clear_screen():
    if detect_os() == "Windows":
        system("cls")
    else:
        system("clear")

def init():
    clear_screen()
    print(" *** PyPad Version: " + version_number + " ***")
    print("Running on: " + detect_os())
    print("Started at: " + time.ctime())

# print_user is for avoiding cyclic import

def print_user(x):
    print(x) 

def exit_():
    sys.exit(0)
    print("User has exited, closing....")



