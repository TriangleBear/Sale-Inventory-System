import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter import font, CENTER
from Utils import Functions
class PosView(tk.Frame):
    def __init__(self,posController,master):
        self.master = master
        self.mainBg = 'Grey89'
        super().__init__(self.master,background=self.mainBg)
        self.posController = posController
        self.pack(fill=tk.BOTH,expand=True)
        self.pos_btn_lbls = ["Add Product","Remove Product"]
        self.btns = []

        self.table_cart = ['Product Name','Quantity','Total Price']
        self.table_product = ['Product Name','Quantity','Price/unit']
        self.category_product = ["Breakfast","Lunch","Dinner","Desert","Drinks","Snacks"]
        self.sales_entry_boxes = []
        self.total_amount = 0

    def main(self):
        self._button_add_remove_frame()
        self._pos_buttons()
        self._search_entry()
        self._search_button()
        self._display_product_table()
        self._cart_label()
        self._display_cart_table()
        self._total_amount_label()
        self._checkout_button()

    def _button_add_remove_frame(self):
        self.headerFrame = tk.Frame(self,background=self.mainBg)
        self.headerFrame.place(relx=0.01,rely=0.05,anchor='nw')

    def _pos_buttons(self):
        Functions.create_buttons_using_grid(
            self.headerFrame,
            labels=self.pos_btn_lbls,
            entryList=self.btns,
            max_columns=2,
            w=21,
            h=1,
            fontSize=12,
            gridxPadding=2,
            gridyPadding=3,
            btnyPadding=2,
            btnxPadding=2,
            cmd=self._pos_button_commands
        )
    
    def _display_product_table(self):
        Functions.treeview_style(self.mainBg)
        self.tree_product = ttk.Treeview(
            self,columns=self.table_product,
            show='headings',
            style="Custom.Treeview",
            selectmode='browse'
        )
        for col in self.table_product:
            self.tree_product.heading(col, text=col)
            self.tree_product.column(col, anchor='e')
        self.tree_product.bind("<Configure>", Functions.adjust_column_widths)
        # self.tree_product.bind("<ButtonRelease-1>", self._on_select_product)
        self.tree_product.place(relx=0.12,rely=0.59,anchor='w',width=350,height=450)
        self._insert_data(Functions.filter_product_columns(self.posController.fetch_all_products()))

    def _search_entry(self):
        self.search_entry = tk.Entry(self, borderwidth=0, width=27,font=font.Font(size=12))
        self.search_entry.place(relx=0.45, rely=0.17,anchor='e')  # Place the entry at the top with some paddin

    def _search_button(self):
        search_button = tk.Button(self, font=font.Font(family='Courier New', size=9, weight='bold'), text="Search",
                                    command=lambda: print("search"), padx=7, pady=2)
        search_button.place(relx=0.12,rely=0.17, anchor='e')  # Place the button at the bottom with some padding

    def _cart_label(self):
        self.cart = tk.Label(self,font=font.Font(family='Courier New',size=14,weight='bold'),text=f"Cart",background=self.mainBg)
        self.cart.place(relx=0.75,rely=0.06,anchor=CENTER)

    def _display_cart_table(self):
        self.tree_cart = ttk.Treeview(self,columns=self.table_cart,show='headings',selectmode='browse')
        for col in self.table_cart:
            self.tree_cart.heading(col, text=col)
            self.tree_cart.column(col, anchor='e')
        self.tree_cart.bind("<Configure>", Functions.adjust_column_widths)
        self.tree_cart.place(relx=0.98,rely=0.48,anchor='e',width=350,height=450)

    def _total_amount_label(self):
        self.total_amount_label = tk.Label(self,font=font.Font(family='Courier New',size=12,weight='bold'),
                                           text=f"Total Amount:     {self.total_amount}",background=self.mainBg)
        self.total_amount_label.place(relx=0.9,rely=0.9,anchor='se')

    def _checkout_button(self):
        checkout_btn = tk.Button(self,font=font.Font(family='Courier New',size=12,weight='bold'),
                                 padx=100,pady=2,text="Checkout",command=self._checkout)
        checkout_btn.place(relx=0.95,rely=0.97,anchor='se')

    def _insert_data(self,data):
        self.tree_product.delete(*self.tree_product.get_children())
        converted_data = Functions.convert_dicc_data(data)
        for item in converted_data:
            self.tree_product.insert('', 'end', values=item)

    def _pos_button_commands(self,btn):
        if btn == "Add Product":
            self.calculate_product_input()
        elif btn == "Remove Product":
            selected_item = self.tree_cart.selection()
            if not selected_item:
                return messagebox.showerror("Error", "Please select an item to remove")
            self._remove_product_from_cart(selected_item)
        elif btn == "Checkout":
            self._checkout()

    def calculate_product_input(self):
        selected_item = self.tree_product.selection()[0]  # Get the focused item in the product table
        if not selected_item:  # Check if an item is selected
            return messagebox.showerror("Error", "No product selected.")
        product_details = self.tree_product.item(selected_item, 'values')[0]
        quantity_available = int(self.tree_product.item(selected_item, 'values')[1])
        product_price = self.tree_product.item(selected_item, 'values')[2]
        quantity = simpledialog.askinteger("Quantity", "Enter quantity:", minvalue=1)
        if quantity > quantity_available:  # Ensure a valid quantity is entered
            return messagebox.showerror("Error", "Quantity is Greater than available stock.")
        elif quantity <= quantity_available:
            self.add_product_to_cart(product_details, quantity, float(product_price))
            self.update_product_table(quantity,selected_item)
            return
        else:
            return messagebox.showerror("Error", "Invalid quantity entered.")

    def _remove_product_from_cart(self,selectedItem):
        for i in selectedItem:
            item = self.tree_cart.item(i)['values']
            current_quantity = int(item[1])
            current_total_price = float(item[2])
            unit_price = current_total_price / current_quantity  # Calculate unit price

            quantity_to_remove = simpledialog.askfloat("Remove Quantity", f"How much of {item[0]} to remove?", parent=self, minvalue=0.0, maxvalue=current_quantity)
            if quantity_to_remove is not None and quantity_to_remove < current_quantity:
                new_quantity = current_quantity - quantity_to_remove
                new_total_price = unit_price * new_quantity  # Recalculate total price based on new quantity
                self.tree_cart.item(i, values=(item[0], new_quantity, new_total_price))
                self.update_total_amount_label(new_total_price)
                return
            else:
                self.tree_cart.delete(i)
                self.total_amount -= current_quantity * unit_price
                self.update_total_amount_label(self.total_amount)
                return

    def add_product_to_cart(self, product_name, quantity, price):
        total_price = int(quantity) * price
        for iid in self.tree_cart.get_children():
            if product_name == self.tree_cart.item(iid, 'values')[0]:
                current_quantity = int(self.tree_cart.item(iid, 'values')[1])
                new_quantity = current_quantity + quantity
                new_total_price = new_quantity * price
                self.tree_cart.item(iid, values=(product_name, new_quantity, new_total_price))
                self.calculate_total_amount()
                self.update_total_amount_label(self.total_amount)
                return
        self.tree_cart.insert('', 'end', values=(product_name, quantity, total_price))
        self.calculate_total_amount()
        self.update_total_amount_label(self.total_amount)

    def calculate_total_amount(self):
        for child in self.tree_cart.get_children():
            self.total_amount += float(self.tree_cart.item(child, 'values')[2])
    
    def update_total_amount_label(self,total_amount):
        self.total_amount_label.config(text=f"Total Amount:     {total_amount}")

    def update_product_table(self,quantity,item):
        pass

    def generate_invoice(self, cart_items):
        if not cart_items:       
            messagebox.showwarning("No Items", "No items to generate invoice.")
            return

        receipt_text = "Restaurant Name\nAddress Line 1\nAddress Line 2\nPhone: 123-456-7890\n"
        receipt_text += "Date: {}\n\n".format(Functions.get_current_date('datetime'))
        receipt_text += "Item Name\tQuantity\tTotal\n" + "-"*40 + "\n"
        for item in cart_items:
            receipt_text += "{}\t{}\t{}\n".format(item[0], item[1], item[2])
        receipt_text += "-"*40 + "\n"
        subtotal = self.total_amount
        tax = subtotal * 0.01  # Assuming a 10% tax rate
        grand_total = subtotal + tax
        receipt_text += "Subtotal:\t{}\nTax (10%):\t{}\nGrand Total:\t{}\n".format(subtotal, tax, grand_total)
        receipt_text += "-"*40 + "\nThank you for dining with us!\n"

        with open("receipt.txt", "w") as file:
            file.write(receipt_text)

        messagebox.showinfo("Invoice Generated", "Invoice has been generated successfully!\n\n" + receipt_text)
        return
    
    def _checkout(self):
        if self.tree_cart.get_children():
            cart_items = [] 
            for child in self.tree_cart.get_children():
                cart_items.append([*Functions.format_cart_item(*self.tree_cart.item(child, 'values'))])
            amount_tendered = simpledialog.askfloat("Amount Tendered", "Enter amount tendered:", minvalue=self.total_amount)
            if amount_tendered > self.total_amount:
                self.generate_invoice(cart_items=cart_items)
            sales_id = self.posController.save_sales(amount_tendered,self.total_amount)
            self.posController.save_transaction_to_sales(cart_items, sales_id)
            self.posController.update_product_quantity_in_database(cart_items=cart_items) #product_name, quantity
            print(f'cart_items: {cart_items}')
            messagebox.showinfo("Checkout", "Checkout successful. Inventory updated and sales recorded.")
            self._insert_data(Functions.filter_product_columns(self.posController.fetch_all_products()))
            self.tree_cart.delete(*self.tree_cart.get_children())
            self.total_amount = 0
        else:
            messagebox.showerror("Checkout Error", "Cart is empty.")


    # def _on_select_product(self,event):
    #     item = self.tree_product.selection()[0]
    #     product_name = self.tree_product.item(item, 'values')[0]
    #     product_price = float(self.tree_product.item(item, 'values')[2])
    #     self.sales_entry_boxes.insert(product_name,product_price)

    # def calculate_total_amount(self):
    #     total_amount = 0
    #     for child in self.tree_cart.get_children():
    #         total_amount += float(self.tree_cart.item(child, 'values')[2])
    #     self.total_amount_label.config(text=f"Total Amount: {total_amount}")    

    # def _remove_product_from_cart(self):
    #     selected_item = self.tree_cart.selection()
    #     if not selected_item:
    #         return messagebox.showerror("Error", "Please select an item to remove")
    #     for i in selected_item:
    #         item = self.tree_cart.item(i)['values']
    #         current_quantity = int(item[1])
    #         current_total_price = float(item[2])
    #         unit_price = current_total_price / current_quantity  # Calculate unit price

    #         quantity_to_remove = simpledialog.askfloat("Remove Quantity", f"How much of {item[0]} to remove?", parent=self, minvalue=0.0, maxvalue=current_quantity)
    #         if quantity_to_remove is not None:
    #             if quantity_to_remove < current_quantity:
    #                 new_quantity = current_quantity - quantity_to_remove
    #                 new_total_price = unit_price * new_quantity  # Recalculate total price based on new quantity
    #                 self.tree_cart.item(i, values=(item[0], new_quantity, new_total_price))
    #                 self.update_total_amount()
    #             else:
    #                 self.tree_cart.delete(i)
    #                 self.update_total_amount()

    # def _on_select_product(self,event):
    #     item = self.tree_product.selection()[0]
    #     product_name = self.tree_product.item(item, 'values')[0]
    #     product_price = self.tree_product.item(item, 'values')[2]
    #     self.sales_entry_boxes[0].delete(0, tk.END)
    #     self.sales_entry_boxes[0].insert(0, product_name)

    # def _search_button(self):
    #     search_btn = tk.Button(self.posFrame,borderwidth=5,width=10,font=font.Font(family='Courier New',size=12,weight='bold'),
    #                            text="Search",command=self._search)
    #     search_btn.grid(row=3,column=0, sticky='nswe')

    # def _search_entry_box(self):
    #     search_entry = tk.Entry(self.posFrame, borderwidth=5, width=10,font=font.Font(size=12))
    #     search_entry.grid(row=3,column=1, sticky='nswe')
    #     self.sales_entry_boxes.append(search_entry)

    # def _category_product_dropdown(self):
    #     self.category_product = ttk.Combobox(self.posFrame,values=self.category_product,width=20,font=font.Font(size=12,weight='bold'),
    #                                          state='readonly',background=self.mainBg)
    #     self.category_product.grid(row=3,column=2,sticky='nswe')
    #     self.category_product.set("Product")
    

    # def _search(self):
    #     search = self.sales_entry_boxes[0].get()
    #     if search != "":
    #         product = self.posController.search_product(search)
    #         if product:
    #             self.tree_product.insert('', 'end', values=product)
    #         else:
    #             messagebox.showerror("Search Error","Product not found.")
    #     else:
    #         messagebox.showerror("Search Error","Please enter a product.")
    #     return
    # def _back_button(self):
    #     self.back_btn = tk.Button(self.posFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Back", 
    #                               command=lambda:self.posController.managerController(self.master))
    #     self.back_btn.pack()
