from os import system
import platform

# This file handles any console output and OS Detection

version_number = "0.1"

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
    print("Starting...")

# print_user is for avoiding cyclic import

def print_user(x):
    print(x) 




