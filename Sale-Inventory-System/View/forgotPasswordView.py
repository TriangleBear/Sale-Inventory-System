from Utils import Functions
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
import tkinter as tk
class ForgotPasswordView(tk.Frame):
    def __init__(self,forgotPasswordController, master):
        self.master = master
        super().__init__(self.master, background="GhostWhite")
        self.forgotPasswordController = forgotPasswordController

        self.confirm_password_labels_with_colspan = {"Old Password":1,"New Password":1,"Confirm Password":1}
        self.email_label_with_colspan = {"Username":1,"Email":1}
        self.forgot_password_entry_boxes = []
        self.pack(fill=tk.BOTH,expand=True)
    
    def main(self):
        self._center_frame()
        self._email_entry_widgets()
        self._back_button("email")
        self._confirm_button("email")

    def _reset_password_page(self):
        self._center_frame()
        self._reset_password_widgets()
        self._back_button("password")
        self._confirm_button("password")

    def _center_frame(self):
        self.entryFrame = tk.Frame(self,background="Gray82")
        self.entryFrame.place(relx =0.5,rely=0.4,anchor=CENTER)
    
    def _email_entry_widgets(self):
        Functions.create_entry_box_using_grid(frame=self.entryFrame,labels=self.email_label_with_colspan,entryList=self.forgot_password_entry_boxes,max_columns=1)

    def _reset_password_widgets(self):
        Functions.create_entry_box_using_grid(frame=self.entryFrame,labels=self.confirm_password_labels_with_colspan,entryList=self.forgot_password_entry_boxes,max_columns=1)
    
    def _back_button(self,state):
        back_btn = tk.Button(self.entryFrame,text="Back",borderwidth=1,background="AntiqueWhite1",command=lambda:self._checkBackInput(state))
        back_btn.grid(row=3,column=1,sticky='w',padx=5,pady=5)

    def _confirm_button(self,state):
        confirm_btn = tk.Button(self.entryFrame,text="Confirm",borderwidth=1,background="AntiqueWhite1",command=lambda:self._checkConfirmInput(self.forgot_password_entry_boxes,state))
        confirm_btn.grid(row=3,column=1,sticky='e',padx=5,pady=5)
    
    def _checkPassword(self,data:list):
        userData = self.forgotPasswordController.checkPassInput(data) 
        #[old_password, new_password, confirm_password, username]
        
        if type(userData) == list:
            # self.forgotPasswordController.user_otp_verification(userData)
            print(f"from _checkAccount;forgotPasswordView|userData:\n{userData}")
            self._askOTP()
        else:
            messagebox.showerror('Invalid Input', userData)   
        # if all(_ is None for _ in data):
        #     messagebox.showerror('No Input', 'No provided Input')
        # elif data[0] is None:
        #     messagebox.showerror('No Input', 'No provided Old Password')
        #     return
        # elif data[1] is None:
        #     messagebox.showerror('No Input', 'No provided New Password')
        #     return
        # elif data[2] is None:
        #     messagebox.showerror('No Input', 'No provided Confirm Password')
        #     return
        # elif not data[2] == data[1]:
        #     messagebox.showerror('Invalid Input', 'Confirm Password must match New Password')
        #     return
        # else:
        #     data.append(self.username) #[old_password, new_password, confirm_password, username]
        #     check_pass = self.forgotPasswordController.checkPassInput(data)
        #     if check_pass == 0:
        #         self.forgotPasswordController.update_password(data)
        #         messagebox.showinfo('Registration', 'Registration Successful!')
        #         self._switch_page(self._login_page)
        #     else:
        #         messagebox.showerror('Registration Error', check_pass)
        #     self.forgotPasswordController.checkPassInput([data[0],data[1],data[3]])


    def _askOTP(self, verifiedUserData:list):
        provided_otp = askstring('OTP Verification', 'Enter OTP')
        if str(provided_otp) == str(verifiedUserData[2]):
            Functions.destroy_page(self)
            self.forgot_password_entry_boxes = []
            self.username = verifiedUserData[0]
            self._reset_password_page()

    def _checkAccount(self,data:list): #[username,email]
        userData = self.forgotPasswordController.checkAccountInput(data) 
        #userData = [username,email, otp] or 0
        
        if type(userData) == list:
            # self.forgotPasswordController.user_otp_verification(userData)
            print(f"from _checkAccount;forgotPasswordView|userData:\n{userData}")
            self._askOTP()
        else:
            messagebox.showerror('Invalid Input', userData)          
        
        
    def _checkBackInput(self,state:str):
        if state == "email":
            self.forgotPasswordController.loginController(self.master)
        if state == "password":
            Functions.destroy_page(self)
            self.main()

    def _checkConfirmInput(self, data:list,state:str):
        entryData = [entry.get() for entry in data]
        if state == "email":
            self._checkAccount(entryData) #[username,email]
            return
        if state == "password":
            self._checkPassword(entryData) #[old_password,new_password,confirm_password]
            
            return

