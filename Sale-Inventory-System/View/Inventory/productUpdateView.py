import tkinter as tk
from tkinter import ttk, messagebox, font, CENTER
from tkcalendar import DateEntry
from Utils import Functions
from icecream import ic

class ProductUpdateView(tk.Toplevel):
    def __init__(self, productUpdateController, product_data):
        self.mainBg = 'Gray89'
        self.product_data = product_data
        super().__init__()
        self.productUpdateController = productUpdateController
        self.product_id = product_data[0]
        self.product_name = product_data[2]
        self.current_quantity = product_data[3]
        if self.product_id[1] == 'R':
            self.state = 'receipe'
        if self.product_id[1] == 'S':
            self.status = "supply"
        self._window_attributes()

        self.product_lbls_with_colspan = {
            "Product Name": 1,
            "Quantity": 1,
            "Price": 1,
            "Expiry Date": 1,
            "Category": 1,
            "Flooring": 1,
            "Ceiling": 1
        }
        self.category = ["Breakfast", "Lunch", "Dinner", "Snack", "Dessert"]
        self.product_entry_boxes = []

    def main(self):
        self._product_id_frame()
        self._product_id_lbl()
        self._product_entry_frame()
        self._product_register_widgets()
        self._insert_into_entry_boxes(self.product_entry_boxes,self.product_data[3:9])
        self._update_product_button(4,3)
        self._back_button(4,2)
        self.mainloop()

    def _window_attributes(self):
        self.h = 420
        self.w = 580
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        self.title('Update Recipe')
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.quit())

    def _product_entry_frame(self):
        self.entryFrame = tk.Frame(self, background=self.mainBg, padx=20, pady=80)
        self.entryFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def _product_id_frame(self):
        self.idFrame = tk.Frame(self, background=self.mainBg, width=580, height=40)
        self.idFrame.place(relx=0, rely=0)

    def _product_id_lbl(self):
        self.productIdLbl = tk.Label(self.idFrame, font=font.Font(family='Courier New', size=14, weight='bold'),
                                     text=f"Product ID:{self.product_id} | Product Name:{self.product_name}", background=self.mainBg)
        self.productIdLbl.place(relx=0.5, rely=0.5, anchor=CENTER)

    def _product_register_widgets(self):
        entrywidth = 23
        subset_one = {key: self.product_lbls_with_colspan[key] for key in ["Quantity", "Price"] if key in self.product_lbls_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_one,
            bgColor=self.mainBg,
            entryList=self.product_entry_boxes,
            borderW=1,
            max_columns=2,
            shortEntryWidth=entrywidth,
            side='e'
        )
        self._expiry_date_entry(1, 0)
        self._category_dropdown(1, 2)

        subset_two = {key: self.product_lbls_with_colspan[key] for key in ["Flooring", "Ceiling"] if key in self.product_lbls_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_two,
            bgColor=self.mainBg,
            entryList=self.product_entry_boxes,
            borderW=1,
            max_columns=2,
            current_r=2,
            current_c=0,
            shortEntryWidth=entrywidth,
            side='e'
        )

    def _insert_into_entry_boxes(self, entryData, list_to_insert):
        ic(entryData)
        ic(list_to_insert)
        for i, entry in enumerate(entryData):
            data_to_insert = list_to_insert[i]
            if isinstance(entry, ttk.Combobox):
                entry.set(data_to_insert)
            if isinstance(entry, DateEntry):
                ic(entry)
                ic(data_to_insert)
                entry.set_date(data_to_insert)
            try:
                entry.delete(0, 'end')
                entry.insert(0, data_to_insert)
            except AttributeError:
                print(f"Error: The widget {type(entry)} does not support delete/insert methods.")

    def _category_dropdown(self, current_r=0, current_c=0):
        categoryLbl = tk.Label(self.entryFrame,text="Category:", background=self.mainBg,anchor='e')
        categoryLbl.grid(row=current_r, column=current_c,padx=1,pady=5,sticky='e')
        categoryBox = ttk.Combobox(self.entryFrame, values=self.category)
        categoryBox.grid(row=current_r, column=current_c + 1,padx=5,pady=5)
        categoryBox.set(self.category[0])
        self.product_entry_boxes.append(categoryBox)

    def _expiry_date_entry(self, current_r=0, current_c=0):
        expiryLbl = tk.Label(self.entryFrame,text="Expiry Date:", background=self.mainBg)
        expiryLbl.grid(row=current_r, column=current_c,padx=2,pady=2,sticky='e')
        expiryBox = DateEntry(self.entryFrame, width=20, background=self.mainBg,date_pattern='YYYY-MM-DD')
        expiryBox.grid(row=current_r, column=current_c + 1,padx=2,pady=2)
        self.product_entry_boxes.append(expiryBox)

    def update_item(self,insufficientStock,product_inputs):
        if insufficientStock == 0:
            self.productRegisterController.register_product(product_inputs,self.product_id,self.name)
            self.productRegisterController.logUserActivity()
            messagebox.showinfo('Product Register', 'Product has been registered successfully!')
            self.destroy()
        else:
            messagebox.showerror("Product Registration", insufficientStock)
            return

    def _checkInput(self, data: list):
        # product name, quantity, price, expiry date, category, flooring, ceiling
        entryData = Functions.format_product_data(data=[entry.get().strip() for entry in data])
        entryData.append(self.product_id)
        check_input = Functions.check_product_input(entryData,self.status)
        if check_input == 0:
            self.productUpdateController.update_product(entryData,self.status)
            self.productUpdateController.logUserActivity()
            messagebox.showinfo("Success", "Product Updated Successfully!")
            self.destroy()
        else:
            messagebox.showerror("Product Update Error", check_input)

    def _checkInput(self, data:list,state:str):
        product_inputs = Functions.format_product_data(data=[entry.get() for entry in data])
        #"""product_id""", """image_id""", """user_id""", """product_name""", quantity, price, exp_date, category, flooring, ceiling, stock_level
        print(f'Product Inputs: {product_inputs}')
        incorrectInput = self.productUpdateController.verify_product_inputs(product_inputs)
        ic(incorrectInput)
        ic(self.state)
        if incorrectInput == 0 and self.state == "Recipe":
            subtract_quantity = self.productUpdateController.added_subtracted_new_quantity(self.product_name,product_inputs[0],self.current_quantity)
            insufficientItem = self.productRegisterController.subtract_item_stock_level(self.product_name,subtract_quantity)
            print(f'Insufficient Item: {insufficientItem}')
            self.update_item(insufficientItem,product_inputs)
            return
        elif incorrectInput == 0 and self.state == "Supply":
            insufficientItem = self.productRegisterController.subtract_supply_stock_level(self.id,self.name,product_inputs[0])
            self.register_item(insufficientItem,product_inputs)
        else:
            messagebox.showerror("Product Registration", incorrectInput)
            return

    def _update_product_button(self, current_r=0, current_c=0):
        updateBtn = tk.Button(self.entryFrame, font=font.Font(family='Courier New', size=9, weight='bold'),
                              text="Update", command=lambda: self._checkInput(self.product_entry_boxes))
        updateBtn.grid(row=current_r,column=current_c,sticky='w',padx=5,pady=5)

    def _back_button(self,current_r=0,current_c=0):
        backBtn = tk.Button(self.entryFrame, text="Back", font=font.Font(family='Courier New', size=9, weight='bold'), command=lambda:self.destroy())
        backBtn.grid(row=current_r, column=current_c, sticky='e',padx=5,pady=5)
