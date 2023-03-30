import os
import sys
import datetime as dt
import numpy as np
class DirNames:
    DN_DATA_PARENT = 'SEMBOT_DATA'
    DN_LOGS = 'LOGS'
    DN_SCREENSHOTS = 'SCREENSHOTS'
class FileNames:
    FN_LOG = 'kbm_log.txt'
# Get the path to the directory where the executable is located
current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

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
with open(PathOperations().create_path_string(FullPathElements.F1_LOGS + [FileNames().FN_LOG]), 'r') as file:
    file_contents = file.read()


length_of_timestamp = 26

# split the file contents by the newline character
lines = file_contents.split('\n')

# collect all timestamps where keys were pressed or released
all_options = {
    'both': [dt.datetime.strptime(line[:26], "%Y-%m-%d %H:%M:%S.%f") for line in lines if (line.find("PRESSED")>=0 or line.find("RELEASED")>=0)],
    'pressonly': [dt.datetime.strptime(line[:26], "%Y-%m-%d %H:%M:%S.%f") for line in lines if (line.find("PRESSED")>=0)],
    "releaseonly": [dt.datetime.strptime(line[:26], "%Y-%m-%d %H:%M:%S.%f") for line in lines if (line.find("RELEASED")>=0)]
}
for k, allts in all_options.items():
    # get time differences in milliseconds
    alldiffs = []
    for i in range(1, len(allts)):
        alldiffs.append((allts[i]-allts[i-1]).microseconds/1000)
    # print(alldiffs)
    # get avg diff
    print(f"RESULTS FOR {k}: avg: {np.mean(alldiffs)} ms, min: {np.min(alldiffs)} ms, number of samples {len(allts)}")
    # fps = 240
    # fps1 = 30
    # fps2 = 60
    # print(f"{fps} fps=> {(1/fps)*1000} ms for each frame")
    # print(f"{fps1} fps=> {(1/fps1)*1000} ms for each frame")
    # print(f"{fps2} fps=> {(1/fps2)*1000} ms for each frame")