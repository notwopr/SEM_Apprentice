"""
WELCOME TO SEM_APPRENTICE!

**SEM_APPRENTICE IS THE PROPERTY OF THE AUTHORS AND OWNERS OF SEM_APPRENTICE (ANUDHA MITTAL and DAVID CHOI) AND MAY NOT BE DISTRIBUTED, COPIED, SOLD, OR USED WITHOUT THE EXPRESS CONSENT FROM THEM.**
**BY USING AND/OR POSSESSING SEM_APPRENTICE CODE, YOU ACKNOWLEDGE AND AGREE TO THESE TERMS.  © 2023 ANUDHA MITTAL and DAVID CHOI**

"""
import os
import sys
import logging
import ctypes
import tkinter as tk
import time
import datetime as dt
import re
# LOCAL IMPORTS
from path_operations import PathOperations
from filesys_nomenclature import FileNames, FullPathElements
from keyboard_mapping import KeyBoardMapping
from snapshot_methods import SnapShotMethods
from kbm_listener import KBMListener
from ui_operations import UIOperations
from machine_operations import MachineOperations
from window_design import Welcome, Status

class SEM_Apprentice:

    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.yesno_window_open = False      
        self.listener = KBMListener(self)
        self.ui = UIOperations(self, self.listener)
        self.kbm_mapper = KeyBoardMapping()
        # Get the path to the directory where the executable is located
        self.current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        # Get Screen Resolution
        self.user32 = ctypes.windll.user32
        self.screen_width = self.user32.GetSystemMetrics(0)
        self.screen_height = self.user32.GetSystemMetrics(1)
        # Load snap shot resources
        self.snapshot = SnapShotMethods(self.screen_width, self.screen_height)
        # Set Message Constants
        self.start_message = "I am learning :D"
        self.end_message = "I stopped learning. Please come back soon :_)"
        self.abort_message = "I understand. There is always next time :)"
        self.copyright_block = [
            "SEM_APPRENTICE",
            "VERSION: 2.3.0.0",
            "WELCOME TO SEM_APPRENTICE!",
            "** SEM_APPRENTICE IS THE PROPERTY OF THE AUTHORS AND OWNERS OF SEM_APPRENTICE (ANUDHA MITTAL and DAVID CHOI) AND MAY NOT BE DISTRIBUTED, COPIED, SOLD, OR USED WITHOUT THE EXPRESS CONSENT FROM THEM.", 
            "** BY USING AND/OR POSSESSING SEM_APPRENTICE CODE, YOU ACKNOWLEDGE AND AGREE TO THESE TERMS.", 
            "© 2023 ANUDHA MITTAL and DAVID CHOI.  ALL RIGHTS RESERVED."
            ]

    def confirm_start_recording(self):
        start_record = self.ui.yesno("SEM Apprentice", 'Hello!  I am SEM Apprentice.\nDo you want me to start recording?')
        if not start_record:
            # notify user of end
            abort_window = Status(self.abort_message, self.current_dir).window
            abort_window.read()
            sys.exit()

    def start_recording(self):
        
        # Activate Logger
        logging.basicConfig(filename=PathOperations().create_path_string(FullPathElements(self.current_dir).F1_LOGS + [FileNames().FN_LOG]), level=logging.INFO, format='%(message)s', force=True)

        # memorialize start
        self.gen_log_msg(self.start_message)
        
        start_window = Status(self.start_message, self.current_dir).window
        start_window.read()
        
        # start listeners
        self.listener.start()
        # listen for when listener is paused
        while True:
            if self.listener.listener_pause:
                stop_record = self.ui.yesno("SEM Apprentice", 'Hi! Would you like to stop recording?')
                if stop_record:
                    # memorialize end
                    self.gen_log_msg(self.end_message)
                    
                    end_window = Status(self.end_message, self.current_dir).window
                    end_window.read()
                    sys.exit()
                self.listener.listener_pause = False

    def prepare(self):
        # display title info and copyright
        for b in self.copyright_block:
            print(b)
            time.sleep(0.02)

        # build directories if not present
        MachineOperations().build_directories(self.current_dir)

    def run(self):
        # Save a reference to the original stdout
        original_stdout = sys.stdout
        welcome_window = Welcome(self.current_dir).window
        self.prepare()
        time.sleep(1)
        welcome_window.close()
        # Reset stdout to the original value
        sys.stdout = original_stdout
        self.confirm_start_recording()
        self.start_recording()

    def gen_log_msg(self, message):
        t = dt.datetime.now()
        logging.info(f"{t}: {message}")
        return re.sub(r'\.|\:|\-|\s', '', str(t))
    
    def snap_and_save(self, signal, detail, mode):
        # compose log message
        match mode:
            case 'keyboard':
                message = f'{signal} {self.kbm_mapper.get_key_symbol(detail)}'
                message_fileversion = f'{signal.upper()}_{self.kbm_mapper.get_key_symbol(detail)}'
            case 'mouse':
                button = self.kbm_mapper.key_legend.get(str(detail[2]), detail[2])
                message = f"{signal} ({detail[0]}, {detail[1]}) with {button}"
                message_fileversion = f"{signal.upper()}_x{detail[0]}_y{detail[1]}_{button}"

        # log message
        ts_string = self.gen_log_msg(message)

        # format filename
        filename = f"{ts_string}__{message_fileversion}.png"
        ss_path = PathOperations().create_path_string(FullPathElements(self.current_dir).F1_SCREENSHOTS+[filename])

        # save to disk
        self.snapshot.win32_snap_save(ss_path)

if __name__ == '__main__':
    app = SEM_Apprentice()
    app.run()