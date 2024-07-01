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
        self.mainBg = "Gray89"
        self.pack(fill=tk.BOTH,expand=True)

    def main(self):
        self._center_frame()
        self._login_widgets()
        self._forgot_password_button()
        self._login_button()

    def _askOTP(self,verifiedUserData:list):#[userID,userType,email,otp]
        provided_otp = askstring('OTP Verification', 'Enter OTP')
        if str(provided_otp) == str(verifiedUserData[3]):
            messagebox.showinfo('Login Status', 'Login Successful!')
            if verifiedUserData[1] == "Manager":
                self.loginController.logUserActivity([verifiedUserData[0]])
                self.loginController.managerController(self.master,verifiedUserData[0])
            if verifiedUserData[1] == "Staff":
                self.loginController.staffController(self.master,verifiedUserData[0])

    def _checkLoginInput(self, data:list):
        entryData = [entry.get() for entry in data]
        # username = entryData[0]
        userData = self.loginController.checkInput(entryData) 
        # userData = [userId,userType, email,otp]

        if type(userData) == list:
            # self.loginController.user_otp_verification(userData)
            messagebox.showinfo('OTP Sent', 'Check Email for OTP')
            print(f"from _checkLoginInput;loginView|userData:{userData}")
            self._askOTP(userData)
        else:
            messagebox.showerror('Invalid Input',userData)

    def _center_frame(self):
        self.entryFrame = tk.Frame(self,background=self.mainBg)
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)

    def _login_widgets(self):
        Functions.create_entry_box_using_grid(frame=self.entryFrame, labels=self.login_labels_with_colspan, 
                                              entryList=self.login_entry_boxes, max_columns=1)
        self.login_entry_boxes[1].config(show="*")
        
    def _forgot_password_button(self):
        forgot_password_btn = tk.Button(self.entryFrame,font=font.Font(family='Courier New',size=9,weight='bold'),
                                        text="Forgot Password",borderwidth=0,background=self.mainBg,
                                        command=lambda:self.loginController.forgotPasswordController(self.master))
        forgot_password_btn.grid(row=2,columnspan=2,sticky='e',padx=5,pady=5)        
        
    def _login_button(self):
        login_btn = tk.Button(self.entryFrame, text="Login",borderwidth=1,background="AntiqueWhite1",
                              command=lambda:self._checkLoginInput(self.login_entry_boxes))
        login_btn.grid(row=3,columnspan=2,sticky='e',padx=5,pady=5)

    




    

