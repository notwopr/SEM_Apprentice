"""
**SEM_APPRENTICE IS THE PROPERTY OF THE AUTHORS AND OWNERS OF SEM_APPRENTICE (ANUDHA MITTAL and DAVID CHOI) AND MAY NOT BE DISTRIBUTED, COPIED, SOLD, MODIFIED, OR USED WITHOUT THE EXPRESS CONSENT FROM THEM.**
**BY USING AND/OR POSSESSING SEM_APPRENTICE CODE, YOU ACKNOWLEDGE AND AGREE TO THESE TERMS.  © 2023 ANUDHA MITTAL and DAVID CHOI**
"""
import os
from pathlib import Path
import time
from filesys_nomenclature import FullPathElements
from path_operations import PathOperations

pace_of_messaging = 0.05

class MachineOperations:

    def check_if_directory_is_directory(self, path_to_dir: str):
        return os.path.isdir(Path(path_to_dir))

    def create_nonexistent_directory(self, path_to_dir: str):
        '''# CREATE DIRECTORY IF DOESN'T EXIST'''

        print('\n')
        print(f'Checking whether directory {path_to_dir} exists...')
        time.sleep(pace_of_messaging)

        if not self.check_if_directory_is_directory(path_to_dir):
            print(f"Directory {path_to_dir} does not exist.")
            time.sleep(pace_of_messaging)
            os.makedirs(Path(path_to_dir))
            print("Directory created.")
            time.sleep(pace_of_messaging)
        else:
            print(f"Directory {path_to_dir} already exists.")
            time.sleep(pace_of_messaging)
    
    def build_directories(self, current_dir):
    
        # get sorted list of all SEM Apprentice Directories to build
        f = FullPathElements(current_dir)
        alldirs = [attr for attr in dir(f) 
                if not attr.startswith('__')]
        alldirs.sort()
        print("\n")
        print("Checking existence of the following directories...")
        time.sleep(pace_of_messaging)
        print(alldirs)
        time.sleep(pace_of_messaging)

        # create each directory from root level up.
        for d in alldirs:
            pathstring = PathOperations().create_path_string(getattr(f, d))
            MachineOperations().create_nonexistent_directory(pathstring)