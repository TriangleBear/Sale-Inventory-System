from tkinter import *
import tkinter as tk
from tkinter import ttk
from Utils import Functions
from tkinter import font, messagebox
from tkcalendar import DateEntry
class InventoryView(tk.Frame):
    def __init__(self,inventoryController,master):
        self.inventoryController = inventoryController
        self.master = master
        super().__init__(self.master, background="GhostWhite")

        self.inventory_labels_with_colspan = {"Product ID":1,
                                             "Product Name":1,
                                             "Quantity":1,
                                             "Supplier":1,
                                             "Expirartion Date":1,
                                             "Menu":1,
                                             "Cost":1,
                                             "Category":1}
        self.inventory_entry_boxes = []
        self.inventory_inputs = []
        self.pack(fill=tk.BOTH,expand=True)

    def main(self):
        self._inventory_frame()  
        self._entry_frame()
        self._inventory_widgets()
        self._inventory_button()

    def _inventory_widgets(self):
        self.table_frame()
        self._display_inventory_table()
        self._search_entry()
        self._search_button()
        #self._update_button()
        self._display_inventory_table()
        self._back_to_manager_button()

    def table_frame(self):
        self.tableFrame = tk.Frame(self.inventoryFrame,background="Gray82")
        self.tableFrame.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _insert_inventory_data_table(self):
        inventory_data = self.inventoryController.get_items_on_database()
        for item in inventory_data:
            self.treeview.insert("", tk.END, values=item)

    def _display_inventory_table(self):
        # Create a Treeview widget
        self.treeview = ttk.Treeview(self.tableFrame)
        
        # Define the columns
        self.treeview["columns"] = ("Product ID", "Product Name", "Quantity", "Supplier", "Expiration Date", "Menu", "Cost", "Category")
        
        # Format the columns
        self.treeview.column("#0", width=0, stretch=tk.NO)

    def _inventory_frame(self):
        self.inventoryFrame = tk.Frame(self,background="GhostWhite")
        self.inventoryFrame.pack(fill=tk.BOTH,expand=True)
    
    def _entry_frame(self):
        self.entryFrame = tk.Frame(self.inventoryFrame,background="Gray82")
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)

    
    def _display_inventory_table(self):
        # Create a Treeview widget
        self.treeview = ttk.Treeview(self.inventoryFrame)
        
        # Define the columns
        self.treeview["columns"] = ("Product ID", "Product Name", "Quantity", "Supplier", "Expiration Date", "Menu", "Cost", "Category")
        
        # Format the columns
        self.treeview.column("#0", width=0, stretch=tk.NO)  # Hide the default first column
        self.treeview.column("Product ID", width=100)
        self.treeview.column("Product Name", width=150)
        self.treeview.column("Quantity", width=80)
        self.treeview.column("Supplier", width=150)
        self.treeview.column("Expiration Date", width=120)
        self.treeview.column("Menu", width=100)
        self.treeview.column("Cost", width=80)
        self.treeview.column("Category", width=100)
        
        # Add column headings
        for column in self.treeview["columns"]:
            self.treeview.heading(column, text=column)
        
        # Add data to the table
        inventory_data = self.inventoryController.get_items_on_database()  # Replace with your own method to get inventory data
        for item in inventory_data:
            self.treeview.insert("", tk.END, values=item)
            
    def _back_to_manager_button(self):
        self.back_btn = tk.Button(self.inventoryFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Back", command=lambda:self.managerController.managerController.main())
        self.back_btn.pack()