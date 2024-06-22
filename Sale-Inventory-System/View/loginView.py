from tkinter import *
import tkinter as tk
from View import Functions
from tkinter import font, messagebox
from tkinter.simpledialog import askstring
import logging


"""
    REMOVE ALL PRINT STATEMENTS
"""

class LoginView(tk.Frame):
    def __init__(self,loginController,master):
        super().__init__(master)
        self.loginController = loginController

        #variables
        #login  
        self.login_labels_with_colspan = {"Username":1, "Password":1}
        self.login_entry_boxes = []
        self.pack(fill=tk.BOTH,expand=True)

    def main(self):
        self._login_frame()
        self._center_frame()
        self._login_widgets()
        self._register_button()
        self._login_button()


    def _login_frame(self):
        self.loginFrame = tk.Frame(self,background="GhostWhite")
        self.loginFrame.pack(fill=tk.BOTH,expand=True)

    def _center_frame(self):
        self.entryFrame = tk.Frame(self.loginFrame,background="Gray82")
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)

    def _login_widgets(self):
        Functions.create_entry_box_using_grid(frame=self.entryFrame,labels=self.login_labels_with_colspan,entryList=self.login_entry_boxes,max_columns=1)
        
    def _register_button(self):
        register_btn = tk.Button(self.entryFrame,font=font.Font(family='Poppins',weight='bold'),text="Register",borderwidth=0,background="Gray82", command=lambda:Functions.destroy_page (self.frame, self.loginController.register_page))
        
        register_btn.grid(row=2,columnspan=2,sticky='e',padx=5,pady=5)

    def _login_button(self):
        login_btn = tk.Button(self.entryFrame, text="Login",borderwidth=1,background="AntiqueWhite1", command=lambda:self.checkInput(self.login_entry_boxes))

        login_btn.grid(row=3,columnspan=2,sticky='e',padx=5,pady=5)

    def checkInput(self, data:list):
        entryData = [entry.get() for entry in data]
        username = entryData[0]
        logging.debug(f"Attempting login with username: {username}")
        userData = self.loginController.checkInput(entryData) # returns a list of user type, email and otp
        logging.debug(f"Received user data: {userData}")
        print(f"from checkInput; userData: {userData}")
        # uncomment if send otp to email is needed for testing/demo
        # self.loginController.user_otp_verification(userData)
        messagebox.showinfo('OTP Sent', 'Check Email for OTP')
        provided_otp = askstring('OTP Verification', 'Enter OTP')
        logging.debug("Sent OTP!")
        if str(provided_otp) == str(userData[2]):
            print(f"from checkInput loginView; otp|userData[2]: {userData[2]}")
            print(f"from checkInput loginView; provided_otp: {provided_otp}")
            messagebox.showinfo('Login Status', 'Login Successful!')
            if userData[0] == "Manager":
                self.loginController._switch_page(self.loginController._manager_page)
            elif userData[0] == "Staff":
                self.loginController._switch_page(self.loginController._staff_page)
