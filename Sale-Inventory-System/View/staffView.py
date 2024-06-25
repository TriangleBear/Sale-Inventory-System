from tkinter import *
import tkinter as tk
class StaffDashboard(tk.Tk):
    def __init__(self,staffController,master,user_id):
        self.master = master
        super().__init__(self.master)
        self.staffController = staffController
        self.user_id = user_id
        self.pack(fill=tk.BOTH,expand=True)
        

    def main(self):
        self._main_window_attributes()
        self._staff_frame()
        self._temp_label()

    def _main_window_attributes(self):
        # main window
        w = 900
        h = 720
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (w / 2)) - 12
        y = int((screen_height / 2) - (h / 2)) - 40

        self.title('S.I.M.S')
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.resizable(False, False)

    def _staff_frame(self):
        self.staffFrame = tk.Frame(self,background="GhostWhite")
        self.staffFrame.pack(fill=tk.BOTH,expand=True)

    def _temp_label(self):
        temp_label = tk.Label(self.staffFrame,text=f"staff dasherboard | user ID: {self.user_id}")
        temp_label.place(relx=0.5,rely=0.5,anchor=CENTER)