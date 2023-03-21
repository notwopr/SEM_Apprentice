"""
WELCOME TO SEM_APPRENTICE!
**SEM_APPRENTICE IS THE PROPERTY OF THE AUTHORS AND OWNERS OF SEM_APPRENTICE (ANUDHA MITTAL and DAVID CHOI) AND MAY NOT BE DISTRIBUTED, COPIED, SOLD, OR USED WITHOUT THE EXPRESS CONSENT FROM THEM.**
**BY USING AND/OR POSSESSING SEM_APPRENTICE CODE, YOU ACKNOWLEDGE AND AGREE TO THESE TERMS.  COPYRIGHT MARCH 15, 2023**
"""
# SYSTEM IMPORTS
import os
from pathlib import Path
import logging
from tkinter import messagebox
import tkinter as tk
import pyautogui
import cv2
import numpy as np
from pynput.mouse import Listener
from pynput import keyboard


# get the current directory path
#__file__= r'C:\Users\...'
username = os.getlogin()

a = r'C:\Users'
b = r'Documents'
__file__= a + '\\'+ username +'\\' +b

current_dir = os.path.dirname(os.path.abspath(__file__))


"""DO NOT MODIFY CODE BELOW THIS LINE"""
"""DO NOT MODIFY CODE BELOW THIS LINE"""
"""DO NOT MODIFY CODE BELOW THIS LINE"""


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
    
    # create one pathstring from list of path elements with '/' or '\' as separator
    def create_path_string_custom(self, list_of_path_elements, separator_type):
        if all(map(lambda x: isinstance(x, str), list_of_path_elements)):
            return separator_type.join(list_of_path_elements)
        else:
            raise ValueError("All pathnames must be strings.")
    
    # create pathstring from list of path elements but gets separator_type from machine_settings
    def create_path_string(self, list_of_path_elements):
        return self.create_path_string_custom(list_of_path_elements, '/')
    

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




# global variable to prevent multiple message boxes from being displayed at once
lock = False  

def on_press(key):
    try:
        #print('alphanumeric key {0} pressed'.format(
            #key.char))
        logging.info('alphanumeric key {0} pressed'.format(key.char))


        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)  #why do I need this step # also can I save just the template # can I save only the program window, not the entire screenshot
        ss_uncropped_filename = f"Key {key}.png"
        path_ss_uncropped = PathOperations().create_path_string(FullPathElements.F1_SCREENSHOTS+[ss_uncropped_filename])
        cv2.imwrite(path_ss_uncropped, image)

    except AttributeError:
        #print('special key {0} pressed'.format(key))
        pass

def on_release(key):
    #print('{0} released'.format(
    #    key))
    logging.info('{0} released'.format(key))

    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)  #why do I need this step # also can I save just the template # can I save only the program window, not the entire screenshot
    ss_uncropped_filename = f"Key {key} released.png"
    path_ss_uncropped = PathOperations().create_path_string(FullPathElements.F1_SCREENSHOTS+[ss_uncropped_filename])
    cv2.imwrite(path_ss_uncropped, image)

    if key == keyboard.Key.esc:
        # Stop listener
        return False

def on_move(x, y):
    logging.info(f"Mouse moved to ({x}, {y})")

def on_click(x, y, button, pressed):
    if pressed:
        logging.info(f"Mouse clicked at ({x}, {y}) with {button}")

        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)  #why do I need this step # also can I save just the template # can I save only the program window, not the entire screenshot
        ss_uncropped_filename = f"Mouse clicked at ({x}, {y}) with {button}.png"
        path_ss_uncropped = PathOperations().create_path_string(FullPathElements.F1_SCREENSHOTS+[ss_uncropped_filename])
        cv2.imwrite(path_ss_uncropped, image)

def on_scroll(x, y, dx, dy):

    logging.info(f"Mouse scrolled at ({x}, {y})({dx}, {dy})")

    # If User is finished recording, user moves mouse to upperleft corner and scrolls
    if x<2 and y<2:

        global lock   
        if not lock:  # if lock is False, set to True and display message to suspend Listener
            lock = True
            
            # c. Display confirmation box
            root = tk.Tk()
            root.withdraw()
            root.focus_set() # Set the messagebox as the top window
            root.attributes('-topmost', True)  # keep window on top of others
            stop_record = messagebox.askyesno('STOP RECORDING?', 'Hi!  Should I stop recording?')
            root.destroy() # destroy the root window

            if stop_record:
                return False
            lock = False  # lock is True, don't display message box


# 1. Get User Confirmation to Begin Recording
root = tk.Tk()
root.withdraw()
root.focus_set() # Set the messagebox as the top window
root.attributes('-topmost', True)  # keep window on top of others
start_record = messagebox.askyesno('START RECORDING?', 'Hello!  Should I start recording?')
root.destroy()  # destroy the root window

# If user confirms to begin recording...
if start_record:

    # 2. Check Directories if present, if not, create them
    build_directories()

    # 3. Activate Logger
    path_to_logfile = PathOperations().create_path_string(FullPathElements.F1_LOGS + [FileNames().FN_LOG])
    logging.basicConfig(filename=path_to_logfile, level=logging.DEBUG, format='%(asctime)s: %(message)s', force =True)

    # 4. Activate Listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()

else:
    exit()