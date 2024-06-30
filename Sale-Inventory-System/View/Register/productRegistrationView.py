import tkinter as tk
from tkinter import ttk
from Utils import Functions
from tkcalendar import DateEntry
class ProductRegistrationView(tk.Toplevel):
    def __init__(self, productRegistrationController, recipe_id=None):
        super().__init__(background="GhostWhite")
        self.recipe_id = recipe_id
        if recipe_id is not None:
            self.recipe_name = self.get_recipe_name_by_id(recipe_id)
        self.productRegistrationController = productRegistrationController
        self._windows_attributes()
        #product_id, supply_id, product_name, quantity, price, expiration_date, category, stock_level, flooring, celling
        self.product_labels_with_colspan = {
            "Product Name": 1,
            "Quantity": 1,
            "Category": 1,
            "Price": 1,
            "Expiry Date": 1,
            "Category": 1,
            "Flooring": 1,
            "Ceiling": 1,
            "Stock Level": 1
        }
        self.product_entry_boxes = []
        self.product_inputs = []
        self.product_categories = ["test1","test2","test3"] # Please change, this is just a placeholder
        self.product_stock_level = ["test1", "test2", "test3"] # Please change, this is just a placeholder
        self.mainBg = "Gray89"

    def main(self):
        self._product_entry_frame()
        self._product_widgets()
        self._product_register_button()
        self._back_button()
        self.mainloop()

    def _windows_attributes(self):
        self.h = 420
        self.w = 580
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        # Set's the title to a specific recipe_id if recipe_id is not None
        if self.recipe_id is not None:
            self.title(f'Product Registration | Recipe ID: {self.recipe_id}')
        else:
            self.title('Product Registration')


        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.quit())

    def _product_entry_frame(self):
        self.entryFrame = tk.Frame(self,background=self.mainBg,padx=40,pady=80)
        self.entryFrame.place(relx =0.5,rely=0.5,anchor='center')

    def _product_widgets(self):
        #product_id, supply_id, product_name, quantity, price, expiration_date, category, stock_level, flooring, celling
        subset_one = {key:self.product_labels_with_colspan[key] for key in ["Product Name","Quantity","Price"] if key in self.product_labels_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_one,
            entryList=self.product_entry_boxes,
            bgColor=self.mainBg,
            borderW=1,
            max_columns=2,
            side='e'
        )
        self._prodcut_expiry_date()
        self._product_category_dropdown()
        subset_two = {key:self.product_labels_with_colspan[key] for key in ["Flooring","Ceiling"] if key in self.product_labels_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_two,
            entryList=self.product_entry_boxes,
            shortEntryWidth=23,
            side='e',
            borderW=1,
            bgColor=self.mainBg,
            max_columns=2,
            current_r=4,
            current_c=0,
            #yPadding=15
        )


    def _prodcut_expiry_date(self):
        self.expiry_date_lbl = tk.Label(self.entryFrame,text="Expiry Date:",background=self.mainBg)
        self.expiry_date_lbl.grid(row=2,column=0,padx=2,pady=2,sticky='e')
        self.expiry_date = DateEntry(self.entryFrame,width=20,borderwidth=0,year=2000,date_pattern='YYYY-MM-DD')
        self.expiry_date.set_date(Functions.get_current_date())
        self.expiry_date.grid(row=2,column=1,padx=2,pady=2)
        
        self.product_entry_boxes.append(self.expiry_date)

    def _product_category_dropdown(self):
        category_lbl = tk.Label(self.entryFrame,text="Category: ",background=self.mainBg,anchor='e')
        category_lbl.grid(row=1,column=2,padx=1,pady=5,sticky='e')
        category_lbl.columnconfigure(2,weight=1)
        category = ttk.Combobox(self.entryFrame, values=self.product_categories)
        category.set("Select Category")
        category.grid(row=1, column=3, sticky='w', padx=1, pady=5)
        self.product_entry_boxes.append(category)

    def _product_register_button(self):
        register_btn = tk.Button(self.entryFrame, text="Register", command=lambda: self._checkInput(self.product_entry_boxes))
        register_btn.grid(row=6, column=2, sticky='w', padx=5, pady=5)

    def _checkInput(self, data: list):
        #product_id, supply_id, product_name, quantity, price, expiration_date, category, stock_level, flooring, celling
        product_inputs = []
        for entry in data:
            product_inputs.append(entry.get())
        self.productRegistrationController.register_product(product_inputs)


    def _back_button(self):
        back_btn = tk.Button(self.entryFrame, text="Back", command=self.quit)
        back_btn.grid(row=6, column=3, sticky='w', padx=5, pady=5) 

"""
HM or PM
if HM then
	recipe_id = recipe_name when creating
if recipe_name not equal in the database then
	return
else then
	popup register product
	pop title supposed to be HM or PM

on top of the pop is supposed to be the recipe ID

register button clicked:
	quantity * recipe ingredient > items in the database return to back to product registration
	then minus that to items on what are the items made
"""