import tkinter as tk
from window_design import Window

class UIOperations:
    def __init__(self, sem_apprentice, kbm_listener):
        self.root = tk.Tk()
        self.root.withdraw()
        self.sem_apprentice = sem_apprentice
        self.kbm_listener = kbm_listener

    def yesno(self, title, message):
        window = Window(title, message).window
        event, values = window.read()
        window.close()
        return event =='Yes'
