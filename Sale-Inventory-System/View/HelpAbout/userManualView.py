import tkinter as tk
from tkinter import CENTER, font, ttk, messagebox
from Utils import Functions
from Utils import CustomDialog
class UserManualView(tk.Frame):
    def __init__(self, userManualController, master):
        self.master = master
        self.mainBg = "Gray89"
        super().__init__(self.master, background=self.mainBg)
        self.userManualController = userManualController
        self.pack(fill=tk.BOTH, expand=True)