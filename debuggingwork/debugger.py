"""
Debugger: Comparing runtime between various logging methods

HERE ARE THE CANDIDATES:
justlog_v1 basicconfig w/ timestamp:  This is the original method, where you use the logging.basicConfig module to setup logging with builtin timestamp.  Then this generates a simple logging message.
Justlog_v1:  This method builds formatter class to allow you to extract the timestamp feature from the log message.  Then this generates a simple logging message.
Justlog_v2:  Uses basicConfig to generate log messages without timestamp.  This uses TimeStamp class to generate timestamp then adds to log message and concatenates the two to form the log message.

logplusfile_v1: This uses the formatter class to extract timestamp from original log message to use in filename.
logplusfile_v2:  This uses the TimeStamp class to generate timestamp to be used both in log message and filename.


HERE ARE THE RESULTS:
Ran justlog_v1 basicconfig w/ timestamp 100 times. Average time per run is: 0.0000649118423461914 secs
Ran justlog_v1 custom config 100 times. Average time per run is:            0.00005678653717041016 secs
Ran justlog_v2 100 times. Average time per run is:                          0.00005523443222045898 secs


Ran logplusfile_v1 1000 times. Average time per run is: 0.00007751989364624023 secs
Ran logplusfile_v2 1000 times. Average time per run is: 0.0000650632381439209 secs

"""

import time
import datetime as dt
import re
import logging
import os
from pathlib import Path
import numpy as np

def runtime_logger(num_runs, func_name, targetfunc, targetinputs):
    results = []
    for i in range(0, num_runs):
        start = time.time()
        '''INSERT FUNCTION TO TEST HERE'''
        targetfunc(targetinputs)
        '''TESTFUNCTION END'''
        end = time.time()
        elapsed = end-start
        results.append(elapsed)
        print(f'Run {i}: {elapsed} secs')
    print(f'Ran {func_name} {num_runs} times. Average time per run is: {np.mean(results)} secs')


samp_message = "I am learning :D"
num_runs = 1000
targetinputs = (samp_message)


if __name__ == '__main__':
    # load in common with all test subjects
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

    build_directories()

    class MyFormatter(logging.Formatter):
        def __init__(self, fmt=None, datefmt=None, style='%'):
            super().__init__(fmt=fmt, datefmt=datefmt, style=style)
            self.timestamp = None

        def format(self, record):
            self.timestamp = self.formatTime(record, self.datefmt)
            return super().format(record)
    
    formatter = MyFormatter(fmt='%(asctime)s: %(message)s')
    handler = logging.FileHandler(filename=PathOperations().create_path_string(FullPathElements.F1_LOGS + [FileNames().FN_LOG]), mode='a')
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # logging.basicConfig(filename=PathOperations().create_path_string(FullPathElements.F1_LOGS + [FileNames().FN_LOG]), level=logging.INFO, format='%(asctime)s: %(message)s', force =True)

    # logging.basicConfig(filename=PathOperations().create_path_string(FullPathElements.F1_LOGS + [FileNames().FN_LOG]), level=logging.INFO, format='%(message)s', force =True)

    class TimeStamp:

        def __init__(self):
            self.__dtobj = dt.datetime.now()
        
        @property
        def dtobject(self):
            return self.__dtobj

        @property
        def string(self):
            return str(self.__dtobj)

        @property
        def string_justnums(self):
            return re.sub(r'\.|\:|\-|\s', '', str(self.__dtobj))
    
    # def justlog_v1(message):
    #     logging.info(message)

    # def justlog_v2(message):
    #     # get timestamp
    #     t = TimeStamp()
    #     logging.info(f"{t.dtobject}: {message}")

    def logplusfile_v1(message):
        logging.info(message)
        timestamp_formatted = re.sub(r'\,|\:|\-|\s', '', formatter.timestamp)
        filename = f"{timestamp_formatted} {message}.png"
        # print(filename)

    def logplusfile_v2(message):
        t = TimeStamp()
        logging.info(f"{t.dtobject}: {message}")    
        filename = f"{t.string_justnums} {message}.png"
        # print(filename)

    runtime_logger(num_runs, 'logplusfile_v1', logplusfile_v1, targetinputs)
