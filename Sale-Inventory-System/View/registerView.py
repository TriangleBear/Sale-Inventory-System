from tkinter import *
import tkinter as tk
from Utils import Functions
from tkinter import font, messagebox
from tkcalendar import DateEntry
class RegisterView:
    def __init__(self,registerController,frame):
        self.registerController = registerController
        self.frame = frame

        self.register_labels_with_colspan = {"First Name":1,
                                             "Last Name":1,
                                             "Access":1,
                                             "Birthdate":1,
                                             "Contact No.":1,
                                             "Email":1,
                                             "Address":3,
                                             "Username":1,
                                             "Password":1}
        self.register_entry_boxes = []
        self.register_inputs = []

    def main(self):
        self._register_frame()  
        self._entry_frame()
        self._register_widgets()
        self._register_button()

    def _register_frame(self):
        self.registerFrame = tk.Frame(self.frame,background="GhostWhite")
        self.registerFrame.pack(fill=tk.BOTH,expand=True)

    def _entry_frame(self):
        self.entryFrame = tk.Frame(self.registerFrame,background="Gray82")
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)

    def _register_widgets(self):
        subset_one = ["First Name","Last Name","Access"]
        Functions.create_entry_box_using_grid(frame=self.entryFrame,
                                              labels={key:self.register_labels_with_colspan[key] for key in subset_one if key in self.register_labels_with_colspan},
                                              entryList=self.register_entry_boxes,
                                              max_columns=2,
                                              entryWidth=54)
        self._register_birthdate_widget()
        subset_two = ["Contact No.","Email","Address","Username","Password"]
        Functions.create_entry_box_using_grid(frame=self.entryFrame,
                                              labels={key:self.register_labels_with_colspan[key] for key in subset_two if key in self.register_labels_with_colspan},
                                              entryList=self.register_entry_boxes,
                                              max_columns=2,
                                              current_r=2,
                                              current_c=0,
                                              entryWidth=54)
    
    def _register_birthdate_widget(self):
        self.birthdate_lbl = tk.Label(self.entryFrame,text="Birthdate",background="Gray82")
        self.birthdate_lbl.grid(row=1,column=2,padx=5,pady=5)

        self.birthdate = tk.DateEntry(self.entryFrame,borderwidth=0,year=2000)
        self.birthdate.grid(row=1,column=3,padx=5,pady=5)

        self.register_entry_boxes.append(self.birthdate)
        

    def _register_button(self):
        register_btn = tk.Button(self.entryFrame,font=font.Font(family='Courier New',size=12,weight='bold'), text="Register", command=lambda:self._checkInput(self.register_entry_boxes))
        register_btn.grid(row=4,columnspan=4,sticky='e',padx=5,pady=5)
            
    def _checkInput(self, data:list): 
        entryData = [entry.get() for entry in data]#user_id,fname, lname, user_type, birthdate, contact_num, email,address, username, password, created_on
        check_pass = self.registerController.check_password_criteria(entryData)
        if check_pass == 0:
            self.registerController.register(entryData)
            messagebox.showinfo('Registration', 'Registration Successful!')
            self._switch_page(self._login_page)
        else:
            messagebox.showerror('Registration Error', check_pass)