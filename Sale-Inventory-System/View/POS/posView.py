import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter import font, CENTER
from Utils import Functions
class PosView(tk.Frame):
    def __init__(self,posController,master):
        self.master = master
        super().__init__(self.master, background=self.mainBg)
        self.posController = posController
        self.mainBg = 'Grey89'
        self.pack(fill=tk.BOTH,expand=True)
        self.pos_btn_lbls = ["Add Product","Remove Product"]
        self.btns = []

        self.table_cart = ['Product Name','Quantity','Total Price']
        self.table_product = ['Product Name','Quantity','Price/unit']
        self.category_product = ["Breakfast","Lunch","Dinner","Desert","Drinks","Snacks"]
        self.sales_entry_boxes = []

    def main(self):
        self._product_table_frame()
        self._pos_frame()
        self._display_product_table()
        self._display_cart_table()
        self._pos_buttons()

    def _pos_buttons(self):
        Functions.create_buttons_using_grid(
            self.posFrame,
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
        # self._search_entry_box()
        # self._search_button()
        # self._category_product_dropdown()
        # self._back_button()




    def _pos_frame(self):
        self.posFrame = tk.Frame(self)
        self.posFrame.place(relx=0.3,rely=0.3,anchor='nw')

    def _product_table_frame(self):
        self.productTableFrame = tk.Frame(self,background=self.mainBg)
        self.productTableFrame.place(relx=0.3,rely=0.5,anchor='w')


    def _display_product_table(self):
        self.tree_product = ttk.Treeview(self,columns=self.table_product,show='headings')
        for col in self.table_product:
            self.tree_product.heading(col, text=col)
            self.tree_product.column(col, anchor='e')
        self.tree_product.bind("<Configure>", Functions.adjust_column_widths)
        self.tree_product.bind("<ButtonRelease-1>", self._on_select_product)
        self.tree_product.place(relx=0.3,rely=0.8)

        # Fetch and display specific product details: product_name, price, quantity
        all_products = Functions.convert_dicc_data(self.posController.fetch_all_products())  # Fetch all products from the database
        self.all_product_details = {}  # Store all product details for later use
        for product in all_products:
            # Store complete product data for later use
            self.all_product_details[product[0]] = product  # Assuming product[0] is a unique identifier for each product
            # Extract and insert only product_name, price, and quantity into the treeview
            self.tree_product.insert('', 'end', values=(product[3], product[4], product[5]))

    # def _pos_button_commands(self,btn):
    #     if btn == "Add Product":
    #         selected_item = self.tree_product.focus()  # Get the focused item in the product table
    #         if selected_item:  # Check if an item is selected
    #             product_details = self.tree_product.item(selected_item, 'values')[0]
    #             product_price = self.tree_product.item(selected_item, 'values')[2]
    #             quantity = simpledialog.askinteger("Quantity", "Enter quantity:", minvalue=1)
    #             if quantity and quantity > 0:  # Ensure a valid quantity is entered
    #                 self.add_product_to_cart(product_details, quantity, float(product_price))
    #             else:
    #                 messagebox.showerror("Error", "Invalid quantity.")
    #         else:
    #             messagebox.showerror("Error", "No product selected.")
    #     if btn == "Remove Product":
    #         self._remove_product_from_cart()
    #     if btn == "Checkout":
    #         self._checkout()


    # def add_product_to_cart(self, product_name, quantity, price):
    #     total_price = int(quantity) * price
    #     self.tree_cart.insert('', 'end', values=(product_name, quantity, total_price))
    #     self.calculate_total_amount()
    #     self.update_total_amount()

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
    
    # def _display_cart_table(self):
    #     self.tree_cart = ttk.Treeview(self.posFrame,columns=self.table_cart,show='headings')
    #     for col in self.table_cart:
    #         self.tree_cart.heading(col,text=col)
    #         self.tree_cart.column(col,anchor='e')
    #     self.tree_cart.bind("<Configure>",Functions.adjust_column_widths)
    #     self.tree_cart.grid(row=4,column=0,sticky='nswe',columnspan=5)


    # def _total_amount_label(self):
    #     self.total_amount_label = tk.Label(self.posFrame,font=font.Font(family='Courier New',size=12,weight='bold'),
    #                                        text=f"Total Amount: ",background=self.mainBg)
    #     self.total_amount_label.grid(row=5,column=0,sticky='s',columnspan=5)

    # def _checkout_button(self):
    #     checkout_btn = tk.Button(self.posFrame,font=font.Font(family='Courier New',size=12,weight='bold'),
    #                              text="Checkout",command=self._checkout)
    #     checkout_btn.grid(row=6,column=0,sticky='s',columnspan=5)

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

    # def _checkout(self):
    #     if self.tree_cart.get_children():
    #         cart_items = []
    #         for child in self.tree_cart.get_children():
    #             product_name, quantity, total_price = self.tree_cart.item(child, 'values')
    #             cart_items.append((product_name, int(quantity), float(total_price)))
    #             print(f'cart_items: {cart_items}')
    #             self.posController.update_product_quantity_in_database(product_name, int(quantity))
    #         self.posController.save_transaction_to_sales()
    #         messagebox.showinfo("Checkout", "Checkout successful. Inventory updated and sales recorded.")
    #         self.tree_cart.delete(*self.tree_cart.get_children())
    #         self.calculate_total_amount()
    #     else:
    #         messagebox.showerror("Checkout Error", "Cart is empty.")

    # def update_total_amount(self):
    #     total_amount = 0
    #     for child in self.tree_cart.get_children():
    #         total_amount += float(self.tree_cart.item(child, 'values')[2])
    #     self.total_amount_label.config(text=f"Total Amount: {total_amount}")

    # def _back_button(self):
    #     self.back_btn = tk.Button(self.posFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Back", 
    #                               command=lambda:self.posController.managerController(self.master))
    #     self.back_btn.pack()