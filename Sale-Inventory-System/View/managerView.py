from tkinter import *
import tkinter as tk
class ManagerDashboard(tk.Frame):
    def __init__(self,managerController,master,user_id):
        self.master = master
        super().__init__(self.master)
        self.managerController = managerController
        self.user_id = user_id
        self.pack(fill=tk.BOTH,expand=True)
    
    def main(self):
        self._main_window_attributes()
        self._manager_frame()
        self._temp_label()

    def _main_window_attributes(self):
        # main window
        w = 900
        h = 720
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (w / 2)) - 12
        y = int((screen_height / 2) - (h / 2)) - 40

        self.master.title('S.I.M.S')
        self.master.geometry(f"{w}x{h}+{x}+{y}")
        self.master.resizable(False, False)

    def _manager_frame(self):
        self.managerFrame = tk.Frame(self,background="GhostWhite")
        self.managerFrame.pack(fill=tk.BOTH,expand=True)

    def _temp_label(self):
        temp_label = tk.Label(self.managerFrame,text=f"manager dasherboard | user ID: {self.user_id}")
        temp_label.place(relx=0.5,rely=0.5,anchor=CENTER)
