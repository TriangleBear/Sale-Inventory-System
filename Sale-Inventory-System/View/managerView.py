from tkinter import *
import tkinter as tk
from tkinter import font
class ManagerDashboard(tk.Frame):
    def __init__(self,managerController,master,user_id):
        self.master = master
        super().__init__(self.master)
        self.managerController = managerController
        self.user_id = user_id
        self.pack(fill=tk.BOTH,expand=True)
    
    def main(self):
        self._main_window_attributes()
        self._header_frame()
        self._user_label()

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

    def _header_frame(self):
        self.headerFrame = tk.Frame(self,background="GhostWhite")
        self.headerFrame.place(relx=0.5,rely=0.2,anchor='n')

    def _user_label(self):
        user_label = tk.Label(self.headerFrame,font=font.Font(family='Courier New',size=14,weight='bold'),text=f"manager dasherboard | user ID: {self.user_id}")
        user_label.pack()

    # def _register_button(self):
    #     self.register_btn = tk.Button(self.entryFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Register", command=lambda:self.managerController.registerController(self.master))
    #     self.register_btn.pack()