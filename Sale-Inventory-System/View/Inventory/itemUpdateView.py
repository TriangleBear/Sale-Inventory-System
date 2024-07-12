import tkinter as tk
from tkinter import *
from tkinter import ttk,font,messagebox
from tkcalendar import DateEntry
from Utils import Functions
from icecream import ic
from PIL import Image,ImageTk

class ItemUpdateView(tk.Toplevel):
    def __init__(self,itemUpdateController,item_data):
        super().__init__(background="GhostWhite")
        self.itemUpdateController = itemUpdateController
        self.item_data = item_data
        self.item_id = self.item_data[0]
        self.status = "Raw Item"
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
        self.units = [
            "Grams (g)",
            "Kilograms (kg)",
            "Pounds (lb)",
            "Ounces (oz)",
            "Milliliters (ml)",
            "Liters (l)",
            "Fluid Ounces (fl oz)",
            "Cups",
            "Pc(s)",
            "Each (ea)",
            "Dozen (dz)",
            "Case (cs)"
        ]
        self.MenuType = ["Drinks","Desserts","Snacks"]
        self.item_entry_boxes = []
        self.action_order = []

    def main(self):
        self._item_entry_frame()
        self._item_register_widgets()
        self._insert_into_entry_boxes(self.item_entry_boxes, [item for i, item in enumerate(self.item_data) if i > 1 and i != len(self.item_data) - 1])
        self._item_id_frame()
        self._item_id_lbl()
        self._update_button(current_r=4,current_c=3)
        self._back_button(4,2)
        self.mainloop()

    def _window_attributes(self):
        self.h = 420
        self.w = 580
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        self.iconphoto(False, ImageTk.PhotoImage(Image.open("Sale-Inventory-System\Assets\icon.jpg")))
        self.title(f'Item Update')
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.quit())

    def _item_entry_frame(self):
        self.entryFrame = tk.Frame(self,background=self.mainBg,padx=20,pady=80)
        self.entryFrame.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _item_id_frame(self):
        self.idFrame = tk.Frame(self,background=self.mainBg,width=580,height=40)
        self.idFrame.place(relx=0,rely=0)

    def _item_id_lbl(self):
        self.itemIdLbl = tk.Label(self.idFrame,font=font.Font(family='Courier New',size=14,weight='bold'),
                              text=f"Item ID: {self.item_id}",background=self.mainBg)
        self.itemIdLbl.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    def _item_register_widgets(self):
        entrywidth = 23
        subset_one = {key:self.item_lbls_with_colspan[key] for key in ["item Name","Quantity"] if key in self.item_lbls_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_one,
            bgColor=self.mainBg,
            entryList=self.item_entry_boxes,
            borderW=1,
            max_columns=2,
            shortEntryWidth=entrywidth,
            side='e'
        )
        self._unit_dropdown(1,0)
        subset_two = {key:self.item_lbls_with_colspan[key] for key in ["Price","Supplier"] if key in self.item_lbls_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_two,
            bgColor=self.mainBg,
            entryList=self.item_entry_boxes,
            borderW=1,
            max_columns=2,
            current_r=1,
            current_c=2,
            shortEntryWidth=entrywidth,
            side='e'
        )
        self._expiry_date_entry(2,0)
        self._category_dropdown(2,2) #row=2 column=(2-3)
        subset_three = {key:self.item_lbls_with_colspan[key] for key in ["Flooring","Ceiling"] if key in self.item_lbls_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_three,
            bgColor=self.mainBg,
            entryList=self.item_entry_boxes,
            borderW=1,
            max_columns=2,
            current_r=3,
            current_c=0,
            shortEntryWidth=entrywidth,
            side='e'
        )
    
    def _insert_into_entry_boxes(self,entryData,list_to_insert):
        for i, entry_box in enumerate(entryData):
            data_to_insert = list_to_insert[i]
            if isinstance(entry_box, ttk.Combobox):
                entry_box.set(data_to_insert)
            if isinstance(entry_box, DateEntry):
                entry_box.set_date(data_to_insert)
            try:
                entry_box.delete(0, 'end')
                entry_box.insert(0, data_to_insert)
            except AttributeError:
                print(f"Error: The widget {type(entry_box)} does not support delete/insert methods.")

    def _unit_dropdown(self,current_r=0,current_c=0):
        unit_lbl = tk.Label(self.entryFrame,text="Unit: ",background=self.mainBg,anchor='e')
        unit_lbl.grid(row=current_r,column=current_c,padx=1,pady=5,sticky='e')
        unit_lbl.columnconfigure(2,weight=1)
        unit = ttk.Combobox(self.entryFrame,values=self.units)
        unit.set("Select Unit")
        unit.grid(row=current_r,column=current_c+1,padx=5,pady=5)
        self.item_entry_boxes.append(unit)


    def _expiry_date_entry(self,current_r=0,current_c=0): #2,0
        self.expiry_date_lbl = tk.Label(self.entryFrame,text="Expiry Date:",background=self.mainBg)
        self.expiry_date_lbl.grid(row=current_r,column=current_c,padx=2,pady=2,sticky='e')

        self.expiry_date = DateEntry(self.entryFrame,width=20,borderwidth=0,year=2000,date_pattern='YYYY-MM-DD')
        self.expiry_date.set_date(Functions.get_current_date())
        self.expiry_date.grid(row=current_r,column=current_c+1,padx=2,pady=2)

        self.item_entry_boxes.append(self.expiry_date)

    def _category_dropdown(self,current_r=0,current_c=0): #2,2
        category_lbl = tk.Label(self.entryFrame,text="Category: ",background=self.mainBg,anchor='e')
        category_lbl.grid(row=current_r,column=current_c,padx=1,pady=5,sticky='e')
        category_lbl.columnconfigure(2,weight=1)
        category = ttk.Combobox(self.entryFrame,values=self.categories)
        category.set("Select Category")
        category.grid(row=current_r,column=current_c+1,padx=5,pady=5)
        self.item_entry_boxes.append(category)


    def _checkInput(self, entries:list): 
        ic(entries)
        #item name,quantity,price,supplier,expiry date, category, flooring, ceiling
        entryData = Functions.format_item_data(data = [entry.get().strip() for entry in entries])
        ic(entryData)
        entryData.append(self.item_id)
        ic(entryData)
        check_input = self.itemUpdateController.checkInput(entryData,self.status)
        if check_input == 0:
            self.itemUpdateController.updateItem(entryData,self.status)
            self.itemUpdateController.logUserActivity()
            messagebox.showinfo('Item Update', 'Item Updated Successfully!')
            self.destroy()
        else:
            messagebox.showerror('Item Update Error', check_input)
            
    def _update_button(self,current_r=0,current_c=0,status=None):#4,3 item #5,3 Supply
        register_btn = tk.Button(self.entryFrame,font=font.Font(family='Courier New',size=9,weight='bold'), 
                                 text="Update", command=lambda:self._checkInput(self.item_entry_boxes))
        register_btn.grid(row=current_r,column=current_c,sticky='w',padx=5,pady=5)
    
    def _back_button(self,current_r,current_c):#4,2 item #5,2 supply
        back_btn = tk.Button(self.entryFrame, text="Back",font=font.Font(family='Courier New',size=9,weight='bold'), command=lambda: self.destroy())
        back_btn.grid(row=current_r,column=current_c,sticky='e',padx=5,pady=5)
