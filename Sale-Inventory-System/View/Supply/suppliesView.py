import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter import font, CENTER
from Utils import Functions
from textwrap import dedent

class SuppliesView(tk.Frame):
    def __init__(self, suppliesController, master):
        self.master = master
        self.mainBg = "Grey89"
        super().__init__(self.master, background=self.mainBg)
        self.suppliesController = suppliesController
        self.supplies_btn_lbls = ["Reorder"]
        self.btns = []  # Initialize btns before calling self.main()
        self.pack(fill=tk.BOTH, expand=True)
        self.table_cart = ['Product Name', 'Current Quantity', 'Quantity to Add']
        self.entry_lbls = {'Product Name': 1, 'Current Quantity': 1, 'Quantity to Add': 1}
        self.reorder_entry_boxes = []
        self.reorder_items = []

    def main(self):
        self._button_reorder_frame()
        self._supplies_buttons()
        self._fetch_button()
        self._cart_label()
        self._display_cart_table()
        # self._reorder_button()

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
        self.cart = tk.Label(self, font=font.Font(family='Courier New', size=14, weight='bold'), text="Reorder Items", background=self.mainBg)
        self.cart.place(relx=0.75, rely=0.06, anchor=CENTER)

    def _display_cart_table(self):
        self.tree_cart = ttk.Treeview(self, columns=self.table_cart, show='headings', selectmode='browse')
        for col in self.table_cart:
            self.tree_cart.heading(col, text=col)
            self.tree_cart.column(col, anchor='e')
        
        self.tree_cart.bind("<Configure>", Functions.adjust_column_widths)
        self.tree_cart.place(relx=0.98, rely=0.48, anchor='e', width=450, height=450)
        self._load_reorder_items()

    def _load_reorder_items(self):
        self.tree_cart.delete(*self.tree_cart.get_children())
        reorder_items = Functions.convert_dicc_data(self.suppliesController.fetch_items_below_or_equal_flooring())
        print(reorder_items)
        self._insert_data(self.tree_cart, reorder_items)
        reorder_supplies = Functions.convert_dicc_data(self.suppliesController.fetch_supply_below_or_equal_flooring())
        print("Reorder Supplies:", reorder_supplies)
        self._insert_data(self.tree_cart, reorder_supplies)

    def _insert_data(self, tree: ttk.Treeview, data: list):
        for item in data:
            tree.insert('', 0, values=item)

    # def _reorder_button(self):
    #     reorder_btn = tk.Button(self, font=font.Font(family='Courier New', size=12, weight='bold'), padx=100, pady=2, text="Reorder", command=self._reorder)
    #     reorder_btn.place(relx=0.95, rely=0.97, anchor='se')

    def _fetch_button(self):
        fetch_btn = tk.Button(self, font=font.Font(family='Courier New', size=12, weight='bold'), padx=100, pady=2, text="Fetch", command=self._load_reorder_items)
        fetch_btn.place(relx=0.60, rely=0.97, anchor='se')

    def _supplies_button_commands(self, btn):
        if btn == "Reorder":
            selected_item = self.tree_cart.selection()
            if not selected_item:
                return messagebox.showerror("Error", "Please select an item to reorder")
            self._reorder_items(selected_item)

    def _reorder_items(self, selected_item):
        # Assuming you want to ask these questions once per reorder action, not per item.
        type_of_id = simpledialog.askstring("Item Type", "Enter the type (supply or raw?):", parent=self)
        if type_of_id not in ["supply", "raw"]:
            messagebox.showerror("Error", "Invalid item type. Please enter 'supply' or 'raw'.")
            return
    
        for i in selected_item:
            item = self.tree_cart.item(i)['values']
            product_name = item[0]
            current_quantity = int(float(item[1]))
            quantity_to_add = simpledialog.askinteger("Add Quantity", f"How much of {product_name} to add?", parent=self, minvalue=1)
    
            if quantity_to_add is not None:
                # Assuming you still want to show the updated quantity in the UI
                new_values = (product_name, current_quantity + quantity_to_add, quantity_to_add)
                self.tree_cart.item(i, values=new_values)
                self.reorder_items.append((product_name, current_quantity, quantity_to_add))
    
                if type_of_id == "supply":
                    # Ensure this method adds `quantity_to_add` to the existing quantity in the database
                    self.suppliesController.update_supply_quantity_in_database(product_name, quantity_to_add)
                elif type_of_id == "raw":
                    # Ensure there's a similar method for raw items that adds `quantity_to_add` to the existing quantity
                    self.suppliesController.update_item_quantity_in_database(product_name, quantity_to_add)

    def _reorder(self,item_name:str=None, current_quantity:int=None):
        if not self.reorder_items:
            return messagebox.showerror("Reorder Error", "No items selected for reorder.")
        
        for item in self.reorder_items:
            item_name, current_quantity, quantity_to_add = item
            new_quantity = current_quantity + quantity_to_add
            self.suppliesController.update_item_quantity_in_database(item_name, new_quantity)
        
        messagebox.showinfo("Reorder", "Reorder successful. Inventory updated.")
        self.tree_cart.delete(*self.tree_cart.get_children())
        self.reorder_items.clear()
        self._load_reorder_items()

