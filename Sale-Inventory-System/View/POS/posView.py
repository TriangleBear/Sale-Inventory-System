import tkinter as tk
import os,textwrap,copy
from tkinter import ttk, messagebox, simpledialog
from tkinter import font, CENTER,FLAT
from Utils import Functions
from textwrap import dedent
class PosView(tk.Frame):
    def __init__(self,posController,master):
        self.master = master
        self.mainBg = "Grey89"
        self.buttonPressBg = "Grey86"
        super().__init__(self.master,background=self.mainBg)
        self.posController = posController
        self.pack(fill=tk.BOTH,expand=True)
        self.pos_btn_lbls = ["Add Product","Remove Product"]
        self.btns = []

        self.table_cart = ['Product Name','Quantity','Total Price']
        self.table_product = ['Product Name','Quantity','Price/unit']
        self.category_product = ["Breakfast","Lunch","Dinner","Desert","Drinks","Snacks"]
        self._all_products = self.posController.fetch_all_products()
        self.category_btns = []
        self.menu_status = "Breakfast" #default
        self.total_amount = 0
    
    @property
    def all_products(self):
        return copy.deepcopy(self._all_products)
    

    def main(self):
        self._button_add_remove_frame()
        self._add_remove_buttons()
        self._search_entry()
        self._search_button()
        self._refresh_button()
        self._display_product_table()
        self._category_frame()
        self._category_buttons()
        self._cart_label()
        self._display_cart_table()
        self._total_amount_label()
        self._total_amount_num_lable()
        self._checkout_button()

    def get_breakfast_products(self,data:list[dict]) -> list[dict]:
        return Functions.convert_dicc_data(Functions.filter_product_columns(Functions.filter_breakfast_products(data)))
    
    def get_lunch_products(self,data:list[dict]) -> list[dict]:
        return Functions.convert_dicc_data(Functions.filter_product_columns(Functions.filter_lunch_products(data)))
    
    def get_dinner_products(self,data:list[dict]) -> list[dict]:
        return Functions.convert_dicc_data(Functions.filter_product_columns(Functions.filter_dinner_products(data)))
    
    def get_desert_products(self,data:list[dict]) -> list[dict]:
        return Functions.convert_dicc_data(Functions.filter_product_columns(Functions.filter_desert_products(data)))
    
    def get_drinks_products(self,data:list[dict]) -> list[dict]:
        return Functions.convert_dicc_data(Functions.filter_product_columns(Functions.filter_drinks_products(data)))
    
    def get_snacks_products(self,data:list[dict]) -> list[dict]:
        return Functions.convert_dicc_data(Functions.filter_product_columns(Functions.filter_snacks_products(data)))

    def _button_add_remove_frame(self):
        self.headerFrame = tk.Frame(self,background=self.mainBg)
        self.headerFrame.place(relx=0.03,rely=0.97,anchor='sw')

    def _add_remove_buttons(self):
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
        self.tree_product.place(relx=0.12,rely=0.48,anchor='w',width=350,height=450)
        self._insert_data(self.tree_product, self.get_breakfast_products(self.posController.fetch_all_products()))

    def _search_entry(self):
        self.search_entry = tk.Entry(self, borderwidth=0, width=27,font=font.Font(size=12))
        self.search_entry.place(relx=0.23, rely=0.06,anchor='w')  # Place the entry at the top with some paddin

    def _search_button(self):
        search_button = tk.Button(self, font=font.Font(family='Courier New', size=9, weight='bold'), text="Search",
                                    command=lambda: self._search_data(self.search_entry.get(),self.menu_status), padx=7, pady=3)
        search_button.place(relx=0.12,rely=0.06, anchor='w')  # Place the button at the bottom with some padding

    def _refresh_button(self):
        refresh_button = tk.Button(self, font=font.Font(family='Courier New',size=9,weight='bold'),text="Refresh", 
                                   command=lambda:self._category_commands(button=self.menu_status),padx=7, pady=3)
        refresh_button.place(relx=0.02,rely=0.06,anchor='w')

    def _category_frame(self):
        self.category_frame = tk.Frame(self,background=self.mainBg,padx=1,pady=3)
        self.category_frame.place(relx=0,rely=0.42,anchor='w')

    def _category_buttons(self):
        Functions.create_buttons_using_grid(
            frame=self.category_frame,
            labels=self.category_product,
            entryList=self.category_btns,
            max_columns=1,
            gridyPadding=1,
            relf=FLAT,
            w=10,
            h=2,
            activeBg=self.buttonPressBg,
            cmd=self._category_commands
        )
    
    def _category_commands(self,button):
        self.tree_product.delete(*self.tree_product.get_children())
        if button == "Breakfast":
            self.menu_status = button
            breakfast = self.all_products
            self._insert_data(self.tree_product, self.get_breakfast_products(breakfast))
        if button == "Lunch":
            self.menu_status = button
            lunch = self.all_products
            self._insert_data(self.tree_product, self.get_lunch_products(lunch))
        if button == "Dinner":
            self.menu_status = button
            dinner = self.all_products
            self._insert_data(self.tree_product, self.get_dinner_products(dinner))
        if button == "Desert":
            self.menu_status == button
            desert = self.all_products
            self._insert_data(self.tree_product, self.get_desert_products(desert))
        if button == "Drinks":
            self.menu_status == button
            drinks = self.all_products
            self._insert_data(self.tree_product, self.get_drinks_products(drinks))
        if button == "Snacks":
            self.menu_status == button
            snacks = self.all_products
            self._insert_data(self.tree_product, self.get_desert_products(snacks))

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
        self.total_amount_label = tk.Label(
            self,
            font=font.Font(family='Courier New',size=12,weight='bold'),
            text=f"{self.total_amount}",
            background=self.mainBg
        )
        self.total_amount_label.place(relx=0.97,rely=0.9,anchor='se')

    def _total_amount_label(self):
        total_amount_label = tk.Label(
            self,
            font=font.Font(family='Courier New',size=12,weight='bold'),
            text=f"Total Amount: ",
            background=self.mainBg
        )
        total_amount_label.place(relx=0.85,rely=0.9,anchor='se')

    def _checkout_button(self):
        checkout_btn = tk.Button(
            self,
            font=font.Font(family='Courier New',size=12,weight='bold'),
            padx=100,
            pady=2,
            text="Checkout",
            command=lambda:self._checkout(self.menu_status)
        )
        checkout_btn.place(relx=0.95,rely=0.97,anchor='se')

    def _search_data(self, search_query,menu):
        result = self.posController.search_data(search_query)
        search_results = Functions.convert_dicc_data(Functions.filter_product_columns(result))

        self.tree_product.delete(*self.tree_product.get_children())
        self._insert_data(self.tree_product,search_results)

    def _insert_data(self,tree:ttk.Treeview,data:list):
        for item in data:
            tree.insert('', 0, values=item)        

    def _pos_button_commands(self,btn):
        if btn == "Add Product":
            self.calculate_product_input()
        elif btn == "Remove Product":
            self._remove_product_from_cart()

    def _remove_product_from_cart(self):
        selected_item = self.tree_cart.selection()
        if not selected_item:
            return messagebox.showerror("Error", "Please select an item to remove")
        for i in selected_item:
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
        selected_item = self.get_selected_product()
        product_name,quantity_available, product_price = self.tree_product.item(selected_item, 'values') #unpack selected product values
        quantity = simpledialog.askinteger("Quantity", "Enter quantity:", minvalue=1) #ask for amount desired for cart
        self.check_quantity(product_name,quantity_available,product_price,quantity)
        
    def get_selected_product(self):
        selected_item = self.tree_product.selection()[0]
        return selected_item if selected_item else messagebox.showerror("Error", "No product selected.")
    
    def check_quantity(self,product_name,quantity_available,product_price,quantity):
        if quantity > int(quantity_available):  # Ensure a valid quantity is entered
            return messagebox.showerror("Error", "Quantity is greater than available stock.")
        elif quantity <= int(quantity_available):
            self.add_product_to_cart(selected_item=[product_name, quantity, float(product_price)],quantity_available=quantity_available)
            # self.update_product_table(quantity,selected_item)
            return
        else:
            return messagebox.showerror("Error", "Invalid quantity entered.")

    def add_product_to_cart(self, selected_item:list,quantity_available:int):#selected item = [product_name, quantity, price]
        product_name,quantity,price = selected_item
        total_price = int(quantity) * price
        for iid in self.tree_cart.get_children():
            existingItem = Functions.check_existing_cart_item(
                insertData=selected_item,
                insertedData=self.tree_cart.item(iid,'values'),
                quantity_available=quantity_available
            )
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
    
    def table_reset(self,menu_status:str) -> None:
        print(menu_status)
        self.tree_cart.delete(*self.tree_cart.get_children())
        self.tree_product.delete(*self.tree_product.get_children())
        self.total_amount = 0
        self.update_total_amount_label()
        self._all_products = self.posController.fetch_all_products()
        if menu_status == "Breakfast":
            self._insert_data(self.tree_product,self.get_breakfast_products(self.all_products))
        if menu_status == "Lunch":
            self._insert_data(self.tree_product,self.get_lunch_products(self.all_products))
        if menu_status == "Dinner":
            self._insert_data(self.tree_product,self.get_dinner_products(self.all_products))
        if menu_status == "Desert":
            self._insert_data(self.tree_product,self.get_desert_products(self.all_products))
        if menu_status == "Drinks":
            self._insert_data(self.tree_product,self.get_drinks_products(self.all_products))
        if menu_status == "Snacks":
            self._insert_data(self.tree_product,self.get_snacks_products(self.all_products))

    def _checkout(self,menu_status:str):
        print(menu_status)
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
                self.generate_invoice(cart_items=cart_items,amount_tendered=amount_tendered,change=amount_tendered - self.total_amount,refNo=sales_id,datetime=datetime,total_sales=self.total_amount)
                self.table_reset(menu_status)
        else:
            messagebox.showerror("Checkout Error", "Cart is empty.")

    def generate_invoice(self, cart_items, amount_tendered, change, refNo, datetime,total_sales):
        if not cart_items:
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
        for name,count,price in cart_items:
            price /= count
            all_price = str(round(price*count,2))
            msg = f'{name}'.ljust(width-len(all_price))+all_price

            if type(count) is int and count >=2:
                msg += f'\n     {count} x {price}'
            elif type(count) is float:
                msg += f'\n     {count} kg x {price}'
            items.append(msg)

        total= str(round(total_sales,2))
        amt_tnd = str(round(amount_tendered,2))
        change_due = str(round(change,2))
        items.append(("-"*width).center(width))
        items.append("TOTAL:".ljust(width-len(total))+total)
        items.append("AMT_TND:".ljust(width-len(amt_tnd))+amt_tnd)
        items.append(("-"*width).center(width))
        items.append("CHANGE DUE:".ljust(width-len(change_due))+change_due)
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
