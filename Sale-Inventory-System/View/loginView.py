from tkinter import *
import tkinter as tk
from View import Functions
from tkinter import font, messagebox


class LoginPage:
    def __init__(self,loginController,frame):
        self.loginController = loginController
        self.frame = frame
        #variables
        #login 
        self.login_labels_with_colspan = {"Username":1, "Password":1}
        self.login_entry_boxes = []

    def checkInput(self,creds:list):
        credentials = [input.get() for input in creds]
        value:list = self.loginController.checkInput(credentials)
        if value[0] == False:
            messagebox.showerror('Invalid Input', 'no such user was found')
        elif value[0] == "Admin" or value[0] == "Manager":
            Functions.switch_page(self.frame,self.loginController.manager_dashboard,self.frame)
        elif value[0] == "Staff":
            self._switch_page(self._staff_page)
        else:
            self._invalid_input_page()
    
    def main(self):
        self.loginFrame = tk.Frame(self.frame,background="GhostWhite")
        self.loginFrame.pack(fill=tk.BOTH,expand=True)

        #center frame
        entryFrame = tk.Frame(self.loginFrame,background="Gray82")
        entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)

        #widgets/buttons/lbls
        Functions._create_entry_box_using_grid(frame=entryFrame,labels=self.login_labels_with_colspan,entryList=self.login_entry_boxes,max_columns=1)
        register_btn = tk.Button(entryFrame,font=font.Font(family='Poppins',weight='bold'),text="Register",borderwidth=0,background="Gray82", command=lambda:Functions._switch_page(Functions._register_page))
        login_btn = tk.Button(entryFrame, text="Login",borderwidth=1,background="AntiqueWhite1", command=lambda:self.checkInput(self.login_entry_boxes))

        register_btn.grid(row=2,columnspan=2,sticky='e',padx=5,pady=5)
        login_btn.grid(row=3,columnspan=2,sticky='e',padx=5,pady=5)