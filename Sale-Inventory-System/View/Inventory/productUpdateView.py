from tkinter import font, messagebox
from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry
from Utils import Functions
class ProductUpdateView(tk.Toplevel):
    def __init__(self,managerController,productUpdateController):
        self.mC = managerController
        self.productUpdateController = productUpdateController
        super().__init__(background="Gray89")
        self._window_attributes()
        self.mainBg = "Gray89"

    def main(self):
        pass
    
    def _window_attributes(self):
        self.h = 420
        self.w = 580
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

    

        
        self.title('Update Recipe')
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.quit())