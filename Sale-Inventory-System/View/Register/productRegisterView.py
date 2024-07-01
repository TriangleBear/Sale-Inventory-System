import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Utils import Functions
from tkcalendar import DateEntry
class ProductRegisterView(tk.Toplevel):
    def __init__(self, productRegisterController, recipe_id=None):
        super().__init__(background="GhostWhite")
        self.recipe_id = recipe_id
        self.productRegisterController = productRegisterController
        if recipe_id is not None:
            self.recipe_name = self.productRegisterController.get_recipe_name_by_id(recipe_id)
        self._windows_attributes()
        #product_id, image_id, user_id, product_name, quantity, price, exp_date, category, flooring, ceiling, stock_level
        self.product_labels_with_colspan = {
            "Product Name": 1,
            "Quantity": 1,
            "Price/unit": 1,
            "Expiry Date": 1,
            "Category": 1,
            "Flooring": 1,
            "Ceiling": 1,
            "Stock Level": 1
        }
        self.product_entry_boxes = []
        self.product_input = []
        self.product_categories = ["Breakfast","Lunch","Dinner","Desert","Drinks","Snacks"] # Please change, this is just a placeholder
        self.mainBg = "Gray89"

    def main(self):
        self._product_entry_frame()
        self._product_widgets()
        self._product_register_button(6,3)
        self._back_button(6,2)
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
            print(f'{self.recipe_id}')
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
        subset_one = {key:self.product_labels_with_colspan[key] for key in ["Product Name","Quantity","Price/unit"] if key in self.product_labels_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_one,
            entryList=self.product_entry_boxes,
            bgColor=self.mainBg,
            borderW=1,
            max_columns=2,
            shortEntryWidth=23,
            side='e'
        )
        self._prodcut_expiry_date(1,2)
        self._product_category_dropdown(2,0)
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
            current_r=3,
            current_c=0,
            #yPadding=15
        )


    def _prodcut_expiry_date(self,current_r=0,current_c=0):
        self.expiry_date_lbl = tk.Label(self.entryFrame,text="Expiry Date:",background=self.mainBg)
        self.expiry_date_lbl.grid(row=current_r,column=current_c,padx=2,pady=2,sticky='e')
        self.expiry_date = DateEntry(self.entryFrame,width=20,borderwidth=0,year=2000,date_pattern='YYYY-MM-DD')
        self.expiry_date.set_date(Functions.get_current_date())
        self.expiry_date.grid(row=current_r,column=current_c+1,padx=2,pady=2)
        self.product_entry_boxes.append(self.expiry_date)

    def _product_category_dropdown(self,current_r=0,current_c=0):
        category_lbl = tk.Label(self.entryFrame,text="Category: ",background=self.mainBg,anchor='e')
        category_lbl.grid(row=current_r,column=current_c,padx=1,pady=5,sticky='e')
        category_lbl.columnconfigure(2,weight=1)
        category = ttk.Combobox(self.entryFrame, values=self.product_categories,width=20)
        category.set("Select Category")
        category.grid(row=current_r, column=current_c+1, padx=1, pady=5)
        self.product_entry_boxes.append(category)

    def _product_register_button(self,current_r=0,current_c=0):
        register_btn = tk.Button(self.entryFrame, text="Register", command=lambda: self._checkInput(self.product_entry_boxes))
        register_btn.grid(row=current_r, column=current_c, sticky='w', padx=5, pady=5)

    def register_item(self,stock_level,product_inputs):
        if stock_level == 0:
            self.productRegisterController.register_product(product_inputs)
            messagebox.showinfo('Product Register', 'Product has been registered successfully!')
        else:
            messagebox.showerror("Product Registration", stock_level)
            return
        

    def _checkInput(self, data:list):
        product_inputs = [entry.get() for entry in data]
        #"""product_id""", """image_id""", """user_id""", product_name, quantity, price, exp_date, category, flooring, ceiling, stock_level
        print(f'Product Inputs: {product_inputs}')
        incorrectInput = self.productRegisterController.verify_product_inputs(product_inputs)
        if incorrectInput == 0:
            insufficientItem = self.productRegisterController.subtract_stock_level(self.recipe_id,product_inputs[1])
            print(f'Insufficient Item: {insufficientItem}')
            self.register_item(insufficientItem,product_inputs)
            return
        else:
            messagebox.showerror("Product Registration", incorrectInput)
            return


    def _back_button(self,current_r=0,current_c=0):
        back_btn = tk.Button(self.entryFrame, text="Back", command=lambda:self.destroy())
        back_btn.grid(row=current_r, column=current_c, sticky='e', padx=5, pady=5) 

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
	quantity product * recipe ingredient > items in the database return to back to product registration
	then minus that to items on what are the items made
"""