from tkinter import *
import tkinter as tk
from tkinter import font,messagebox
from Utils import Functions, CustomDialog, CustomComboboxDialog
class StaffDashboard(tk.Frame):
    def __init__(self,staffController,master,user_id):
        self.master = master
        self._main_window_attributes()
        super().__init__(self.master, background="GhostWhite")
        self.sC = staffController
        self.user_id = user_id
        self.pack(fill=tk.BOTH,expand=True)

        #frames attributes
        self.mainBg = 'Grey90'

        #buttons
        self.main_btn_lbls = ["Point of Sale","Forget Password"]
        self.btns = []
        self.item_btns = []
    
    def main(self):
        self._header_frame()
        self._body_frame()
        self.body()

    def body(self):
        self._center_frame()
        self._body_buttons()
        

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

        self._user_label()
        self._home_button()
        self._logout_button()

    def _user_label(self):
        user_label = tk.Label(self.headerFrame,font=font.Font(family='Courier New',size=14,weight='bold'),
                              text=f"staff dashboard | user ID: {self.user_id}",background=self.mainBg)
        user_label.place(x=9,y=9)

    def _home_button(self):
        home_btn = tk.Button(self.headerFrame,font=font.Font(family='Courier New',size=9,weight='bold'),
                               text="Home", command=lambda:self._check_back_command("home page"))
        home_btn.place(relx=0.88,rely=0.5,anchor='e')

    def _logout_button(self):
        logout_btn = tk.Button(self.headerFrame,font=font.Font(family='Courier New',size=9,weight='bold'),
                               text="Logout", command=lambda:self._check_back_command("logout"))
        logout_btn.place(relx=0.95,rely=0.5,anchor='e')

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
                                            fontSize=13,
                                            gridxPadding=15,
                                            gridyPadding=10,
                                            btnyPadding=2,
                                            btnxPadding=10,
                                            cmd=self._check_buttons_command)

    def _main_register_buttons(self):
        Functions.create_buttons_using_grid(self.btn_frame,
                                            labels=self.registration_btn_lbls,
                                            entryList=self.btns,
                                            max_columns=2,
                                            w=21,
                                            h=1,
                                            fontSize=12,
                                            gridxPadding=10,
                                            gridyPadding=10,
                                            btnyPadding=2,
                                            btnxPadding=5,
                                            cmd=self._check_buttons_command)

    def _check_back_command(self,string):
        if string == "logout":
            if messagebox.askyesno('Confirm Logout','Proceed with logout?'):
                self.mC.mainController()
        if string == "home page":
            Functions.destroy_page(self.bodyFrame)
            self.body()

    def _entry_test(self):
        

    def _check_buttons_command(self,string):
        # if string == "Registration":
        #     Functions.destroy_page(self.bodyFrame)
        #     self.register_page()
        if string == "Point of Sale":
            self.sC.posController(self.bodyFrame)
        if string == "Forget Password":
            self.sC.forgotPasswordController(self.bodyFrame)
            

            