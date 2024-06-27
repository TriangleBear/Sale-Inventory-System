from tkinter import *
import tkinter as tk
from tkinter import font
from Utils import Functions
class ManagerDashboard(tk.Frame):
    def __init__(self,managerController,master,user_id):
        self.master = master
        self._main_window_attributes()
        super().__init__(self.master, background="GhostWhite")
        self.managerController = managerController
        self.user_id = user_id
        self.pack(fill=tk.BOTH,expand=True)

        #frames attributes
        self.mainBg = 'Grey90'

        #buttons
        self.main_btn_lbls = ["Security", "Registration","Inventory", "Supplies", "Point of Sale", "Report", "Maintenance"]
        self.registration_btn = ["User Registration","Item Registration","product Registration","recipe Registration"]
        self.btns = []
    
    def main(self):
        self._header_frame()
        self._user_label()
        self._body_frame()
        self.body()



    def body(self):
        self._center_frame()
        self._body_buttons()



    def register_page(self):
        self._center_frame()
        self.main_register_buttons() # load buttons
        self._back_button("register_page")

    def _main_window_attributes(self):
        # main window
        self.h = 720
        self.w = 900
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        self.master.title('S.I.M.S')
        self.master.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.master.resizable(False, False)

    def _header_frame(self):
        self.headerFrame = tk.Frame(self,background=self.mainBg)
        self.headerFrame.place(x=0,y=0, width=900,height=45)

    def _user_label(self):
        user_label = tk.Label(self.headerFrame,font=font.Font(family='Courier New',size=14,weight='bold'),text=f"manager dasherboard | user ID: {self.user_id}",background=self.mainBg)
        user_label.place(x=9,y=9)

    def _body_frame(self):
        self.bodyFrame = tk.Frame(self, background=self.mainBg)
        self.bodyFrame.place(x=30,y=75,width=(self.w-60),height=self.h-120)

    def _center_frame(self):
        self.btn_frame = tk.Frame(self.bodyFrame,background=self.mainBg)
        self.btn_frame.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _body_buttons(self):
        Functions.create_buttons_using_grid(self.btn_frame,
                                            labels=self.main_btn_lbls,
                                            entryList=self.btns,
                                            max_columns=2,
                                            w=16,
                                            h=1,
                                            xPadding=10,
                                            yPadding=10,
                                            cmd=self._check_buttons_command)

    def main_register_buttons(self):
        Functions.create_buttons_using_grid(self.btn_frame,
                                            labels=self.registration_btn,
                                            entryList=self.btns,
                                            max_columns=2,
                                            w=21,
                                            h=1,
                                            xPadding=10,
                                            yPadding=10,
                                            cmd=self._check_buttons_command)

    def _back_button(self,state:str):
        self.back_btn = tk.Button(self.bodyFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Back", background="Grey89",command=lambda:self._check_back_command(f"{state}"))
        self.back_btn.place(relx=0.5,rely=0.9,anchor='s')

    def _check_back_command(self,string):
        if string == "register_page":
            Functions.destroy_page(self.bodyFrame)
            self.body()

    def _check_buttons_command(self,string):
        if string == "Registration":
            Functions.destroy_page(self.bodyFrame)
            self.register_page()
        if string == "Report": 
            self.managerController.reportController(self.bodyFrame)
        if string == "User Registration":
            self.managerController.userRegisterController()
        if string == "Item Registration":
            self.managerController.itemRegisterController()

