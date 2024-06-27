import tkinter as tk
from Utils import Functions
from tkcalendar import DateEntry
class ProductRegistrationView(tk.Toplevel):
    def __init__(self, productRegistrationController):
        super().__init__(background="GhostWhite")
        self.productRegistrationController = productRegistrationController
        self.productRegistrationController.set_product_registration_view(self)
        self._windows_attributes()
        #product_id, supply_id, product_name, quantity, price, expiration_date, category, stock_level, flooring, celling
        self.register_labels_with_colspan = {
            "Product Name": 1,
            "Quantity": 1,
            "Category": 1,
            "Price": 1,
            "Expiry Date": 1,
            "Category": 1,
            "Stock Level": 1,
            "Flooring": 1,
            "Ceiling": 1
        }
        self.product_entry_boxes = []
        self.product_inputs = []
        self.mainBg = "Gray89"

    def main(self):
        self._product_frame()
        self._entry_frame()
        self._product_widgets()
        self._product_button()
        self._back_button()
        self.mainloop()

    def _windows_attributes(self):
        self.h = 420
        self.w = 580
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        self.title('Product Registration')
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.quit())

    def _product_frame(self):
        self.registerFrame = tk.Frame(self, background=self.mainBg, padx=40, pady=80)
        self.registerFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def _entry_frame(self):
        self.entryFrame = tk.Frame(self.registerFrame, background=self.mainBg)
        self.entryFrame.grid(row=1, column=0, columnspan=3, pady=10)

    def _product_widgets(self):
        for label, colspan in self.register_labels_with_colspan.items():
            self._product_label(label, colspan)
            self._product_entry(colspan)
        subset_one = {key: self.register_labels_with_colspan[key] for key in ["Product Name",
            "Quantity","Category","Price"] if key in self.register_labels_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_one,
            entry_boxes=self.product_entry_boxes,
            entry_width=23,
            entry_font_size=10
        )
        self._expiry_date_entry()
        self._category_dropdown()
        self._stock_level_dropdown()
        subset_two = {key: self.register_labels_with_colspan[key] for key in ["Flooring","Ceiling"] if key in self.register_labels_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_two,
            entry_boxes=self.product_entry_boxes,
            entry_width=23,
            entry_font_size=10
        )

    def _expiry_date_entry(self):
        self.expiry_date_lbl = tk.Label(self.entryFrame, text="Expiry Date:", background=self.mainBg)
        self.expiry_date_lbl.grid(row=4, column=0, padx=2, pady=2, sticky='e')

        self.expiry_date = DateEntry(self.registerFrame,width=20,borderwidth=0,year=2000,date_pattern='YYYY-MM-DD')
        self.expiry_date.set_date(Functions.get_current_date())
        self.expiry_date.grid(row=2,column=1,padx=2,pady=2)

    def _category_dropdown(self):
        self.category_lbl = tk.Label(self.entryFrame, text="Category:", background=self.mainBg)
        self.category_lbl.grid(row=2, column=2, padx=2, pady=2, sticky='e')

        self.category = tk.StringVar()
        self.category.set("Select Category")
        self.category_dropdown = tk.OptionMenu(self.entryFrame, self.category, "Unknown") #add more categories
        self.category_dropdown.config(width=20, font=("Arial", 10))
        self.category_dropdown.grid(row=2, column=3, padx=2, pady=2)

    def _stock_level_dropdown(self):
        self.stock_level_lbl = tk.Label(self.entryFrame, text="Stock Level:", background=self.mainBg)
        self.stock_level_lbl.grid(row=3, column=2, padx=2, pady=2, sticky='e')

        self.stock_level = tk.StringVar()
        self.stock_level.set("Select Stock Level")
        self.stock_level_dropdown = tk.OptionMenu(self.entryFrame, self.stock_level, "medium", "low", "high")

    def _register_button(self):
        register_btn = tk.Button(self.registerFrame, text="Register", command=lambda: self._checkInput(self.product_entry_boxes))
        register_btn.grid(row=5, column=3, sticky='w', padx=5, pady=5)

    def _checkInput(self, data: list):
        #product_id, supply_id, product_name, quantity, price, expiration_date, category, stock_level, flooring, celling
        product_inputs = []
        for entry in data:
            product_inputs.append(entry.get())
        self.productRegistrationController.register_product(product_inputs)

    def _back_button(self):
        back_btn = tk.Button(self.registerFrame, text="Back", command=self.quit)
        back_btn.grid(row=5, column=0, sticky='w', padx=5, pady=5)