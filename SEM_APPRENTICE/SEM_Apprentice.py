"""
WELCOME TO SEM_APPRENTICE!

**SEM_APPRENTICE IS THE PROPERTY OF THE AUTHORS AND OWNERS OF SEM_APPRENTICE (ANUDHA MITTAL and DAVID CHOI) AND MAY NOT BE DISTRIBUTED, COPIED, SOLD, OR USED WITHOUT THE EXPRESS CONSENT FROM THEM.**
**BY USING AND/OR POSSESSING SEM_APPRENTICE CODE, YOU ACKNOWLEDGE AND AGREE TO THESE TERMS.  COPYRIGHT MARCH 15, 2023**

"""
# SYSTEM IMPORTS
import os
import re
import datetime as dt
from pathlib import Path
import logging
from tkinter import messagebox
import tkinter as tk
import pyautogui
from pynput import mouse
from pynput import keyboard
from win32gui import GetWindowDC, ReleaseDC, DeleteObject
from win32ui import CreateDCFromHandle, CreateBitmap
from win32con import SRCCOPY
from PIL import Image
import dxcam

# Get path to directory enclosing this script
current_dir = os.path.dirname(os.path.abspath(__file__))
resolution = pyautogui.size()

symbol_legend = {
    "Button.left": "leftbutton",
    "Button.right": "rightbutton",
    ".": "period",
    ",": "comma",
    ";": "semicolon",
    "#": "pound",
    "%": "percent",
    "&": "ampersand",
    "(": "leftparenthesis",
    ")": "rightparenthesis",
    "[": "leftbracket",
    "]": "rightbracket",
    "{": "leftbrace",
    "}": "rightbrace",
    "<": "leftchevron",
    ">": "rightchevron",
    "\\": "backslash",
    "*": "asterisk",
    "?": "question",
    "/": "forwardslash",
    " ": "space",
    "$": "dollar",
    "!": "exclamation",
    "'": "singlequote",
    "\"": "doublequote",
    ":": "colon",
    "@": "atsign",
    "+": "plus",
    "`": "backtick",
    "|": "pipe",
    "=": "equal",
    "~": "tilde",
    "^": "caret",
    "_": "underscore",
    "-": "minus",
    "<12>": "numpad_numlockoff_5",
    "<48>": "ctrl_0",
    "<49>": "ctrl_1",
    "<50>": "ctrl_2",
    "<51>": "ctrl_3",
    "<52>": "ctrl_4",
    "<53>": "ctrl_5",
    "<54>": "ctrl_6",
    "<55>": "ctrl_7",
    "<56>": "ctrl_8",
    "<57>": "ctrl_9",
    "\\x11": "ctrl_q",
    "\\x17": "ctrl_w",
    "\\x05": "ctrl_e",
    "\\x12": "ctrl_r",
    "\\x14": "ctrl_t",
    "\\x19": "ctrl_y",
    "\\x15": "ctrl_u",
    "\\t": "ctrl_i",
    "\\x0f": "ctrl_o",
    "\\x10": "ctrl_p",
    "\\x1b": "ctrl_leftbracket",
    "\\x1d": "ctrl_rightbracket",
    "\\x1c": "ctrl_backslash",
    "\\x01": "ctrl_a",
    "\\x13": "ctrl_s",
    "\\x04": "ctrl_d",
    "\\x06": "ctrl_f",
    "\\x07": "ctrl_g",
    "\\x08": "ctrl_h",
    "\\n": "ctrl_j",
    "\\x0b": "ctrl_k",
    "\\x0c": "ctrl_l",
    "<186>": "ctrl_;",
    "<222>": "ctrl_'",
    "\\x1a": "ctrl_z",
    "\\x18": "ctrl_x",
    "\\x03": "ctrl_c",
    "\\x16": "ctrl_v",
    "\\x02": "ctrl_b",
    "\\x0e": "ctrl_n",
    "\\r": "ctrl_m",
    "<188>": "ctrl_comma",
    "<190>": "ctrl_period",
    "<191>": "ctrl_forwardslash",
    "<96>": "numpad_numlockon_0",
    "<97>": "numpad_numlockon_1",
    "<98>": "numpad_numlockon_2",
    "<99>": "numpad_numlockon_3",
    "<100>": "numpad_numlockon_4",
    "<101>": "numpad_numlockon_5",
    "<102>": "numpad_numlockon_6",
    "<103>": "numpad_numlockon_7",
    "<104>": "numpad_numlockon_8",
    "<105>": "numpad_numlockon_9",
    "<106>": "numpad_ctrl_asterisk",
    "<107>": "numpad_ctrl_plus",
    "<109>": "numpad_ctrl_minus",
    "<110>": "numpad_numlockon_period",
    "<111>": "numpad_ctrl_forwardslash",
    "<187>": "ctrl_equal",
    "<189>": "ctrl_minus",
    "<192>": "ctrl_backtick",
}

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

class TimeStamp:

    def __init__(self):
        self.__dtobj = dt.datetime.now()
    
    @property
    def dtobject(self):
        return self.__dtobj

    @property
    def string_justnums(self):
        return re.sub(r'\.|\:|\-|\s', '', str(self.__dtobj))

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
    """given keystroke return its name"""
    char = None
    vk = None
    neither = key
    symbol = None
    if hasattr(key, 'char'):
        # print('char found')
        char = key.char
    if hasattr(key, 'vk'):
        # print('vk found')
        vk = key.vk

    if char is None and vk is None:
        symbol = str(key)[4:]
        if symbol.endswith('_r'):
            symbol = f"right{symbol[:-2]}"
        elif symbol.endswith('_l'):
            symbol = f"left{symbol[:-2]}"
        elif symbol == 'shift':
            symbol = f"left{symbol}"
    elif char is None and vk is not None:
        # some keys in numpad satisfy this condition
        symbol = str(neither)
    elif char:
        symbol = char
    
    # pressing ctrl plus any of keys in the alphabet rows except the functional keys (enter, shift tab, etc.) 
    if str(neither).startswith("'\\"):
        symbol = str(neither)[1:-1]

    # print(f"vk: {vk} char: {char} neither: {neither}")

    final_symbol = symbol_legend.get(symbol, symbol)
    # print(f"final symbol: {final_symbol}")
    return final_symbol

def gen_log_msg(message):
    t = TimeStamp()
    logging.info(f"{t.dtobject}: {message}")

def win32_snap_save(path_to_img):
    w = resolution[0] # set this
    h = resolution[1] # set this

    hwnd = None #win32gui.FindWindow(None, windowname)

    # get image data and save to bmp
    wDC = GetWindowDC(hwnd)
    dcObj=CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), SRCCOPY)

    # save to bitmap
    dataBitMap.SaveBitmapFile(cDC, path_to_img)

    # save to png
    # bmpstr = dataBitMap.GetBitmapBits(True)
    # img = Image.frombuffer(
    #     'RGB',
    #     (w,h),
    #     bmpstr, 'raw', 'BGRX', 0, 1)
    # img.save(path_to_img)
  
    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    ReleaseDC(hwnd, wDC)
    DeleteObject(dataBitMap.GetHandle())

def dxcam_snap_save(path_to_img):
    screenshot = camera.grab()
    if screenshot is not None:
        # Convert the numpy array to a Pillow image object
        image = Image.fromarray(screenshot)
        # Save the image as a PNG file to disk
        image.save(path_to_img)

def snap_and_save(signal, detail, mode):
    # compose log message
    match mode:
        case 'keyboard':
            message = f'{signal.upper()} {get_key_symbol(detail)}'
            message_fileversion = f'{signal.upper()}_{get_key_symbol(detail)}'
        case 'mouse':
            message = f"{signal.upper()} ({detail[0]}, {detail[1]}) with {detail[2]}"
            message_fileversion = f"{signal.upper()}_x{detail[0]}_y{detail[1]}_{detail[2]}"

    # log message
    t = TimeStamp()
    logging.info(f"{t.dtobject}: {message}")

    # format filename
    filename = f"{t.string_justnums}__{message_fileversion}.png"
    ss_path = PathOperations().create_path_string(FullPathElements.F1_SCREENSHOTS+[filename])
    dxcam_snap_save(ss_path)
    # win32_snap_save(ss_path)

def on_press(key):
    global lock
    # if listener not suspended...
    if not lock:
        # print('press') 
        snap_and_save('pressed', key, 'keyboard')

def on_release(key):
    global lock
    # if listener not suspended...
    if not lock: 
        # print('release') 
        snap_and_save('released', key, 'keyboard')

def on_move(x, y):
    global lock
    # if listener not suspended...
    if not lock:
        # print('moved')
        gen_log_msg(f"moved ({x}, {y})")  # coordinates are what mouse moved TO (according to pynput docs)

def on_click(x, y, button, pressed):
    global lock
    # if listener not suspended...
    if not lock:
        if pressed:
            # print(f'clicked')  
            snap_and_save('clicked', [x, y, symbol_legend.get(str(button), button)], 'mouse')
        else:
            # print(f'unclicked') 
            snap_and_save('unclicked', [x, y, symbol_legend.get(str(button), button)], 'mouse')

def on_scroll(x, y, dx, dy):
    global lock
    # if listener not suspended...
    if not lock:
        # print('scroll')
        gen_log_msg(f"scrolled ({x}, {y}) ({dx}, {dy})")

        # If user moves mouse to upperleft corner and scrolls
        if x<2 and y<2:
            # suspend all listener activity
            lock = True 
            # Display confirmation box
            stop_record = UIOperations().yesno('STOP RECORDING?', 'Hi! Would you like to stop recording?')
            if stop_record:
                return False
            # if chose 'No', then resume listening
            lock = False  


# Set constants
start_message = "I am learning :D"
end_message = "I stopped learning. Please come back soon :_)"

"""EXECUTABLES BELOW"""
# Check Directories if present, if not, create them
build_directories()

# Activate Logger (using the custom Formatter to later store created log message to variable)
logging.basicConfig(filename=PathOperations().create_path_string(FullPathElements.F1_LOGS + [FileNames().FN_LOG]), level=logging.INFO, format='%(message)s', force =True)

# Suspend listener
lock = True

# turn on dxcam 
camera = dxcam.create()

# Activate Listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as k_listener, mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as m_listener:

    # Get User Confirmation to Begin Recording
    start_record = UIOperations().yesno('START RECORDING?', 'Hello!  Should I start recording?')

    # If user confirms to begin recording...
    if start_record:

        # Resume listening
        lock = False
        # Log start of session
        gen_log_msg(start_message)
        print(start_message)
        m_listener.join()
        # Log end of session
        gen_log_msg(end_message)
        print(end_message)
        exit()  # must exit because keyboard listener is still active
    else:
        exit()
