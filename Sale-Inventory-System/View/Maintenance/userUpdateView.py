from tkinter import *
import tkinter as tk
from Utils import Functions
from tkinter import font, messagebox, ttk
from tkcalendar import DateEntry
from icecream import ic
from PIL import Image,ImageTk

class UserUpdateView(tk.Toplevel):
    def __init__(self,userUpdateController,user_data):
        super().__init__(background="GhostWhite")
        self.userUpdateController = userUpdateController
        self.user_data = user_data
        self.user_id = self.user_data[0]
        self._window_attributes()

        self.update_labels_with_colspan = {
            "First Name":1,
            "Last Name":1,
            "Access":1,
            "Birthdate":1,
            "Contact No.":1,
            "Email":1,
            "Address":3,
            "Username":1,
            "Password":1
        }
        self.levels_of_access = ["Manager","Staff"]
        self.update_entry_boxes = []
        self.update_inputs = []
        self.mainBg = "Gray89"

    def main(self):
        self._update_frame()  
        self._entry_frame()
        self._user_id_frame()
        self._user_id_lbl()
        self._update_widgets()
        self._insert_into_entry_boxes(self.update_entry_boxes,self.user_data[1:10])
        self._update_button()
        self._back_button()
        self.mainloop()

    def _window_attributes(self):
        self.h = 420
        self.w = 580
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        self.iconphoto(False, ImageTk.PhotoImage(Image.open("Sale-Inventory-System\Assets\icon.jpg")))
        self.title('User Registration')
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.quit())


    def _update_frame(self):
        self.updateFrame = tk.Frame(self,background="GhostWhite")
        self.updateFrame.pack(fill=tk.BOTH,expand=True)

    def _entry_frame(self):
        self.entryFrame = tk.Frame(self.updateFrame,background=self.mainBg,padx=40,pady=45)
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)

    def _user_id_frame(self):
        self.idFrame = tk.Frame(self,background=self.mainBg,width=580,height=40)
        self.idFrame.place(relx=0,rely=0)

    def _user_id_lbl(self):
        self.userIdLbl = tk.Label(self.idFrame,font=font.Font(family='Courier New',size=14,weight='bold'),
                              text=f"User ID: {self.user_id}",background=self.mainBg)
        self.userIdLbl.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _update_widgets(self):
        subset_one = {key:self.update_labels_with_colspan[key] for key in ["First Name","Last Name"] if key in self.update_labels_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_one,
            bgColor=self.mainBg,
            entryList=self.update_entry_boxes,
            borderW=1,
            max_columns=2,
            shortEntryWidth=20,
            longEntryWidth=55,
            side='e'
        )
        self._access_dropdown(1,0)
        self._update_birthdate_widget(1,2)
        subset_two = {key:self.update_labels_with_colspan[key] for key in ["Contact No.","Email","Address","Username","Password"] if key in self.update_labels_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_two,
            bgColor=self.mainBg,
            entryList=self.update_entry_boxes,
            borderW=1,
            max_columns=2,
            current_r=2,
            current_c=0,
            shortEntryWidth=20,
            longEntryWidth=55,
            side='e'
        )
        self.update_entry_boxes[-1].config(show="*")
    
    def _update_birthdate_widget(self,current_r=0,current_c=0):
        self.birthdate_lbl = tk.Label(self.entryFrame,text="Birthdate",background=self.mainBg)
        self.birthdate_lbl.grid(row=current_r,column=current_c,padx=5,pady=5,sticky='e')

        self.birthdate = DateEntry(self.entryFrame,width=17,borderwidth=0,year=2000,date_pattern='YYYY-MM-DD')
        self.birthdate.grid(row=current_r, column=current_c+1,padx=5,pady=5)
        self.birthdate.set_date(Functions.get_current_date())
        self.update_entry_boxes.append(self.birthdate)
        
    def _access_dropdown(self,current_r=0,current_c=0):
        self.access_lbl = tk.Label(self.entryFrame,text="Access: ",background=self.mainBg,anchor='e')
        self.access_lbl.grid(row=current_r,column=current_c,padx=1,pady=5,sticky='e')
        self.access_lbl.columnconfigure(2,weight=1)
        self.access = ttk.Combobox(self.entryFrame, values=self.levels_of_access,width=17)
        self.access.set("Select Category")
        self.access.grid(row=current_r, column=current_c+1, padx=1, pady=5)
        self.update_entry_boxes.append(self.access)

    def _insert_into_entry_boxes(self,entryData,list_to_insert):
        ic(list_to_insert)
        ic(len(list_to_insert))
        for i, entry_box in enumerate(entryData):
            data_to_insert = list_to_insert[i]
            if isinstance(entry_box, ttk.Combobox):
                entry_box.set(data_to_insert)
            if isinstance(entry_box, DateEntry):
                entry_box.set_date(data_to_insert)
            if i == len(list_to_insert)-1:
                continue
            try:
                entry_box.delete(0, 'end')
                entry_box.insert(0, data_to_insert)
            except AttributeError:
                print(f"Error: The widget {type(entry_box)} does not support delete/insert methods.")

    def _update_button(self):
        update_btn = tk.Button(self.entryFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Update", command=lambda:self._checkInput(self.update_entry_boxes))
        update_btn.grid(row=5,column=3,sticky='w',padx=5,pady=5)
    
    def _back_button(self):
        back_btn = tk.Button(self.entryFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Back", command=lambda:self.destroy())
        back_btn.grid(row=5,column=2,sticky='e',padx=5,pady=5)
            
    def _checkInput(self, input:list): 
        #user_id,fname, lname, user_type, birthdate, contact_num, email,address, username, password, created_on
        entryData = Functions.format_user_data(data=[entry.get() for entry in input])
        print(f"from _checkInput;RegisterView|entryData:\n{entryData}")
        check_pass = self.userUpdateController.check_password_criteria(entryData)
        if check_pass == 0:
            self.userUpdateController.updateUserData(entryData,self.user_id)
            self.userUpdateController.logUserActivity()
            messagebox.showinfo('User Data Update', 'Update Successful!')
            self.destroy()
        else:
            messagebox.showerror('Update Error', check_pass)