import tkinter as tk
from Utils import Functions
from tkcalendar import DateEntry
class ProductRegistrationView(tk.Toplevel):
    def __init__(self, productRegistrationController):
        super().__init__(background="GhostWhite")
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
            "Stock Level": 1,
            "Flooring": 1,
            "Ceiling": 1
        }
        self.product_entry_boxes = []
        self.product_inputs = []
        self.product_categories = ["test1","test2","test3"] # Please change, this is just a placeholder
        self.product_stock_level = ["test1", "test2", "test3"] # Please change, this is just a placeholder
        self.mainBg = "Gray89"

    def main(self):
        self._header_frame()
        self._base_frame()
        self._entry_frame()
        self._product_widgets()
        self._register_button()
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

    def _header_frame(self):
        self.headerFrame = tk.Frame(self,background=self.mainBg)
        self.headerFrame.place(x=0,y=0,width=self.w,height=30)

    def _base_frame(self):
        self.baseFrame = tk.Frame(self, background=self.mainBg)
        self.baseFrame.place(x=15, y=43, width=self.w-30, height=370)

    def _entry_frame(self):
        self.entryFrame = tk.Frame(self.baseFrame,background=self.mainBg,padx=40,pady=80)
        self.entryFrame.place(relx =0.5,rely=0.5,anchor='center')

    def _product_widgets(self):
        #product_id, supply_id, product_name, quantity, price, expiration_date, category, stock_level, flooring, celling
        subset_one = {key:self.product_labels_with_colspan[key] for key in ["Product Name","Quantity","Price"] if key in self.product_labels_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_one,
            entryList=self.product_entry_boxes,
            shortEntryWidth=23,
            side='e',
            borderW=1,
            bgColor=self.mainBg,
            max_columns=1,
            #yPadding=15
        )
        self._prodcut_expiry_date()
        self._product_stock_level_dropdown()
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
            max_columns=1,
            #yPadding=15
        )


    def _prodcut_expiry_date(self):
        expiry_date = DateEntry(self.entryFrame, width=20, background=self.mainBg, borderwidth=1)
        expiry_date.grid(row=3, column=1, sticky='w', padx=5, pady=5)
        self.product_entry_boxes.append(expiry_date)

    def _product_category_dropdown(self):
        category = tk.StringVar(self.entryFrame)
        category.set(self.product_stock_level[0])
        category_dropdown = tk.OptionMenu(self.entryFrame, category, *self.product_stock_level)
        category_dropdown.grid(row=3, column=1, sticky='w', padx=5, pady=5)
        self.product_entry_boxes.append(category_dropdown)

    def _product_stock_level_dropdown(self):
        stock_level = tk.StringVar(self.entryFrame)
        stock_level.set(self.product_categories[0])
        stock_level_dropdown = tk.OptionMenu(self.entryFrame, stock_level, *self.product_categories)
        stock_level_dropdown.grid(row=2, column=1, sticky='w', padx=5, pady=5)
        self.product_entry_boxes.append(stock_level_dropdown)

    def _register_button(self):
        register_btn = tk.Button(self.entryFrame, text="Register", command=lambda: self._checkInput(self.product_entry_boxes))
        register_btn.grid(row=5, column=1, sticky='w', padx=5, pady=5)

    def _checkInput(self, data: list):
        #product_id, supply_id, product_name, quantity, price, expiration_date, category, stock_level, flooring, celling
        product_inputs = []
        for entry in data:
            product_inputs.append(entry.get())
        self.productRegistrationController.register_product(product_inputs)

    def _back_button(self):
        back_btn = tk.Button(self.entryFrame, text="Back", command=self.quit)
        back_btn.grid(row=5, column=0, sticky='w', padx=5, pady=5) 