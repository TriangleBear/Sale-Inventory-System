import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter import font, CENTER
from Utils import Functions
from textwrap import dedent
import os
from icecream import ic

class SuppliesView(tk.Frame):
    def __init__(self, suppliesController, master):
        self.master = master
        self.mainBg = "Grey89"
        super().__init__(self.master, background=self.mainBg)
        self.suppliesController = suppliesController
        self.supplies_btn_lbls = ["Reorder", "Order Supplies"]
        self.btns = []  # Initialize btns before calling self.main()
        self.pack(fill=tk.BOTH, expand=True)
        self.table_product = ['ID', 'Product Name', 'Current Quantity', 'Stock Level']
        self.table_cart = ['ID', 'Product Name', 'Quantity to Add', 'Expected Payment']
        self.entry_lbls = {'ID': 1,
                           'Product Name': 1,
                           'Current Quantity': 1,
                           'Quantity to Add': 1}
        self.reorder_entry_boxes = []
        self.reorder_items = []
        self.main()

    def main(self):
        self._button_reorder_frame()
        self._supplies_buttons()
        self._fetch_button()
        self._cart_label()
        self._display_cart_table()
        self._display_product_table()

    def _button_reorder_frame(self):
        self.headerFrame = tk.Frame(self, background=self.mainBg)
        self.headerFrame.place(relx=0.01, rely=0.05, anchor='nw')

    def _supplies_buttons(self):
        Functions.create_buttons_using_grid(
            self.headerFrame,
            labels=self.supplies_btn_lbls,
            entryList=self.btns,
            max_columns=2,
            w=21,
            h=1,
            fontSize=12,
            gridxPadding=2,
            gridyPadding=3,
            btnyPadding=2,
            btnxPadding=2,
            cmd=self._supplies_button_commands
        )

    def _cart_label(self):
        self.cart = tk.Label(self, font=font.Font(family='Courier New', size=14, weight='bold'),
                             text="Reorder Items", background=self.mainBg)
        self.cart.place(relx=0.75, rely=0.06, anchor=CENTER)

    def _display_product_table(self):
        self.tree_product = ttk.Treeview(self, 
                                         columns=self.table_product, 
                                         show='headings', 
                                         selectmode='browse')
        for col in self.table_product:
            self.tree_product.heading(col, text=col)
            self.tree_product.column(col, anchor='e')

        self.tree_product.bind("<Configure>", Functions.adjust_column_widths)
        self.tree_product.place(relx=0.01, rely=0.52, anchor='w', width=350, height=450)
        self._load_reorder_items()

    def _display_cart_table(self):
        Functions.treeview_style(self.mainBg)
        self.tree_cart = ttk.Treeview(
            self, columns=self.table_cart,
            show='headings',
            style="Custom.Treeview",
            selectmode='browse'
        )
        for col in self.table_cart:
            self.tree_cart.heading(col, text=col)
            self.tree_cart.column(col, anchor='e')
        self.tree_cart.bind("<Configure>", Functions.adjust_column_widths)
        self.tree_cart.place(relx=0.975, rely=0.53, anchor='e', width=440, height=450)

    def _load_reorder_items(self):
        self.tree_product.delete(*self.tree_product.get_children())
        reorder_items = Functions.convert_dicc_data(self.suppliesController.fetch_items_below_or_equal_flooring())
        print(reorder_items)
        self._insert_data(self.tree_product, reorder_items)
        reorder_supplies = Functions.convert_dicc_data(self.suppliesController.fetch_supply_below_or_equal_flooring())
        print("Reorder Supplies:", reorder_supplies)
        self._insert_data(self.tree_product, reorder_supplies)

    def _insert_data(self, tree: ttk.Treeview, data: list):
        for item in data:
            tree.insert('', 0, values=item)

    def _reorder_button(self):
        reorder_btn = tk.Button(self, font=font.Font(family='Courier New', size=12, weight='bold'),
                                padx=100, pady=2, text="Reorder", command=self._reorder)
        reorder_btn.place(relx=0.95, rely=0.97, anchor='se')

    def _fetch_button(self):
        fetch_btn = tk.Button(self, font=font.Font(family='Courier New', size=12, weight='bold'),
                              padx=100, pady=2, text="Fetch", command=self._load_reorder_items)
        fetch_btn.place(relx=0.60, rely=0.97, anchor='se')

    def _supplies_button_commands(self, btn):
        if btn == "Reorder":
            selected_item = self.tree_product.selection()
            print(f"Selected item: {selected_item}")  # Debugging statement
            if not selected_item:
                return messagebox.showerror("Error", "Please select an item to reorder")
            self._add_to_cart(selected_item)
        if btn == "Order Supplies":
            self._reorder()

    def _add_to_cart(self, selected_item):
        for i in selected_item:
            item = self.tree_product.item(i)['values']
            print(f'Item: {item}')  # Debugging statement
            item_id = item[0]
            product_name = item[1]
            quantity_to_add = simpledialog.askinteger("Add Quantity", f"How much of {product_name} to add?", parent=self, minvalue=1)
            expected_payment = simpledialog.askfloat("Expected Payment", f"Enter the expected payment for {product_name}", parent=self, minvalue=0.0)

            if quantity_to_add is not None and expected_payment is not None:
                new_values = (item_id, product_name, quantity_to_add, expected_payment)
                self.tree_cart.insert('', 'end', values=new_values)
                self.reorder_items.append((item_id, product_name, quantity_to_add, expected_payment))

    def _reorder(self):
        if not self.reorder_items:
            return messagebox.showerror("Reorder Error", "No items selected for reorder.")
        
        for item in self.reorder_items:
            item_id, item_name, quantity_to_add, expected_payment = item
            table_name_or_type = self.suppliesController.get_item_type_by_id(item_id)
            print(f'Table name or type: {table_name_or_type}')

            if table_name_or_type == "Supply":
                self.suppliesController.update_supply_quantity_in_database(item_name, quantity_to_add)
            elif table_name_or_type == "Items":
                self.suppliesController.update_item_quantity_in_database(item_name, quantity_to_add)

        if self.generate_invoice(supply_items=self.reorder_items, refNo=self.reorder_items[0], datetime=Functions.get_current_date('datetime'), total_sales=sum([item[3] for item in self.reorder_items])):
            messagebox.showinfo("Reorder", "Reorder successful. Inventory updated.")
            self.tree_cart.delete(*self.tree_cart.get_children())
            self.reorder_items.clear()
            self._load_reorder_items()

    # def fetch_data_from_supplies(self):
    #     suppliesData = []
    #     for items in self.tree_cart.get_children():
    #         suppliesData.append(self.tree_cart.item(items)['values'])
    #     return suppliesData

    def generate_invoice(self, supply_items, refNo, datetime, total_sales):
        ic(supply_items)
        if not supply_items:
            messagebox.showwarning("No Items", "No items to generate invoice.")
            return
        width = 35
        currency = 'Php'
        shop_name = "TAPSI NI VIVIAN"
        disclaimer = "THIS DOCUMENT IS NOT VALID \nFOR CALIM OF INPUT TAX"

        items = [
            shop_name.center(width),
            str(refNo).center(width),
            str(datetime).center(width),
            currency.rjust(width)
        ]
        for supply_id, name, count, price in supply_items:
            price /= count
            all_price = str(round(price*count,2))
            msg = f'{name}'.ljust(width-len(all_price))+all_price

            if type(count) is int and count >=2:
                msg += f'\n     {count} x {price}'
            elif type(count) is float:
                msg += f'\n     {count} x {price}'
            items.append(msg)

        total= str(round(total_sales,2))
        items.append(("-"*width).center(width))
        items.append("TOTAL:".ljust(width-len(total))+total)
        items.append(("-"*width).center(width))
        items.append(disclaimer.center(width))
        receipt_text = '\n'.join(items)
        

        if not os.path.exists("Sale-Inventory-System/Receipts"):
            os.makedirs("Sale-Inventory-System/Receipts")

        path = os.path.join("Sale-Inventory-System/Receipts", f"{refNo}.txt")

        with open(path, "w") as file:
            file.write(receipt_text)

        messagebox.showinfo("Invoice Generated", receipt_text)
        return

