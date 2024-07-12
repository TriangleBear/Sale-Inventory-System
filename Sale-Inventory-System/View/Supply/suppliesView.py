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
        self.supplies_btn_lbls = ["Refresh", "Reorder","Order Supplies"]
        self.btns = []  # Initialize btns before calling self.main()
        self.pack(fill=tk.BOTH, expand=True)
        self.table_product = ['ID', 'Product Name', 'Current Quantity', 'Stock Level']
        self.table_cart = ['ID', 'Product Name', 'Quantity Order', 'Payment','Arrival']
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
        self._items_label()
        self._cart_label()
        self._back_btn()
        self._display_cart_table()
        self._display_product_table()

    def _button_reorder_frame(self):
        self.btnFrame = tk.Frame(self, background=self.mainBg,width=800)
        self.btnFrame.place(relx=0.99, rely=0.96, anchor='se')

    def _supplies_buttons(self):
        Functions.create_buttons_using_grid(
            self.btnFrame,
            labels=self.supplies_btn_lbls,
            entryList=self.btns,
            max_columns=4,
            w=15,
            h=1,
            fontSize=12,
            gridxPadding=6,
            gridyPadding=3,
            btnyPadding=2,
            cmd=self._supplies_button_commands
        )
    def _items_label(self):
        self.items = tk.Label(self,font=font.Font(family='Courier New',size=14,weight='bold'),text=f"Low Stock Items",background=self.mainBg)
        self.items.place(relx=0.23,rely=0.06,anchor='n')

    def _cart_label(self):
        self.cart = tk.Label(self,font=font.Font(family='Courier New',size=14,weight='bold'),text=f"Cart",background=self.mainBg)
        self.cart.place(relx=0.73,rely=0.06,anchor='n')

    def _back_btn(self):
        self.back_btn = tk.Button(self,font=font.Font(family='Courier New',size=9,weight='bold'), 
                                  text="Back", background="Grey89",command=lambda:self.suppliesController.suppliesPage())
        self.back_btn.place(relx=0.09,rely=0.954,anchor='s')


    def _display_product_table(self):
        Functions.treeview_style(self.mainBg)
        self.tree_product = ttk.Treeview(self, 
                                         columns=self.table_product, 
                                         show='headings', 
                                         selectmode='browse')
        for col in self.table_product:
            self.tree_product.heading(col, text=col)
            self.tree_product.column(col, anchor='e')
        self.tree_product.bind("<Configure>", Functions.adjust_column_widths)
        self.tree_product.place(relx=0.015, rely=0.49, anchor='w', width=350, height=450)
        self._load_reorder_items()

    def _display_cart_table(self):
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
        self.tree_cart.place(relx=0.98, rely=0.49, anchor='e', width=440, height=450)    

    def _supplies_button_commands(self, btn):
        if btn == "Reorder":
            selected_item = self.tree_product.item(self.tree_product.selection()[0],'values')
            if not selected_item:
                return messagebox.showerror("Error", "Please select an item to reorder")
            # self._add_to_cart(selected_item)
            self.suppliesController.reorderController(selected_item)
        if btn == "Refresh":
            self._load_reorder_items()
        if btn == "Order Supplies" and not self.tree_cart.get_children():
            return messagebox.showerror("Error", "Please select an item to reorder")
        if btn == "Order Supplies" and self.tree_cart.get_children():
            self._reorder()

    def _load_reorder_items(self):
        self.tree_product.delete(*self.tree_product.get_children())
        reorder_items = Functions.convert_dicc_data(self.suppliesController.fetch_items_below_or_equal_flooring())
        reorder_supplies = Functions.convert_dicc_data(self.suppliesController.fetch_supply_below_or_equal_flooring())
        self._insert_data(self.tree_product, reorder_items)
        self._insert_data(self.tree_product, reorder_supplies)

    def add_to_cart(self, selected_item):
        for iid in self.tree_cart.get_children():
            existingItem = Functions.check_cart_item(
                insertData=selected_item,
                insertedData=self.tree_cart.item(iid,'values')
            )
            if existingItem == None:
                continue
            if type(existingItem) == list:
                self.tree_cart.item(iid,values=existingItem)
                return
        self._insert_data(self.tree_cart,[[selected_item[3],selected_item[4],*selected_item[0:3]]])
        

    def _reorder(self):
        datetime = Functions.get_current_date("datetime")
        if self.tree_cart.get_children():
            cart_items = []
            for child in self.tree_cart.get_children():
                formattedData = [*Functions.format_item_order(*self.tree_cart.item(child, 'values'))]
                formattedData.append(datetime)
                formattedData.append("Pending")
                cart_items.append(formattedData)
        self.suppliesController.reorder(cart_items)
        self.suppliesController.logUserActivity()
        self.generate_invoice(supply_items=cart_items,refNo="1",datetime=datetime)
        self.tree_cart.delete(*self.tree_cart.get_children())
        return

    def _insert_data(self, tree: ttk.Treeview, data: list):
        for item in data:
            tree.insert('', 0, values=item)

    def generate_invoice(self, supply_items, refNo, datetime):
        if not supply_items:
            messagebox.showwarning("No Items", "No items to generate invoice.")
            return
        width = 35
        currency = 'Php'
        shop_name = "TAPSI NI VIVIAN"
        disclaimer = "THIS DOCUMENT IS NOT VALID \nFOR CALIM OF INPUT TAX"

        total = 0
        items = [
            shop_name.center(width),
            str(refNo).center(width),
            str(datetime).center(width),
            currency.rjust(width)
        ]
        ic(supply_items)
        for id,name,count,price,arrival,ordered_on,status in supply_items:
            total += price*float(count)
            all_price = str(round(price*float(count),2))
            msg = f'{name}'.ljust(width-len(all_price))+all_price

            if type(count) is int and count >=2:
                msg += f'\n     {count} x {price}'
            elif type(count) is float:
                msg += f'\n     {count} kg x {price}'
            items.append(msg)

        total= str(round(total,2))
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



    # for item in self.reorder_items:
    #     item_id, item_name, quantity_to_add, expected_payment = item
    #     table_name_or_type = self.suppliesController.get_item_type_by_id(item_id)
    #     print(f'Table name or type: {table_name_or_type}')

    #     if table_name_or_type == "Supply":
    #         self.suppliesController.update_supply_quantity_in_database(item_name, quantity_to_add)
    #     elif table_name_or_type == "Items":
    #         self.suppliesController.update_item_quantity_in_database(item_name, quantity_to_add)

    # if self.generate_invoice(supply_items=self.reorder_items, refNo=self.reorder_items[0], datetime=Functions.get_current_date('datetime'), total_sales=sum([item[3] for item in self.reorder_items])):
    #     messagebox.showinfo("Reorder", "Reorder successful. Inventory updated.")
    #     self.tree_cart.delete(*self.tree_cart.get_children())
    #     self.reorder_items.clear()
    #     self._load_reorder_items()

    # def fetch_data_from_supplies(self):
    #     suppliesData = []
    #     for items in self.tree_cart.get_children():
    #         suppliesData.append(self.tree_cart.item(items)['values'])
    #     return suppliesData