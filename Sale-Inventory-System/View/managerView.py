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
        self._header_frame()
        self._manager_label()
        self._header_buttons()
        self._body_frame()

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
        self.headerFrame = tk.Frame(self,background="Gray82")
        self.headerFrame.place(relx=0.5,rely=0.1,anchor='n')
    
    def _body_frame(self):
        self.bodyFrame = tk.Frame(self,background="GhostWhite")
        self.bodyFrame.place(relx=0.5,rely=0., anchor=CENTER)

    def _manager_label(self):
        self.manager_label = tk.Label(self.headerFrame,text=f"manager dasherboard | user ID: {self.user_id}")
        self.manager_label.place(relx=0.1,rely=0.5,anchor='w')
    
    def _button_frame(self):
        self.button_frame = tk.Frame(self.headerFrame, background="Gray82")
        self.button_frame.place(relx=0.7,rely=0.5,anchor='e')

    def _header_buttons(self):
        self.home_btn = tk.Button(self.button_frame, text="=Home",borderwidth=1,background="AntiqueWhite1", command=lambda:self.managerController.homePage(self.bodyFrame))
        self.home_btn.grid(row=0,column=0,padx=5,pady=5)

        self.logout_btn = tk.Button(self.button_frame, text="=Logout",borderwidth=1,background="AntiqueWhite1", command=lambda:self.managerController.loginController(self.master))
        self.logout_btn.grid(row=0,column=1,padx=5,pady=5)

    def _body_buttons(self):
        self.logout_btn = tk.Button(self.button_frame, text="=Logout",borderwidth=1,background="AntiqueWhite1", command=lambda:self.managerController.registerController(self.master))
        self.logout_btn.place(relx=0.5,rely=0.5,anchor=CENTER)