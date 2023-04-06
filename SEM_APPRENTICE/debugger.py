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
import glob
from pathlib import Path
import numpy as np
from bmptopng_pil import bmp_to_png_pil
from bmptopng_cv2 import bmp_to_png_cv
from path_operations import PathOperations
from filesys_nomenclature import FullPathElements
import multiprocessing

def runtime_logger_generator(func_name, targetfunc):
    
    
    results = []
    i = 0
    for p in glob.glob(source):
        
        targetinputs = (p, p[:-4]+".png",)
        start = time.time()
        '''INSERT FUNCTION TO TEST HERE'''
        # pool.apply_async(targetfunc, targetinputs)
        targetfunc(*targetinputs)
        '''TESTFUNCTION END'''
        end = time.time()
        elapsed = end-start
        results.append(elapsed)
        print(f'Run {i}: {elapsed} secs')
        i += 1
    print(f'Ran {func_name} {num_runs} times. Average time per run is: {np.mean(results)} secs')

def runtime_logger(num_runs, func_name, targetfunc, targetinputs):
    results = []
    for i in range(0, num_runs):
        start = time.time()
        '''INSERT FUNCTION TO TEST HERE'''
        targetfunc(*targetinputs)
        '''TESTFUNCTION END'''
        end = time.time()
        elapsed = end-start
        results.append(elapsed)
        print(f'Run {i}: {elapsed} secs')
    print(f'Ran {func_name} {num_runs} times. Average time per run is: {np.mean(results)} secs')


num_runs = 306
# load in common with all test subjects
current_dir = os.path.dirname(os.path.abspath(__file__))
source = PathOperations().create_path_string(FullPathElements(current_dir).F1_SCREENSHOTS+['*.bmp'])



if __name__ == '__main__':
    runtime_logger_generator('bmp_to_png_cv', bmp_to_png_cv)

