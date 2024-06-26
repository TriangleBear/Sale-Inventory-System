from tkinter import *
import tkinter as tk
from Utils import Functions
from tkinter import font, messagebox
from tkcalendar import DateEntry
class UserRegisterView(tk.Frame):
    def __init__(self,userRegisterController,master):
        self.userRegisterController = userRegisterController
        self.master = master
        super().__init__(self.master, background="GhostWhite")

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
        self.pack(fill=tk.BOTH,expand=True)
        self.mainBg = "Gray89"

    def main(self):
        self._register_frame()  
        self._entry_frame()
        self._register_widgets()
        self._register_button()
        self._back_button()

    def _register_frame(self):
        self.registerFrame = tk.Frame(self,background="GhostWhite")
        self.registerFrame.pack(fill=tk.BOTH,expand=True)

    def _entry_frame(self):
        self.entryFrame = tk.Frame(self.registerFrame,background=self.mainBg)
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)

    def _register_widgets(self):
        subset_one = {key:self.register_labels_with_colspan[key] for key in ["First Name","Last Name","Access"] if key in self.register_labels_with_colspan}
        Functions.create_entry_box_using_grid(frame=self.entryFrame,
                                              labels=subset_one,
                                              bgColor=self.mainBg,
                                              entryList=self.register_entry_boxes,
                                              borderW=1,
                                              max_columns=2,
                                              entryWidth=54)
        self._register_birthdate_widget()
        subset_two = {key:self.register_labels_with_colspan[key] for key in ["Contact No.","Email","Address","Username","Password"] if key in self.register_labels_with_colspan}
        Functions.create_entry_box_using_grid(frame=self.entryFrame,
                                              labels=subset_two,
                                              bgColor=self.mainBg,
                                              entryList=self.register_entry_boxes,
                                              borderW=1,
                                              max_columns=2,
                                              current_r=2,
                                              current_c=0,
                                              entryWidth=54)
    
    def _register_birthdate_widget(self):
        self.birthdate_lbl = tk.Label(self.entryFrame,text="Birthdate",background=self.mainBg)
        self.birthdate_lbl.grid(row=1,column=2,padx=5,pady=5)

        self.birthdate = DateEntry(self.entryFrame,borderwidth=0,year=2000,date_pattern='YYYY-MM-DD')
        self.birthdate.grid(row=1,column=3,padx=5,pady=5)

        self.register_entry_boxes.append(self.birthdate)
        

    def _register_button(self):
        register_btn = tk.Button(self.entryFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Register", command=lambda:self._checkInput(self.register_entry_boxes))
        register_btn.grid(row=5,column=4,sticky='w',padx=5,pady=5)
    
    def _back_button(self):
        back_btn = tk.Button(self.entryFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Back", command=lambda:self.userRegisterController.manager_body(self.master))
        back_btn.grid(row=5,column=3,sticky='e',padx=5,pady=5)
            
    def _checkInput(self, data:list): 
        #user_id,fname, lname, user_type, birthdate, contact_num, email,address, username, password, created_on
        entryData = [entry.get().strip() for entry in data]
        print(f"from _checkInput;RegisterView|entryData:\n{entryData}")
        check_pass = self.registerController.check_password_criteria(entryData)
        if check_pass == 0:
            self.registerController.register(entryData)
            messagebox.showinfo('Registration', 'Registration Successful!')
            self.userRegisterController.managerController(self.master)
        else:
            messagebox.showerror('Registration Error', check_pass)