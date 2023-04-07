

class DirNames:
    DN_DATA_PARENT = 'SEMAPPRENTICE_DATA'
    DN_LOGS = 'LOGS'
    DN_SCREENSHOTS = 'SCREENSHOTS'

class FileNames:
    FN_LOG = 'kbm_log.txt'

class FullPathElements:
    def __init__(self, current_dir):
        self.F0_DATA_PARENT = [current_dir, DirNames.DN_DATA_PARENT]
        self.F1_LOGS = self.F0_DATA_PARENT + [DirNames.DN_LOGS]
        self.F1_SCREENSHOTS = self.F0_DATA_PARENT + [DirNames.DN_SCREENSHOTS]
