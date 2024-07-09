import tkinter as tk
from tkinter import ttk, messagebox, font, CENTER
from tkcalendar import DateEntry
from Utils import Functions

class ProductUpdateView(tk.Toplevel):
    def __init__(self, productUpdateController, product_data):
        self.mainBg = 'Gray89'
        super().__init__(self.master, background=self.mainBg)
        self.productUpdateController = productUpdateController
        self.product_id = product_data[0]
        self.status = "Products"
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

        self.main()  # Call main to set up the UI

    def main(self):
        self._product_id_frame()
        self._product_id_lbl()
        self._product_entry_frame()
        self._product_register_widgets()
        self._update_product_button()  # Added this missing call
        self._back_button()

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
                                     text=f"Product ID: {self.product_id}", background=self.mainBg)
        self.productIdLbl.place(relx=0.5, rely=0.5, anchor=CENTER)

    def _product_register_widgets(self):
        entrywidth = 23
        subset_one = {key: self.product_lbls_with_colspan[key] for key in ["Product Name", "Quantity", "Price"] if key in self.product_lbls_with_colspan}
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
        self._expiry_date_entry(2, 0)
        self._category_dropdown(2, 1)

        subset_two = {key: self.product_lbls_with_colspan[key] for key in ["Flooring", "Ceiling"] if key in self.product_lbls_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_two,
            bgColor=self.mainBg,
            entryList=self.product_entry_boxes,
            borderW=1,
            max_columns=2,
            current_r=3,
            current_c=0,
            shortEntryWidth=entrywidth,
            side='e'
        )

    def _insert_into_entry_boxes(self, entryData, list_to_insert):
        for i, entry in enumerate(entryData):
            data_to_insert = list_to_insert[i]
            if isinstance(entry, ttk.Combobox):
                entry.set(data_to_insert)
            if isinstance(entry, DateEntry):
                entry.set_date(data_to_insert)
            try:
                entry.delete(0, 'end')
                entry.insert(0, data_to_insert)
            except AttributeError:
                print(f"Error: The widget {type(entry)} does not support delete/insert methods.")

    def _category_dropdown(self, current_r=0, current_c=0):
        categoryLbl = tk.Label(self.entryFrame, font=font.Font(family='Courier New', size=14, weight='bold'),
                               text="Category:", background=self.mainBg)
        categoryLbl.grid(row=current_r, column=current_c, sticky='w')
        categoryBox = ttk.Combobox(self.entryFrame, values=self.category)
        categoryBox.grid(row=current_r, column=current_c + 1, sticky='w')
        categoryBox.set(self.category[0])
        self.product_entry_boxes.append(categoryBox)

    def _expiry_date_entry(self, current_r=0, current_c=0):
        expiryLbl = tk.Label(self.entryFrame, font=font.Font(family='Courier New', size=14, weight='bold'),
                             text="Expiry Date:", background=self.mainBg)
        expiryLbl.grid(row=current_r, column=current_c, sticky='w')
        expiryBox = DateEntry(self.entryFrame, width=20, background=self.mainBg)
        expiryBox.grid(row=current_r, column=current_c + 1, sticky='w')
        self.product_entry_boxes.append(expiryBox)

    def _update_product_button(self, current_r=0, current_c=0, status=None):
        updateBtn = tk.Button(self.entryFrame, text="Update Product", font=font.Font(family='Courier New', size=12, weight='bold'),
                              background=self.mainBg, command=lambda: self._checkInput(self.product_entry_boxes))
        updateBtn.grid(row=current_r,column=current_c,sticky='w',padx=5,pady=5)

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

    def _back_button(self):
        backBtn = tk.Button(self.entryFrame, text="Back", font=font.Font(family='Courier New', size=12, weight='bold'),
                            background=self.mainBg, command=self.destroy)
        backBtn.grid(row=3, column=2, columnspan=2, sticky='w')
