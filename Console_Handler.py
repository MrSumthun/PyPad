from os import system
from tqdm import tqdm
import time
import platform

# This file handles any console output and OS Detection
# Also handles status label

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
    for i in tqdm(range(100), colour='#2f4f4f'):          #This will be useful for file r/w
        time.sleep(0.001) 

# print_user is for avoiding cyclic import

def print_user(x):
    print(x) 

def exit_():
    print("User has exited, closing....")



