from tkinter import font
from tkinter import *
import tkinter as tk
from Utils import Functions
class RecipeRegisterView(tk.Frame):
    def __init__(self,recipeRegisterController,master):
        self.master = master
        self.recipeRegisterController = recipeRegisterController
        super().__init__(self.master,background="Gray89")
        self.pack(fill=tk.BOTH,expand=True)
        self.mainBg = "Gray89"
        # self.recipe_labels_with_colspan = {
        #     "Recipe Name":1,
        #     "Category":1,
        #     "Ingredients":1,
        #     "Details":3
        # }
        # self.recipe_entry_boxes = []
        # self.recipe_inputs = []

    def main(self):
        self._entry_frame()
        self._recipe_label()
        self._recipe_name_entry()
        self._confirm_button()
        self._back_button()


    def _entry_frame(self):
        self.entryFrame = tk.Frame(self,background=self.mainBg,padx=40,pady=80)
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)
    
    def _recipe_label(self):
        recipe_label = tk.Label(self.entryFrame,font=font.Font(family='Courier New',size=14,weight='bold'),
                              text=f"Recipe Name: ",background=self.mainBg)
        recipe_label.grid(row=0,column=0)

    def _recipe_name_entry(self):
        self.recipe_name_entry = tk.Entry(self.entryFrame, borderwidth=0, width=23,font=font.Font(size=12))
        self.recipe_name_entry.grid(row=0,column=1)  

    def _commit_recipe_name(self,recipe_name):
        self.recipeRegisterController.register_recipe(recipe_name)

    def _confirm_button(self):
        confirm_button = tk.Button(self.entryFrame, font=font.Font(family='Courier New',size=9,weight='bold'),text="Confirm", command=lambda:self._commit_recipe_name(self.recipe_name_entry.get()))
        confirm_button.grid(row=1,column=1,sticky='e')
    
    def _back_button(self):
        back_button = tk.Button(self, font=font.Font(family='Courier New',size=9,weight='bold'),text="Back", command=lambda:self.recipeRegisterController.manager_view(self.master))
        back_button.place(relx=0.1,rely=0.9,anchor='sw')  # Place the button at the bottom with some padding


class RecipeRegisterTopLevel(tk.Toplevel):
    def __init__(self,recipeRegisterController):
        super().__init__(background="GhostWhite")
        self.recipeRegisterController = recipeRegisterController
        self._window_attributes()

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
        self.register_entry_boxes = []
        self.register_inputs = []
        self.mainBg = "Gray89"

    def main(self):
        self._register_frame()  
        self._entry_frame()
        self._register_widgets()
        self._register_button()
        self._back_button()
        self.mainloop()

    def _window_attributes(self):
        self.h = 420
        self.w = 580
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        self.title('Item Registration')
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.quit())


    def _register_frame(self):
        self.registerFrame = tk.Frame(self,background="GhostWhite")
        self.registerFrame.pack(fill=tk.BOTH,expand=True)

    def _entry_frame(self):
        self.entryFrame = tk.Frame(self.registerFrame,background=self.mainBg,padx=40,pady=80)
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)

    def _register_widgets(self):
        subset_one = {key:self.register_labels_with_colspan[key] for key in ["First Name","Last Name","Access"] if key in self.register_labels_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_one,
            bgColor=self.mainBg,
            entryList=self.register_entry_boxes,
            borderW=1,
            max_columns=2,
            longEntryWidth=54,
            side='e'
        )
        self._register_birthdate_widget()
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
            longEntryWidth=54,
            side='e'
        )
    
    def _register_birthdate_widget(self):
        self.birthdate_lbl = tk.Label(self.entryFrame,text="Birthdate",background=self.mainBg)
        self.birthdate_lbl.grid(row=1,column=2,padx=5,pady=5,sticky='e')

        self.birthdate = DateEntry(self.entryFrame,width=15,borderwidth=0,year=2000,date_pattern='YYYY-MM-DD')
        self.birthdate.grid(row=1,column=3,padx=5,pady=5)
        self.birthdate.set_date(Functions.get_current_date())
        self.register_entry_boxes.append(self.birthdate)
        

    def _register_button(self):
        register_btn = tk.Button(self.entryFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Register", command=lambda:self._checkInput(self.register_entry_boxes))
        register_btn.grid(row=5,column=3,sticky='w',padx=5,pady=5)
    
    def _back_button(self):
        back_btn = tk.Button(self.entryFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Back", command=lambda:self.destroy())
        back_btn.grid(row=5,column=2,sticky='e',padx=5,pady=5)
            
    def _checkInput(self, data:list): 
        #user_id,fname, lname, user_type, birthdate, contact_num, email,address, username, password, created_on
        entryData = [entry.get().strip() for entry in data]
        print(f"from _checkInput;RegisterView|entryData:\n{entryData}")
        check_pass = self.userRegisterController.check_password_criteria(entryData)
        if check_pass == 0:
            self.userRegisterController.register(entryData)
            messagebox.showinfo('Registration', 'Registration Successful!')
            self.userRegisterController.managerController(self.master)
        else:
            messagebox.showerror('Registration Error', check_pass)