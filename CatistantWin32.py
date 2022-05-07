import os
import subprocess
import sys
import time
import random
import pynput
import pyautogui

print("""   _____      _   _     _              _   
  / ____|    | | (_)   | |            | |  
 | |     __ _| |_ _ ___| |_ __ _ _ __ | |_ 
 | |    / _` | __| / __| __/ _` | '_ \| __|
 | |___| (_| | |_| \__ \ || (_| | | | | |_ 
  \_____\__,_|\__|_|___/\__\__,_|_| |_|\__|
                                           
                                           """)

def copen(item):
    if item.endswith(".exe"):
        subprocess.run(item.replace("open ", ""))

def rm(item):
    os.remove(item.replace("rm ", ""))

def rmdir(item):
    os.rmdir(item.replace("rmdir ", ""))

def cat(item):
    with open(item.replace("cat ", ""), "r") as file:
        print(file.read())

def pwd():
    print(os.getcwd())

def ls():
    for i in os.listdir():
        print(i)
    print("\n")

def cd(path):
    os.chdir(path.replace("cd ", ""))

def touch(item):
    open(item.replace("touch ",""), "x")

CMD = True

while CMD == True:
    i = input("~$ ")

    if i == "exit":
        CMD = False

    elif i.startswith("open "):
        copen(i)

    elif i.startswith("rm "):
        rm(i)

    elif i.startswith("rmdir "):
        rmdir(i)

    elif i.startswith("cat "):
        cat(i)

    elif i == "pwd":
        pwd()

    elif i == "ls":
        ls()

    elif i.startswith("cd "):
        cd(i)

    elif i.startswith("touch "):
        touch(i)
