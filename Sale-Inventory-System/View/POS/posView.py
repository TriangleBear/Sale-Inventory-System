import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter import font, CENTER
from Utils import Functions
class PosView(tk.Frame):
    def __init__(self,posController,master):
        self.master = master
        super().__init__(self.master)
        self.posController = posController
        self.mainBg = 'Grey89'
        self.pack(fill=tk.BOTH,expand=True)
        self.pos_btn_lbls = ["Add Product","Remove Product"]
        self.btns = []

        self.table_cart = ['Product Name','Quantity','Total Price']
        self.table_product = ['Product Name','Quantity','Price']
        self.category_product = ["Breakfast","Lunch","Dinner","Desert","Drinks","Snacks"]
        self.sales_entry_boxes = []

    def main(self):
        self._pos_frame()
        self._pos_buttons()

    def _pos_buttons(self):
        Functions.create_buttons_using_grid(self.posFrame,
                                            labels=self.pos_btn_lbls,
                                            entryList=self.btns,
                                            max_columns=2,
                                            w=21,
                                            h=1,
                                            fontSize=12,
                                            gridxPadding=5,
                                            gridyPadding=5,
                                            btnyPadding=2,
                                            btnxPadding=5,
                                            cmd=self._pos_button_commands,
                                            )
        self._search_entry_box()
        self._search_button()
        self._category_product_dropdown()
        self._display_product_table()
        self._display_table_cart()
        self._total_amount_label()
        self._checkout_button()
        # self._back_button()


    def _pos_frame(self):
        self.posFrame = tk.Frame(self,background="GhostWhite")
        self.posFrame.pack(fill=tk.BOTH,expand=True)

    def _pos_button_commands(self,btn):
        if btn == "Add Product":
            selected_item = self.tree_product.focus()  # Get the focused item in the product table
            if selected_item:  # Check if an item is selected
                product_details = self.tree_product.item(selected_item, 'values')[0]
                product_price = self.tree_product.item(selected_item, 'values')[2]
                quantity = simpledialog.askinteger("Quantity", "Enter quantity:", minvalue=1)
                if quantity and quantity > 0:  # Ensure a valid quantity is entered
                    self.add_product_to_cart(product_details, quantity, float(product_price))
                else:
                    messagebox.showerror("Error", "Invalid quantity.")
            else:
                messagebox.showerror("Error", "No product selected.")
        elif btn == "Remove Product":
            pass  # Implement product removal logic here
        elif btn == "Checkout":
            self._checkout()
    def _display_product_table(self):
        self.tree_product = ttk.Treeview(self.posFrame,
                                    columns=self.table_product,
                                    show='headings')
        for col in self.table_product:
            self.tree_product.heading(col, text=col)
            self.tree_product.column(col, anchor='e')
        self.tree_product.bind("<Configure>", Functions.adjust_column_widths)
        self.tree_product.bind("<ButtonRelease-1>", self._on_select_product)
        self.tree_product.grid(row=2,column=0,sticky='s',columnspan=5)

        # Fetch and display specific product details: product_name, price, quantity
        all_products = Functions.convert_dicc_data(self.posController.fetch_all_products())  # Fetch all products from the database
        for product in all_products:
            # Extract and insert only product_name, price, and quantity into the treeview
            self.tree_product.insert('', 'end', values=(product[3], product[4], product[5]))  # Insert each product into the treeview        
    
    def _search_button(self):
        search_btn = tk.Button(self.posFrame,borderwidth=5,width=10,font=font.Font(family='Courier New',size=12,weight='bold'),
                               text="Search",command=self._search)
        search_btn.grid(row=3,column=0, sticky='nswe')

    def _search_entry_box(self):
        search_entry = tk.Entry(self.posFrame, borderwidth=5, width=10,font=font.Font(size=12))
        search_entry.grid(row=3,column=1, sticky='nswe')
        self.sales_entry_boxes.append(search_entry)

    def _category_product_dropdown(self):
        self.category_product = ttk.Combobox(self.posFrame,values=self.category_product,width=20,font=font.Font(size=12,weight='bold'),
                                             state='readonly',background=self.mainBg)
        self.category_product.grid(row=3,column=2,sticky='nswe')
        self.category_product.set("Product")

        #table_product
    
    def _display_table_cart(self):
        self.tree_cart = ttk.Treeview(self.posFrame,
                                 columns=self.table_cart,
                                 show='headings')
        for col in self.table_cart:
            self.tree_cart.heading(col, text=col)
            self.tree_cart.column(col, anchor='e')
        self.tree_cart.bind("<Configure>", Functions.adjust_column_widths)
        self.tree_cart.bind("<<TreeviewSelect>>", self._on_product_select)
        self.tree_cart.grid(row=4,column=0,sticky='n',columnspan=5)
    
    def _total_amount_label(self):
        self.total_amount_label = tk.Label(self.posFrame,font=font.Font(family='Courier New',size=12,weight='bold'),
                                           text=f"Total Amount: ",background=self.mainBg)
        self.total_amount_label.grid(row=5,column=0,sticky='s',columnspan=5)

    def _checkout_button(self):
        checkout_btn = tk.Button(self.posFrame,font=font.Font(family='Courier New',size=12,weight='bold'),
                                 text="Checkout",command=self._checkout)
        checkout_btn.grid(row=6,column=0,sticky='s',columnspan=5)

    def _search(self):
        search = self.sales_entry_boxes[0].get()
        if search != "":
            product = self.posController.search_product(search)
            if product:
                self.tree_product.insert('', 'end', values=product)
            else:
                messagebox.showerror("Search Error","Product not found.")
        else:
            messagebox.showerror("Search Error","Please enter a product.")
        return
    
    def _on_product_select(self, event):
        selected_item = self.tree_product.selection()[2]  # Assuming single selection
        product_details = self.tree_product.item(selected_item, 'values')
        quantity = simpledialog.askinteger("Quantity", "Enter quantity:", minvalue=1)
        if quantity > 0:
            self.add_product_to_cart(product_details, quantity)
        else:
            messagebox.showerror("Quantity Error", f"Invalid quantity {self.quantity}.")

    def _on_select_product(self,_):
        selected_item = self.tree_product.focus()
        current_selection = self.tree_product.selection()
        if current_selection == selected_item:
            self.tree_product.selection_remove(current_selection)
        else:
            self.tree_product.selection_set(selected_item)

    def add_product_to_cart(self, product_name, quantity, product_price):
        # Check if the product is already in the cart
        for item in self.tree_cart.get_children():
            item_details = self.tree_cart.item(item, 'values')
            if item_details[0] == str(product_name):
                # Product is already in the cart, update its quantity
                new_cart_quantity = int(item_details[1]) + quantity
                new_cart_total_price = new_cart_quantity * product_price
                # Update the cart item with the new quantity and total price
                self.tree_cart.item(item, values=(product_name, new_cart_quantity, product_price, new_cart_total_price))
                return
        
        # Product is not in the cart, add it as a new entry
        new_cart_total_price = quantity * product_price
        self.tree_cart.insert('', 'end', values=(product_name, quantity, product_price, new_cart_total_price))
    
    def get_current_quantity(self, product_name):
        for item in self.tree_product.get_children():
            item_details = self.tree_product.item(item, 'values')
            if item_details[0] == str(product_name):
                return int(item_details[1])
        return 0

    def _update_product_quantity_in_tree_product(self, product_name, new_quantity):
        for item in self.tree_product.get_children():
            item_details = self.tree_product.item(item, 'values')
            # Convert item_details to a list to allow modifications
            item_details_list = list(item_details)
            
            if item_details_list[0] == str(product_name):
                # Update the quantity at the correct index
                item_details_list[1] = str(new_quantity)
                
                # Update the item in the tree with the modified details
                self.tree_product.item(item, values=item_details_list)
                break  # Exit the loop once the product is found and updated
   
    def _sum_of_total_price(self):
        total_price = 0
        for item in self.tree_cart.get_children():
            # Assuming 'values' is a list and you want to sum all elements from the third element onwards
            item_values = self.tree_cart.item(item)['values']
            if len(item_values) > 2:  # Check if there are more than two elements
                prices = item_values[2:]  # Get all elements from the third element onwards
                total_price += sum(map(float, prices))  # Convert each to float and sum them
        return total_price
        
    def _update_total_amount(self):
        total_amount = self._sum_of_total_price()
        self.total_amount_label.config(text=f"Total Amount: {total_amount}")
        return

    def _checkout(self):
        #messagebox.showinfo("Checkout","Checkout Successful!")
        pass

    def _back_button(self):
        self.back_btn = tk.Button(self.posFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Back", 
                                  command=lambda:self.posController.managerController(self.master))
        self.back_btn.pack()