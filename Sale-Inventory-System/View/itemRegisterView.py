import tkinter as tk
from tkinter import *
from tkinter import ttk,font,messagebox
from Utils import Functions


class ItemRegisterView(tk.Toplevel):
    def __init__(self,itemRegisterController):
        super().__init__(background="GhostWhite")
        self.itemRegisterController = itemRegisterController
        self._window_attributes()

        #frames attributes
        self.mainBg = 'Grey90'

        #variables
        self.item_lbls_with_colspan = {
            "item Name":1,
            "Quantity":1,
            "Price":1,
            "Supplier":1,
            "Expiry Date":1,
            "Flooring":1,
            "Ceiling":1,
        }

        self.item_entry_boxes = []

        self.categories = ["Vegetable","Meat","Spice"]

    def main(self):
        self._item_register_frame()
        self._item_register_widgets()

        self._back_button()


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

        self.protocol("WM_DELETE_WINDOW", self.quit())

    def _item_register_frame(self):
        self.registerFrame = tk.Frame(self,background=self.mainBg)
        self.registerFrame.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    def _item_register_widgets(self):
        subset_one = {key:self.item_lbls_with_colspan[key] for key in ["item Name","Quantity","Price","Supplier","Expiry Date"] if key in self.item_lbls_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.registerFrame,
            labels=subset_one,
            bgColor=self.mainBg,
            entryList=self.item_entry_boxes,
            borderW=1,
            max_columns=2,
        )
        self._category_dropdown()
        subset_two = {key:self.item_lbls_with_colspan[key] for key in ["Flooring","Ceiling"] if key in self.item_lbls_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.registerFrame,
            labels=subset_two,
            bgColor=self.mainBg,
            entryList=self.item_entry_boxes,
            borderW=1,
            max_columns=2
        )

    def _category_dropdown(self):
        category = ttk.Combobox(self.registerFrame,values=self.categories)
        self.item_entry_boxes.append(category)

    def _register_button(self):
        register_btn = tk.Button(self.entryFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Register", command=lambda:self._check_input(self.item_entry_boxes))
        register_btn.grid(row=5,column=4,sticky='w',padx=5,pady=5)

    def _checkInput(self, data:list): 
        #item name,quantity,price,supplier,expiry date, category, flooring, ceiling, stock_level
        entryData = [entry.get().strip() for entry in data]
        print(f"from _checkInput;RegisterView|entryData:\n{entryData}")
        check_input = self.itemRegisterController.checkInput(entryData)
        if check_input == 0:
            self.itemRegisterController.register(entryData)
            messagebox.showinfo('Item Registration', 'Item Registration Successful!')
            self.itemRegisterController.managerController.close_toplevel()
        else:
            messagebox.showerror('Item Registration Error', check_input)
    
    def _back_button(self):
        back_btn = tk.Button(self.registerFrame, text="Back", command=lambda: self.quit())
        back_btn.place(relx=0.9, rely=0.5,anchor=CENTER)
