"""
WELCOME TO SEM_APPRENTICE!

**SEM_APPRENTICE IS THE PROPERTY OF THE AUTHORS AND OWNERS OF SEM_APPRENTICE (ANUDHA MITTAL and DAVID CHOI) AND MAY NOT BE DISTRIBUTED, COPIED, SOLD, OR USED WITHOUT THE EXPRESS CONSENT FROM THEM.**
**BY USING AND/OR POSSESSING SEM_APPRENTICE CODE, YOU ACKNOWLEDGE AND AGREE TO THESE TERMS.  COPYRIGHT MARCH 15, 2023**

"""
# SYSTEM IMPORTS
import os
import re
from pathlib import Path
import logging
from tkinter import messagebox
import tkinter as tk
import pyautogui
import d3dshot
import dxcam
import cv2
import numpy as np
from pynput import mouse
from pynput import keyboard


# get the current directory path
#__file__= r'C:\Users\...'
# username = os.getlogin()

# a = r'C:\Users'
# b = r'Documents'
# __file__= a + '\\'+ username +'\\' +b

# Get path to directory enclosing this script
current_dir = os.path.dirname(os.path.abspath(__file__))

class DirNames:
    DN_DATA_PARENT = 'SEMBOT_DATA'
    DN_LOGS = 'LOGS'
    DN_SCREENSHOTS = 'SCREENSHOTS'

class FileNames:
    FN_LOG = 'kbm_log.txt'

class FullPathElements:
    F0_DATA_PARENT = [current_dir, DirNames.DN_DATA_PARENT]
    F1_LOGS = F0_DATA_PARENT + [DirNames.DN_LOGS]
    F1_SCREENSHOTS = F0_DATA_PARENT + [DirNames.DN_SCREENSHOTS]

class PathOperations:
    # create pathstring from list of path elements
    def create_path_string(self, list_of_path_elements):
        if all(map(lambda x: isinstance(x, str), list_of_path_elements)):
            return '/'.join(list_of_path_elements)
        else:
            raise ValueError("All pathnames must be strings.")
    
class MachineOperations:

    def check_if_directory_is_directory(self, path_to_dir: str):
        return os.path.isdir(Path(path_to_dir))

    def create_nonexistent_directory(self, path_to_dir: str):
        '''# CREATE DIRECTORY IF DOESN'T EXIST'''

        print('\n')
        print(f'Checking whether directory {path_to_dir} exists...')

        if not self.check_if_directory_is_directory(path_to_dir):
            print(f"Directory {path_to_dir} does not exist.")
            os.makedirs(Path(path_to_dir))
            print("Directory created.")
        else:
            print(f"Directory {path_to_dir} already exists.")


class UIOperations:
    def yesno(self, title, question):
        """Gives a Yes/No popup dialog box that stays on top of everything else on the screen always and doesn't close until you click yes or no"""
        root = tk.Tk()
        root.withdraw()
        root.focus_set() # Set the messagebox as the top window
        root.attributes('-topmost', True)  # keep window on top of others
        response = messagebox.askyesno(title, question)
        root.destroy()  # destroy the root window
        return response

# Create a custom Formatter that captures the entire log message in a variable
class MyFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%'):
        super().__init__(fmt=fmt, datefmt=datefmt, style=style)
        self.timestamp = None

    def format(self, record):
        self.timestamp = self.formatTime(record, self.datefmt)
        return super().format(record)
    

def build_directories():
    
    # get sorted list of all SEMBot Directories to build
    f = FullPathElements()
    alldirs = [attr for attr in dir(f) 
              if not attr.startswith('__')]
    alldirs.sort()
    print("\n")
    print("Checking existence of the following directories...")
    print(alldirs)

    # create each directory from root level up.
    for d in alldirs:
        pathstring = PathOperations().create_path_string(getattr(f, d))
        MachineOperations().create_nonexistent_directory(pathstring)

def get_key_symbol(key):
    """given key, determines the name of that key, regardless whether it has .char, .vk or neither attribute"""
    if hasattr(key, 'vk') and 96 <= key.vk <= 105:
        return key.vk - 96
    if hasattr(key, 'char'):
        return key.char
    else:
        return key

def snap_and_save(signal, detail, mode):
    # compose log message
    match mode:
        case 'keyboard':
            message = f'{signal} {get_key_symbol(detail)}'
        case 'mouse':
            message = f"{signal} {detail}"

    # log message
    logging.info(message)

    # format filename
    raw_timestamp = formatter.timestamp
    timestamp_formatted = re.sub(r'\,|\:|\-|\s', '', raw_timestamp)
    filename = f"{timestamp_formatted} {message}.png"

    # takes snapshot and save image to disk with that filename
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)  #why do I need this step # also can I save just the template # can I save only the program window, not the entire screenshot
    ss_path = PathOperations().create_path_string(FullPathElements.F1_SCREENSHOTS+[filename])
    cv2.imwrite(ss_path, image)

def on_press(key):
    global lock
    if not lock: 
        # if lock is True, that means Stop Recording? prompt is open, so do not log until prompt closes
        snap_and_save('pressed', key, 'keyboard')

def on_release(key):
    global lock
    if not lock: 
        # if lock is True, that means Stop Recording? prompt is open, so do not log until prompt closes
        snap_and_save('released', key, 'keyboard')

def on_move(x, y):
    global lock   
    if not lock:  
        # if lock is True, that means Stop Recording? prompt is open, so do not log until prompt closes
        logging.info(f"moved ({x}, {y})")  # coordinates are what mouse moved TO (according to pynput docs)

def on_click(x, y, button, pressed):
    global lock   
    if not lock and pressed:  
        # if lock is True, that means Stop Recording? prompt is open, so do not log until prompt closes
        snap_and_save('clicked', f'({x}, {y}) {button}', 'mouse')

def on_scroll(x, y, dx, dy):
    global lock
    if not lock: 
        # if lock is True, that means Stop Recording? prompt is open, so do not log until prompt closes
        logging.info(f"scrolled ({x}, {y})({dx}, {dy})")

    # If User is finished recording, user moves mouse to upperleft corner and scrolls
    if x<2 and y<2 and not lock:
    # if lock is False, set to True and display message, suspend Listener
        lock = True
        # Display confirmation box
        stop_record = UIOperations().yesno('STOP RECORDING?', 'Are you sure you want to stop recording?')
        if stop_record:
            return False
        lock = False  # if chose 'No', then change lock to False and continue logging


# Set constants

start_message = "SEM Apprentice activated!"
end_message = "SEM Apprentice terminated."

"""EXECUTABLES BELOW"""
# Check Directories if present, if not, create them
build_directories()

# Activate Logger (using the custom Formatter to later store created log message to variable)
# mode 'a' means append new log messages; mode 'w' means 'write' rather rewrite new log messages (previous messages are overwritten)
formatter = MyFormatter(fmt='%(asctime)s: %(message)s')
path_to_logfile = PathOperations().create_path_string(FullPathElements.F1_LOGS + [FileNames().FN_LOG])
handler = logging.FileHandler(filename=path_to_logfile, mode='a')
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Suspend logging
lock = True

# Activate Listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as k_listener, \
    mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as m_listener:

    # Get User Confirmation to Begin Recording
    start_record = UIOperations().yesno('START RECORDING?', 'Hello!  Should I start recording?')

    # If user confirms to begin recording...
    if start_record:

        # Resume logging
        lock = False

        # Log start of session
        logging.info(start_message)
        print(start_message)

        # Quit SEM Apprentice
        m_listener.join()
        logging.info(end_message)
        print(end_message)
        exit()  # must exit because keyboard listener is still active
    else:
        exit()
