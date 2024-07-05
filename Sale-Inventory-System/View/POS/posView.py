import tkinter as tk
import os,textwrap
from tkinter import ttk, messagebox, simpledialog
from tkinter import font, CENTER
from Utils import Functions
from textwrap import dedent
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
        self._total_amount_num_lable()
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
        self.tree_product.place(relx=0.12,rely=0.59,anchor='w',width=350,height=450)
        self._insert_data(self.tree_product, Functions.convert_dicc_data(Functions.filter_product_columns(self.posController.fetch_all_products())))

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

    def _total_amount_num_lable(self):
        self.total_amount_label = tk.Label(self,font=font.Font(family='Courier New',size=12,weight='bold'),
                                           text=f"{self.total_amount}",background=self.mainBg)
        self.total_amount_label.place(relx=0.97,rely=0.9,anchor='se')

    def _total_amount_label(self):
        total_amount_label = tk.Label(self,font=font.Font(family='Courier New',size=12,weight='bold'),
                                           text=f"Total Amount: ",background=self.mainBg)
        total_amount_label.place(relx=0.85,rely=0.9,anchor='se')

    def _checkout_button(self):
        checkout_btn = tk.Button(self,font=font.Font(family='Courier New',size=12,weight='bold'),
                                 padx=100,pady=2,text="Checkout",command=self._checkout)
        checkout_btn.place(relx=0.95,rely=0.97,anchor='se')

    def _insert_data(self,tree:ttk.Treeview,data:list):
        for item in data:
            tree.insert('', 0, values=item)        

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

    def _remove_product_from_cart(self,selectedItem):
        for i in selectedItem:
            item = self.tree_cart.item(i)['values']
            current_quantity = int(item[1])
            current_total_price = float(item[2])
            unit_price = current_total_price / current_quantity  # Calculate unit price

            quantity_to_remove = simpledialog.askinteger("Remove Quantity", f"How much of {item[0]} to remove?", parent=self, minvalue=0.0, maxvalue=current_quantity)
            if quantity_to_remove is not None and quantity_to_remove < current_quantity:
                new_quantity = current_quantity - quantity_to_remove
                new_total_price = unit_price * new_quantity 
                self.total_amount -= (current_total_price-new_total_price) # Recalculate total price based on new quantity
                self.tree_cart.item(i, values=(item[0], new_quantity, new_total_price))
                self.update_total_amount_label()
                return
            else:
                self.tree_cart.delete(i)
                self.total_amount -= current_quantity * unit_price
                self.update_total_amount_label()
                return

    def calculate_product_input(self):
        selected_item = self.tree_product.selection()[0]  # Get the focused item in the product table
        if not selected_item:  # Check if an item is selected
            return messagebox.showerror("Error", "No product selected.")
        product_name,quantity_available, product_price = self.tree_product.item(selected_item, 'values')
        quantity = simpledialog.askinteger("Quantity", "Enter quantity:", minvalue=1)
        if quantity > int(quantity_available):  # Ensure a valid quantity is entered
            return messagebox.showerror("Error", "Quantity is greater than available stock.")
        elif quantity <= int(quantity_available):
            self.add_product_to_cart(selected_item=[product_name, quantity, float(product_price)],quantity_available=quantity_available)
            self.update_product_table(quantity,selected_item)
            return
        else:
            return messagebox.showerror("Error", "Invalid quantity entered.")

    def add_product_to_cart(self, selected_item:list,quantity_available):#selected item = [product_name, quantity, price]
        product_name,quantity,price = selected_item 
        total_price = int(quantity) * price
        for iid in self.tree_cart.get_children():
            existingItem = Functions.check_existing_cart_item(
                insertData=selected_item,
                insertedData=self.tree_cart.item(iid,'values'),
                quantity_available=quantity_available
            )
            print(f"from existingItem: {existingItem}")
            if existingItem == None:
                continue
            if type(existingItem) == list:
                self.total_amount += (existingItem[2] - float(self.tree_cart.item(iid,'values')[2]))
                self.tree_cart.item(iid,values=existingItem)
                self.update_total_amount_label()
                return
            else:
                return messagebox.showerror("Error",existingItem)
        self._insert_data(self.tree_cart,[[product_name,quantity,int(quantity)*price]])
        self.total_amount += int(quantity)*price
        print(f"{self.total_amount}")
        self.update_total_amount_label()
    
    def update_total_amount_label(self):
        self.total_amount_label.config(text=f"{self.total_amount}")

    def update_product_table(self,quantity,item):
        pass
    
    def _checkout(self):
        datetime = Functions.get_current_date("datetime")
        if self.tree_cart.get_children():
            cart_items = [] 
            for child in self.tree_cart.get_children():
                cart_items.append([*Functions.format_cart_item(*self.tree_cart.item(child, 'values'))])
            amount_tendered = simpledialog.askfloat("Amount Tendered", "Enter amount tendered:", minvalue=self.total_amount)
            if amount_tendered >= self.total_amount:
                sales_id,sold_on = self.posController.save_sales(amount_tendered,self.total_amount,datetime)
                self.posController.save_transaction_to_sales(cart_items, sales_id,sold_on)
                self.posController.update_product_quantity_in_database(cart_items=cart_items) #product_name, quantity
                self.posController.logUserActivity(sales_id)
                messagebox.showinfo("Checkout", "Checkout successful. Inventory updated and sales recorded.")
                self.generate_invoice(cart_items=cart_items,amount_tendered=amount_tendered,change=amount_tendered - self.total_amount,refNo=sales_id,datetime=datetime)
                self.tree_cart.delete(*self.tree_cart.get_children())
                self.tree_product.delete(*self.tree_product.get_children())
                self._insert_data(self.tree_product,Functions.convert_dicc_data(Functions.filter_product_columns(self.posController.fetch_all_products())))
                self.total_amount = 0
                self.update_total_amount_label()
        else:
            messagebox.showerror("Checkout Error", "Cart is empty.")

    def generate_invoice(self, cart_items,amount_tendered,change,refNo,datetime):
        if not cart_items:       
            messagebox.showwarning("No Items", "No items to generate invoice.")
            return
        max_item_name_width = max(len(item[0]) for item in cart_items) + 2  # Adding a little extra space
        min_quantity_width = 5  # Minimum width for the quantity column
        min_total_width = 10  # Minimum width for the total price column
            
        receipt_text = dedent(f"""
        Tapsi ni Vivian
        991 AURORA BLVD, PROJECT 3, QUEZON CITY, 
        1102 METRO MANILA
        32 GIL FERNANDO AVENUE, QUEZON CITY
        Phone: (02)8645-0125
        DATE: {datetime}
        REF#: {refNo}
        ITEM NAME\tQUANTITY\tTOTAL
        """ + "-"*55 + "\n")

        for item in cart_items:
            item_name, quantity, total = item
            receipt_text += f"{item_name.upper():<{max_item_name_width}}{quantity:>{min_quantity_width}}{total:>{min_total_width}.2f}\n"

        subtotal = self.total_amount
        tax = subtotal * 0.01  # Assuming a 10% tax rate
        grand_total = subtotal + tax
        receipt_text += "-"*55 + "\n"
        receipt_text += f"SUBTOTAL:\t\t\t{subtotal:.2f}\n"
        receipt_text += f"TAX (10%):\t\t\t{tax:.2f}\n"
        receipt_text += f"TOTAL:\t\t\t\t{grand_total:.2f}\n"
        receipt_text += "-"*55 + "\n"
        receipt_text += f"AMOUNT TEND:\t\t\t{amount_tendered:.2f}\n"
        receipt_text += f"CHANGE DUE:\t\t\t{change:.2f}\n"
        receipt_text += "-"*55 + "\nThank you for dining with us!\n"

        if not os.path.exists("Sale-Inventory-System/Receipts"):
            os.makedirs("Sale-Inventory-System/Receipts")
        
        path = os.path.join("Sale-Inventory-System/Receipts",f"{refNo}.txt")

        with open(path, "w") as file:
            file.write(receipt_text)

        messagebox.showinfo("Invoice Generated", receipt_text)
        return
