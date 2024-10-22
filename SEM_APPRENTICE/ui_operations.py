"""
**SEM_APPRENTICE IS THE PROPERTY OF THE AUTHORS AND OWNERS OF SEM_APPRENTICE (ANUDHA MITTAL and DAVID CHOI) AND MAY NOT BE DISTRIBUTED, COPIED, SOLD, MODIFIED, OR USED WITHOUT THE EXPRESS CONSENT FROM THEM.**
**BY USING AND/OR POSSESSING SEM_APPRENTICE CODE, YOU ACKNOWLEDGE AND AGREE TO THESE TERMS.  © 2023 ANUDHA MITTAL and DAVID CHOI**
"""
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
