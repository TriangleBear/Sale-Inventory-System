from tkinter import *
import tkinter as tk
from Utils import Functions
from tkinter import font, messagebox

class RegisterView:
    def __init__(self,registerController,frame):
        self.registerController = registerController
        self.frame = frame
        
        self.register_labels_with_colspan = {"Name":1,"Number":1,"Address":3,"Access":1,"Email":1,"Username":1,"Password":1}
        self.register_entry_boxes = []
        self.register_inputs = []

    def main(self):
            
    def _register_frame(self):
        self.registerFrame = tk.Frame(self.frame,background="GhostWhite")
        self.registerFrame.pack(fill=tk.BOTH,expand=True)
    def _entry_frame(self):
        self.entryFrame = tk.Frame(self.registerFrame,background="Gray82")
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)
    def _register_widgets(self):
        Functions.create_entry_box_using_grid(frame=self.entryFrame,labels=self.register_labels_with_colspan,entryList=self.register_entry_boxes,max_columns=2,entryWidth=54)

    def _register_button(self):
        register_btn = tk.Button(self.entryFrame,font=font.Font(family='Poppins',weight='bold'), text="Register", command=lambda:self._checkInput(self.register_entry_boxes))
        register_btn.grid(row=4,columnspan=4,sticky='e',padx=5,pady=5)
            
    def _checkInput(self, data:list): 
        entryData = [entry.get() for entry in data]
        check_pass = self.registerController.check_password_criteria(entryData)
        if check_pass == 0:
            self.controller.register(user_id, access, first, last, username, password, email)
            messagebox.showinfo('Registration', 'Registration Successful!')
            self._switch_page(self._login_page)
        else:
            messagebox.showerror('Registration Error', check_pass)