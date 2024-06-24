from tkinter import *
import tkinter as tk
from Utils import Functions
from tkinter import font, messagebox
from tkinter.simpledialog import askstring
import logging


"""
    REMOVE ALL PRINT STATEMENTS
"""

class LoginView(tk.Frame):
    def __init__(self,loginController,master):
        self.master = master
        super().__init__(self.master, background="GhostWhite")
        self.loginController = loginController

        #variables
        #login  
        self.login_labels_with_colspan = {"Username":1, "Password":1}
        self.login_entry_boxes = []
        self.pack(fill=tk.BOTH,expand=True)

    def main(self):
        self._center_frame()
        self._login_widgets()
        self._forgot_password_button()
        self._login_button()

    def checkLoginInput(self, data:list):
        entryData = [entry.get() for entry in data]
        username = entryData[0]
        logging.debug(f"Attempting login with username: {username}")
        userData = self.loginController.checkInput(entryData) # returns a list of [userId,userType, email,otp]
        logging.debug(f"Received user data: {userData}")
        print(f"from checkInput; userData: {userData}")
        # uncomment if send otp to email is needed for testing/demo
        # self.loginController.user_otp_verification(userData)
        messagebox.showinfo('OTP Sent', 'Check Email for OTP')
        provided_otp = askstring('OTP Verification', 'Enter OTP')
        logging.debug("Sent OTP!")
        if str(provided_otp) == str(userData[3]):
            print(f"from checkInput loginView; otp|userData[2]: {userData[3]}")
            print(f"from checkInput loginView; provided_otp: {provided_otp}")
            messagebox.showinfo('Login Status', 'Login Successful!')
            if userData[1] == "Manager":
                self.loginController.managerPage(self.master,userData[0])
            elif userData[1] == "Staff":
                self.loginController._switch_page(self.loginController._staff_page)

    def _center_frame(self):
        self.entryFrame = tk.Frame(self,background="Gray82")
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)

    def _login_widgets(self):
        Functions.create_entry_box_using_grid(frame=self.entryFrame,labels=self.login_labels_with_colspan,entryList=self.login_entry_boxes,max_columns=1)
        
    def _forgot_password_button(self):
        forgot_password_btn = tk.Button(self.entryFrame,font=font.Font(family='Courier New',weight='bold'),text="Forgot Password",borderwidth=0,background="Gray82", command=lambda:self.loginController.forgotPasswordController(self.master))
        
        forgot_password_btn.grid(row=2,columnspan=2,sticky='e',padx=5,pady=5)        
        
    def _login_button(self):
        login_btn = tk.Button(self.entryFrame, text="Login",borderwidth=1,background="AntiqueWhite1", command=lambda:self.checkLoginInput(self.login_entry_boxes))

        login_btn.grid(row=3,columnspan=2,sticky='e',padx=5,pady=5)




    

