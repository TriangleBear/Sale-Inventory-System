from Utils import Functions
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
import tkinter as tk
class ForgotPasswordView(tk.Frame):
    def __init__(self,forgotPasswordController, master):
        super().__init__(master, background="GhostWhite")
        self.forgotPasswordController = forgotPasswordController

        self.confirm_password_labels_with_colspan = {"Old Password":1,"New Password":1,"Confirm Password":1}
        self.email_label_with_colspan = {"Username":1,"Email":1}
        self.forgot_password_entry_boxes = []
        self.pack(fill=tk.BOTH,expand=True)
    
    def main(self):
        self._center_frame()
        self._email_entry_widgets()
        self._confirm_button("email")

    def _reset_password_page(self):
        self._center_frame()
        self._reset_password_widgets()
        self._confirm_button("password")

    def _center_frame(self):
        self.entryFrame = tk.Frame(self,background="Gray82")
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)
    
    def _email_entry_widgets(self):
        Functions.create_entry_box_using_grid(frame=self.entryFrame,labels=self.email_label_with_colspan,entryList=self.forgot_password_entry_boxes,max_columns=1)

    def _reset_password_widgets(self):
        Functions.create_entry_box_using_grid(frame=self.entryFrame,labels=self.confirm_password_labels_with_colspan,entryList=self.forgot_password_entry_boxes,max_columns=1)
    
    def _confirm_button(self,state):
        confirm_btn = tk.Button(self.entryFrame,text="Confirm",borderwidth=1,background="AntiqueWhite1",command=lambda:self._checkInput(self.forgot_password_entry_boxes,state))
        confirm_btn.grid(row=3,columnspan=2,sticky='e',padx=5,pady=5)
    
    def _checkPassword(self,data:list):
        if all(_ is None for _ in data):
            messagebox.showerror('No Input', 'No provided Input')
        elif data[0] is None:
            messagebox.showerror('No Input', 'No provided Old Password')
            return
        elif data[1] is None:
            messagebox.showerror('No Input', 'No provided New Password')
            return
        elif data[2] is None:
            messagebox.showerror('No Input', 'No provided Confirm Password')
            return
        elif not data[2] == data[1]:
            messagebox.showerror('Invalid Input', 'Confirm Password must match New Password')
            return
        else:
            data.append(self.username) #[old_password, new_password, confirm_password, username]
            self.forgotPasswordController.checkPassInput([data[0],data[1],data[3]])



    def _checkAccount(self,data:list): #[username,email]
        
        if data[0] is None and data[1] is None:
            messagebox.showerror('No Input', 'No provided Username and Email')
            return
        elif data[0] is None:
            messagebox.showerror('No Input', 'No provided Username')
            return
        elif data[1] is None:
            messagebox.showerror('No Input', 'No provided Email')
            return
        else:
            userData = self.forgotPasswordController.checkAccountInputs(data) #userData = [username,email, otp]
            print(f"from _checkAccount | userData:{userData}")
            # self.forgotPasswordController.user_otp_verification(userData)
            messagebox.showinfo('OTP sent', 'Check Email for OTP')          
        
        provided_otp = askstring('OTP Verification', 'Enter OTP')
        if str(provided_otp) == str(userData[2]):
            Functions.destroy_page(self)
            self.forgot_password_entry_boxes = []
            self.username = userData[0]
            self._reset_password_page()

    def _checkInput(self, data:list,state:str):

        entryData = [entry.get() if entry.get()!='' else None for entry in data]
        if state == "email":
            self._checkAccount(entryData)
            return
        elif state == "password":
            self._checkPassword(entryData)
            return

