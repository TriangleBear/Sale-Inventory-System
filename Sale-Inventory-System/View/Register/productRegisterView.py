import tkinter as tk
from tkinter import ttk,font,messagebox,CENTER
from Utils import Functions
from tkcalendar import DateEntry
from icecream import ic
class ProductRegisterView(tk.Toplevel):
    def __init__(self, productRegisterController, id=None,name=None):
        super().__init__(background="GhostWhite")
        self.id = id
        self.name = name
        self.productRegisterController = productRegisterController
        if id[0] =="R":
            self.state = "Recipe"
        if id[0] =="I":
            self.state = "Supply"
        self._windows_attributes()
        self.product_id = self.create_product_id()

        #product_id, image_id, user_id, product_name, quantity, price, exp_date, category, flooring, ceiling, stock_level
        self.product_labels_with_colspan = {
            "Quantity": 1,
            "Price/unit": 1,
            "Expiry Date": 1,
            "Menu Type": 1,
            "Flooring": 1,
            "Ceiling": 1,
            "Stock Level": 1
        }
        self.product_entry_boxes = []
        self.product_input = []
        self.product_categories = ["Breakfast","Lunch","Dinner","Desert","Drinks","Snacks"] # Please change, this is just a placeholder
        self.mainBg = "Gray89"

    def create_product_id(self):
        id = self.productRegisterController.check_existing_product(self.name)
        if not id:
            return self.productRegisterController.get_product_id()
        else:
            return id
    def main(self):
        self._product_entry_frame()
        self._product_id_frame()
        self._product_id_lbl()
        self._product_widgets()
        self._product_register_button(3,3)
        self._back_button(3,2)
        self.mainloop()

    def _windows_attributes(self):
        self.h = 420
        self.w = 580
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        # Set's the title to a specific recipe_id if recipe_id is not None
        if self.state == "Recipe":
            print(f'{self.id}')
            self.title(f'Product Registration | Recipe ID: {self.id}')
        elif self.state == "Supply":
            print(f'{self.id}')
            self.title(f'Product Registration | Supply ID: {self.id}')


        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.quit())

    def _product_entry_frame(self):
        self.entryFrame = tk.Frame(self,background=self.mainBg,padx=40,pady=80)
        self.entryFrame.place(relx =0.5,rely=0.5,anchor='center')
    
    def _product_id_frame(self):
        self.idFrame = tk.Frame(self,background=self.mainBg,width=580,height=40)
        self.idFrame.place(relx=0,rely=0)

    def _product_id_lbl(self):
        self.itemIdLbl = tk.Label(
            self.idFrame,
            font=font.Font(family='Courier New',size=14,weight='bold'),
            text=f"Product ID: {self.product_id} | Product Name: {self.name}",
            background=self.mainBg
        )
        self.itemIdLbl.place(relx=0.5,rely=0.5,anchor=CENTER)


    def _product_widgets(self):
        #product_id, supply_id, product_name, quantity, price, expiration_date, category, stock_level, flooring, celling
        subset_one = {key:self.product_labels_with_colspan[key] for key in ["Quantity","Price/unit"] if key in self.product_labels_with_colspan}
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
        self._prodcut_expiry_date(1,0)
        self._product_category_dropdown(1,2)
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
            current_r=2,
            current_c=0,
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
        register_btn = tk.Button(self.entryFrame, text="Register", command=lambda: self._checkInput(self.product_entry_boxes,self.state))
        register_btn.grid(row=current_r, column=current_c, sticky='w', padx=5, pady=5)

    def register_item(self,insufficientStock,product_inputs):
        if insufficientStock == 0:
            self.productRegisterController.register_product(product_inputs,self.product_id,self.name)
            self.productRegisterController.logUserActivity()
            messagebox.showinfo('Product Register', 'Product has been registered successfully!')
            self.destroy()
        else:
            messagebox.showerror("Product Registration", insufficientStock)
            return
    
    # def register_pre_made_item(self,insufficientStock,product_inputs):
    #     if insufficientStock == 0:
    #         self.productRegisterController.register_product(product_inputs,self.product_id,self.name)
    #         self.productRegisterController.logUserActivity()
    #         messagebox.showinfo('Product Register', 'Product has been registered successfully!')
    #         self.destroy()
    #     else:
    #         messagebox.showerror("Product Registration", insufficientStock)
    #         return

    def _checkInput(self, data:list,state:str):
        product_inputs = Functions.format_product_data(data=[entry.get() for entry in data])
        #"""product_id""", """image_id""", """user_id""", """product_name""", quantity, price, exp_date, category, flooring, ceiling, stock_level
        print(f'Product Inputs: {product_inputs}')
        incorrectInput = self.productRegisterController.verify_product_inputs(product_inputs)
        print("debug 1")
        ic(incorrectInput)
        ic(self.state)
        if incorrectInput == 0 and self.state == "Recipe":
            insufficientItem = self.productRegisterController.subtract_item_stock_level(self.id,product_inputs[0])
            print(f'Insufficient Item: {insufficientItem}')
            self.register_item(insufficientItem,product_inputs)
            return
        elif incorrectInput == 0 and self.state == "Supply":
            insufficientItem = self.productRegisterController.subtract_supply_stock_level(self.id,self.name,product_inputs[0])
            self.register_item(insufficientItem,product_inputs)
        else:
            messagebox.showerror("Product Registration", incorrectInput)
            return

    def _back_button(self,current_r=0,current_c=0):
        back_btn = tk.Button(self.entryFrame, text="Back", command=lambda:self.destroy())
        back_btn.grid(row=current_r, column=current_c, sticky='e', padx=5, pady=5)