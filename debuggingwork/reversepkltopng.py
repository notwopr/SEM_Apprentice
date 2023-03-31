import os
import sys
import pickle as pkl
from pathlib import Path
from PIL import Image
import numpy as np

# Get the path to the directory where the executable is located
current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
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
    
    def savetopkl(self, filepath: str, filedata):
        with open(Path(filepath), "wb") as targetfile:
            pkl.dump(filedata, targetfile, protocol=4)

    def readpkl(self, path: str):
        with open(Path(path), "rb") as targetfile:
            data = pkl.load(targetfile)
        return data
    
filename = "20230330005540030637__RELEASED_h.pkl"
ss_path = PathOperations().create_path_string(FullPathElements.F1_SCREENSHOTS+[filename])
newfn = "20230330005540030637__RELEASED_h.png"
new_path = PathOperations().create_path_string(FullPathElements.F1_SCREENSHOTS+[newfn])
# save new file
def save_array_as_png(array, file_path):
    image = Image.fromarray(np.uint8(array))
    image.save(file_path)

targetarr = MachineOperations().readpkl(ss_path)
save_array_as_png(targetarr, new_path)