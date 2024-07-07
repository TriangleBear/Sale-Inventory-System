from tkinter import font, messagebox, ttk, CENTER
import tkinter as tk
from tkcalendar import DateEntry
from Utils import Functions
class UserUpdateView(tk.Toplevel):
    def __init__(self,managerController,userUpdateController,user_data):
        self.mC = managerController
        self.userUpdateController = userUpdateController
        self.user_data = user_data
        self.user_id = self.user_data[0]
        super().__init__(background="Gray89")
        self._window_attributes()

        self.mainBg = "Gray89"

        self.register_labels_with_colspan = {
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

        self.user_entry_boxes = []
        self.action_order = []

    def main(self):
        self._user_entry_frame()
        self._user_register_widgets()
        self._insert_into_entry_boxes(self.user_entry_boxes, [item for i, item in enumerate(self.item_data) if i > 1 and i != len(self.item_data) - 1])
        self._user_buttons()
        self.mainloop()

    def _window_attributes(self):
        self.h = 420
        self.w = 580
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        
        self.title('Update User')
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.quit())

    def _user_entry_frame(self):
        self.entryFrame = tk.Frame(self,background=self.mainBg,padx=20,pady=80)
        self.entryFrame.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _user_id_frame(self):
        self.idFrame = tk.Frame(self,background=self.mainBg,width=580,height=40)
        self.idFrame.place(relx=0,rely=0)

    def _user_id_lbl(self):
        self.userIdLbl = tk.Label(self.idFrame,font=font.Font(family='Courier New',size=14,weight='bold'),
                              text=f"User ID: {self.user_id}",background=self.mainBg)
        self.userIdLbl.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _user_register_widgets(self):
        entrywidth = 23
        subset_one = {key:self.register_labels_with_colspan[key] for key in ["First Name","Last Name"] if key in self.register_labels_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_one,
            bgColor=self.mainBg,
            entryList=self.register_entry_boxes,
            borderW=1,
            max_columns=2,
            shortEntryWidth=20,
            longEntryWidth=55,
            side='e'
        )
        self._access_dropdown(1,0)
        self._register_birthdate_widget(1,2)
        subset_two = {key:self.register_labels_with_colspan[key] for key in ["Contact No.","Email","Address","Username","Password"] if key in self.register_labels_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_two,
            bgColor=self.mainBg,
            entryList=self.register_entry_boxes,
            borderW=1,
            max_columns=2,
            current_r=2,
            current_c=0,
            shortEntryWidth=20,
            longEntryWidth=55,
            side='e'
        )

    def _insert_into_entry_boxes(self,entryData,list_to_insert):
        for i, entry_box in enumerate(entryData):
            data_to_insert = list_to_insert[i]
            if isinstance(entry_box,ttk.Combobox):
                entry_box.insert(data_to_insert)
            if isinstance(entry_box,DateEntry):
                entry_box.insert(data_to_insert)
            try:
                entry_box.insert(0, 'end')
                entry_box.insert(0, data_to_insert)
            except AttributeError:
                print(f"Error: The widget {type(entry_box)} does not support delete/insert methods.")

    def _access_dropdown(self,row,column):
        accessLbl = tk.Label(self.entryFrame,font=font.Font(family='Courier New',size=12,weight='bold'),
                              text="Access",background=self.mainBg)
        accessLbl.grid(row=row,column=column,sticky='e')

        accessVar = tk.StringVar()
        accessVar.set(self.user_data[3])
        accessEntry = ttk.Combobox(self.entryFrame,width=23,textvariable=self.accessVar)
        accessEntry['values'] = ('Staff', 'Manager')
        accessEntry.grid(row=row,column=column+1,sticky='w')
        self.register_entry_boxes.append(accessEntry)

    def _register_birthdate_widget(self,row,column):
        birthdateLbl = tk.Label(self.entryFrame,font=font.Font(family='Courier New',size=12,weight='bold'),
                              text="Birthdate",background=self.mainBg)
        birthdateLbl.grid(row=row,column=column,sticky='e')

        birthdateEntry = DateEntry(self.entryFrame,width=23,date_pattern='yyyy-mm-dd')
        birthdateEntry.grid(row=row,column=column+1,sticky='w')
        self.register_entry_boxes.append(birthdateEntry)

    def _user_buttons(self):
        self.updateBtn = tk.Button(self,font=font.Font(family='Courier New',size=12,weight='bold'),
                                   text="Update",command=lambda:self._checkInput(self.register_entry_boxes))
        self.updateBtn.place(relx=0.5,rely=0.9,anchor=CENTER)

    def _checkInput(self,entryBoxes):
        self.action_order = []
        for entry_box in entryBoxes:
            try:
                entry_data = entry_box.get()
                if entry_data == '':
                    messagebox.showerror("Error","Please fill up all fields.")
                    break
                self.action_order.append(entry_data)
            except AttributeError:
                print(f"Error: The widget {type(entry_box)} does not support get method.")
        self._update_user()

    def _update_user(self):
        self.userUpdateController.update_user(self.user_id,self.action_order)
    