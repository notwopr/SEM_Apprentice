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
import queue
from multiprocessing import Manager, Process, freeze_support
# LOCAL IMPORTS
from path_operations import PathOperations
from filesys_nomenclature import FileNames, FullPathElements
from keyboard_mapping import KeyBoardMapping
from snapshot_methods import SnapShotMethods
from kbm_listener import KBMListener
from ui_operations import UIOperations
from machine_operations import MachineOperations
from window_design import Welcome, Status
from bmptopng_cv2 import check_queue_for_bmp

class SEM_Apprentice:

    def __init__(self):
        self.root = tk.Tk()
        self.pause_queue = queue.Queue()
        self.listener = KBMListener(self)
        self.ui = UIOperations(self, self.listener)
        # logging
        self.kbm_mapper = KeyBoardMapping()
        # Get the path to the directory where the executable is located
        self.current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        # Get Screen Resolution
        self.user32 = ctypes.windll.user32
        self.screen_width = self.user32.GetSystemMetrics(0)
        self.screen_height = self.user32.GetSystemMetrics(1)
        # Load snap shot resources
        self.snapshot = SnapShotMethods(self.screen_width, self.screen_height)
        # Initialize a queue to manage the conversion process
        self.convert_queue = Manager().Queue()
        # Start the conversion process in a separate process
        self.convert_processor = Process(target=check_queue_for_bmp, args=(self.convert_queue,))
        # Set Message Constants
        self.start_message = "I am learning :D"
        self.end_message = "I stopped learning. Please come back soon :_)"
        self.abort_message = "I understand. There is always next time :)"
        self.copyright_block = [
            "SEM_APPRENTICE",
            "VERSION: 0.4.0",
            "WELCOME TO SEM_APPRENTICE!",
            "** SEM_APPRENTICE IS THE PROPERTY OF THE AUTHORS AND OWNERS OF SEM_APPRENTICE (ANUDHA MITTAL and DAVID CHOI) AND MAY NOT BE DISTRIBUTED, COPIED, SOLD, OR USED WITHOUT THE EXPRESS CONSENT FROM THEM.", 
            "** BY USING AND/OR POSSESSING SEM_APPRENTICE CODE, YOU ACKNOWLEDGE AND AGREE TO THESE TERMS.", 
            "© 2023 ANUDHA MITTAL and DAVID CHOI.  ALL RIGHTS RESERVED."
            ]

    def confirm_start_recording(self):
        start_record = self.ui.yesno("SEM Apprentice", 'Do you want me to start recording?')
        if not start_record:
            # notify user of end
            abort_window = Status(self.abort_message).window
            abort_window.read()
            sys.exit()

    def confirm_stop_recording(self):
        # if listener_pause is True
        stop_record = self.ui.yesno("SEM Apprentice", 'Hi, again! Would you like to stop recording?')
        if stop_record:
            # memorialize end
            self.gen_log_msg(self.end_message)
            end_window = Status(self.end_message).window
            end_window.read()
            self.convert_queue.put("STOP RECORDING")
            self.convert_processor.join()
            sys.exit()
        self.listener.listener_pause = False

    def start_recording(self):

        # Activate Logger
        logging.basicConfig(filename=PathOperations().create_path_string(FullPathElements(self.current_dir).F1_LOGS + [FileNames().FN_LOG]), level=logging.INFO, format='%(message)s', force=True)

        # memorialize start
        self.gen_log_msg(self.start_message)
        start_window = Status(self.start_message).window
        start_window.read()
        
        # start convert processor
        self.convert_processor.start()

        # start kbm listeners
        self.listener.start()

        while True:
            try:
                # Wait for message in queue
                message = self.pause_queue.get(timeout=0.1)
            except queue.Empty:
                pass
            else:
                # If message is "stop", run confirm_stop_recording function
                if message == "pause":
                    self.confirm_stop_recording()
                
                # Mark task as done
                self.pause_queue.task_done()
                
    def prepare(self):
        MachineOperations().build_directories(self.current_dir)

    def splash_welcome(self):
        # Save a reference to the original stdout - this is so that stdout can return to console window
        original_stdout = sys.stdout
        welcome_window = Welcome(self.copyright_block).window
        self.prepare()
        time.sleep(3)
        welcome_window.close()
        # Reset stdout to the original value - this is so that stdout can return to console window
        sys.stdout = original_stdout

    def run(self):
        self.splash_welcome()
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
        filename = f"{ts_string}__{message_fileversion}.bmp"
        ss_path = PathOperations().create_path_string(FullPathElements(self.current_dir).F1_SCREENSHOTS+[filename])

        # save to disk
        self.snapshot.win32_snap_save(ss_path)

        # Add the BMP filepath to the queue for conversion
        self.convert_queue.put(ss_path)

if __name__ == '__main__':
    # this is needed because otherwise running the compiled EXE version causes it to open an infinite number of copies of SEM Apprentice crashing the program.
    freeze_support()

    app = SEM_Apprentice()

    # code to make sure icon file is packaged inside EXE file and call from inside the EXE instead of looking for it outside.
    datafile = f'{app.current_dir}\mikey.ico'
    if not hasattr(sys, "frozen"):
        datafile = os.path.join(os.path.dirname(__file__), datafile)
    else:
        datafile = os.path.join(sys.prefix, datafile)
    def resource_path(relative_path):    
        try:       
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    app.root.iconbitmap(default=resource_path(datafile))
    app.root.iconify()
    
    # run SEM Apprentice
    app.run()