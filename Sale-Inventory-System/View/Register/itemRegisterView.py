import tkinter as tk
from tkinter import *
from tkinter import ttk,font,messagebox
from tkcalendar import DateEntry
from Utils import Functions


class ItemRegisterView(tk.Toplevel):
    def __init__(self,itemRegisterController,status):
        super().__init__(background="GhostWhite")
        self.itemRegisterController = itemRegisterController
        self.status = status
        self._window_attributes()

        #frames attributes
        self.mainBg = 'Grey90'

        #variables
        self.item_lbls_with_colspan = {
            "item Name":1,
            "Quantity":1,
            "Unit":1,
            "Price/unit":1,
            "Supplier":1,
            "Expiry Date":1,
            "menu_type":1,#supply item
            "Flooring":1,
            "Ceiling":1,


        }

        self.item_entry_boxes = []

        self.action_order = []

        self.categories = [
            "Fruits",
            "Vegetables",
            "Meats",
            "Poultry",
            "Seafood",
            "Dairy",
            "Grains",
            "Legumes",
            "Nuts and Seeds",
            "Herbs",
            "Spices",
            "Oils and Fats",
            "Sweeteners",
            "Condiments and Sauces",
            "Beverages"
        ]
        self.MenuType = ["Drinks","Desserts","Snacks"]

    def main(self):
        self._item_register_frame()
        if self.status == "Raw Item":
            self._item_register_widgets()
            self._register_button(4,3)
            self._back_button(4,2)
        if self.status == "Supply Item":
            self._supply_register_widgets()
            self._register_button(4,3)
            self._back_button(4,2)
        self.mainloop()


    def _window_attributes(self):
        self.h = 420
        self.w = 580
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        
        self.title(f'{self.status} Registration')
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.quit())

    def _item_register_frame(self):
        self.registerFrame = tk.Frame(self,background=self.mainBg,padx=40,pady=80)
        self.registerFrame.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    def _item_register_widgets(self):
        entrywidth = 23
        subset_one = {key:self.item_lbls_with_colspan[key] for key in ["item Name","Quantity","Unit","Price","Supplier"] if key in self.item_lbls_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.registerFrame,
            labels=subset_one,
            bgColor=self.mainBg,
            entryList=self.item_entry_boxes,
            borderW=1,
            max_columns=2,
            shortEntryWidth=entrywidth,
            side='e'
        )
        self._expiry_date_entry(2,0)
        self._category_dropdown(2,2) #row=2 column=(2-3)
        subset_two = {key:self.item_lbls_with_colspan[key] for key in ["Flooring","Ceiling"] if key in self.item_lbls_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.registerFrame,
            labels=subset_two,
            bgColor=self.mainBg,
            entryList=self.item_entry_boxes,
            borderW=1,
            max_columns=2,
            current_r=3,
            current_c=0,
            shortEntryWidth=entrywidth,
            side='e'
        )

    def _supply_register_widgets(self):
        entrywidth = 23
        subset_one = {key:self.item_lbls_with_colspan[key] for key in ["item Name","Quantity","Unit","Price","Supplier"] if key in self.item_lbls_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.registerFrame,
            labels=subset_one,
            bgColor=self.mainBg,
            entryList=self.item_entry_boxes,
            borderW=1,
            max_columns=2,
            shortEntryWidth=entrywidth,
            side='e'
        )
        self._expiry_date_entry(2,0)
        self._menu_type_dropdown(2,2)
        subset_two = {key:self.item_lbls_with_colspan[key] for key in ["Flooring","Ceiling"] if key in self.item_lbls_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.registerFrame,
            labels=subset_two,
            bgColor=self.mainBg,
            entryList=self.item_entry_boxes,
            borderW=1,
            max_columns=2,
            current_r=3,
            current_c=0,
            shortEntryWidth=entrywidth,
            side='e'
        )

    def _expiry_date_entry(self,current_r,current_c): #2,0
        self.expiry_date_lbl = tk.Label(self.registerFrame,text="Expiry Date:",background=self.mainBg)
        self.expiry_date_lbl.grid(row=current_r,column=current_c,padx=2,pady=2,sticky='e')

        self.expiry_date = DateEntry(self.registerFrame,width=20,borderwidth=0,year=2000,date_pattern='YYYY-MM-DD')
        self.expiry_date.set_date(Functions.get_current_date())
        self.expiry_date.grid(row=current_r,column=current_c+1,padx=2,pady=2)

        self.item_entry_boxes.append(self.expiry_date)

    def _category_dropdown(self,current_r,current_c): #2,2
        category_lbl = tk.Label(self.registerFrame,text="Category: ",background=self.mainBg,anchor='e')
        category_lbl.grid(row=current_r,column=current_c,padx=1,pady=5,sticky='e')
        category_lbl.columnconfigure(2,weight=1)
        category = ttk.Combobox(self.registerFrame,values=self.categories)
        category.set("Select Category")
        category.grid(row=current_r,column=current_c+1,padx=5,pady=5)
        self.item_entry_boxes.append(category)

    def _menu_type_dropdown(self,current_r,current_c): #3,0
        menu_type_lbl = tk.Label(self.registerFrame,text="Menu Type: ",background=self.mainBg,anchor='e')
        menu_type_lbl.grid(row=current_r,column=current_c,padx=1,pady=5,sticky='e')
        menu_type_lbl.columnconfigure(2,weight=1)
        menu_type = ttk.Combobox(self.registerFrame,values=self.MenuType)
        menu_type.set("Select Menu Type")
        menu_type.grid(row=current_r,column=current_c+1,padx=5,pady=5)
        self.item_entry_boxes.append(menu_type)

    def _register_button(self,current_r,current_c):#4,3 item #5,3 Supply
        register_btn = tk.Button(self.registerFrame,font=font.Font(family='Courier New',size=9,weight='bold'), 
                                 text="Register", command=lambda:self._checkInput(self.item_entry_boxes))
        register_btn.grid(row=current_r,column=current_c,sticky='w',padx=5,pady=5)

    def _checkInput(self, data:list): 
        #item name,quantity,price,supplier,expiry date, category, flooring, ceiling
        entryData = [entry.get().strip() for entry in data]
        if self.status == "Raw Item":
            entryData.append(None)
        print(f"from _checkInput;RegisterView|entryData:\n{entryData}")
        check_input = self.itemRegisterController.checkInput(entryData)
        if check_input == 0:
            self.itemRegisterController.register(entryData)
            self.itemRegisterController.logUserActivity()
            messagebox.showinfo('Item Registration', 'Item Registration Successful!')
            self.destroy()
        else:
            messagebox.showerror('Item Registration Error', check_input)
    
    def _back_button(self,current_r,current_c):#4,2 item #5,2 supply
        back_btn = tk.Button(self.registerFrame, text="Back",font=font.Font(family='Courier New',size=9,weight='bold'), command=lambda: self.destroy())
        back_btn.grid(row=current_r,column=current_c,sticky='e',padx=5,pady=5)
