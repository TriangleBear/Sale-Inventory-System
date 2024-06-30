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
        self.mainBg = "Gray89"
        self.navBarBg = "Gray84"
        super().__init__(self.master, background=self.mainBg)

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
        self.menus = ["Items","Supplies","Products","Recipes"]
        self.table = self.inventoryController.get_items_column_names()
        print(self.table)
        self.pack(fill=tk.BOTH,expand=True)

    def main(self):
        self._nav_bar_frame()
        self._back_button()
        self._display_table()

    def _nav_bar_frame(self):
        w = self.master.winfo_width()
        h = 50
        self.navBarFrame = tk.Frame(self,background=self.navBarBg)
        self.navBarFrame.place(relx=0,rely=0,width=w,height=h)
        self._nav_bar_label()
        self._tree_dropdown()

    def _tree_dropdown(self):
        self.selectTable = ttk.Combobox(self.navBarFrame,values=self.menus)
        self.selectTable.place(relx=0.4,rely=0.5,anchor=CENTER)
        self.selectTable.set(self.menus[0])
        self.selectTable.bind('<<ComboboxSelected>>', lambda event: self._change_column_labels(self.selectTable.get(),self.selectTable.get()))
        #self._update_table(self.selectTable.get())

    def _insert_table_columns(self):
        for col in self.table:
            self.tree.heading(col, text=col)    
            self.tree.column(col, anchor='center')

    def _display_table(self):
        self.tree = ttk.Treeview(self, columns=self.table, show='headings',selectmode='browse')
        self._insert_table_columns()
        self.tree.bind('<Configure>',Functions.adjust_column_widths)
        self.tree.place(relx=0.49999,rely=0.5,anchor='center',width=839.9,height=355)
        self._insert_data(self.inventoryController.get_items_on_database())

    def _insert_data(self,data):
        self.tree.delete(*self.tree.get_children())
        converted_data = Functions.convert_dicc_data(data)
        for item in converted_data:
            self.tree.insert('', 'end', values=item)

    def _change_column_labels(self,tree, table):
        # Clear existing headers
        for col in tree["columns"]:
            tree.heading(col, text="")

        if table == "Items":
            print("this is from items")
            self.table = self.inventoryController.get_items_column_names()
            for i, label in enumerate(self.table):
                tree.heading(tree["columns"][i], text=label)
            self._insert_data(self.inventoryController.get_items_on_database())
            print("this is from items2")
        if table == "Products":
            self.table = self.inventoryController.get_product_column_names()
            for i, label in enumerate(self.table):
                tree.heading(tree["columns"][i], text=label)
            self._insert_data(self.inventoryController.get_product_on_database())
        if table == "Recipes":
            self.table = self.inventoryController.get_recipe_column_names()
            for i, label in enumerate(self.table):
                tree.heading(tree["columns"][i], text=label)
            self._insert_data(self.inventoryController.get_recipe_on_database())
        return


        # Update headers with new labels

    def _update_table(self,table):
            # if table == "Supplies":
            #     self.table = self.inventoryController.get_items_column_names()
            #     self._insert_table_columns()
            #     self._insert_data(self.inventoryController.get_items_on_database())
        return

    def _nav_bar_label(self):
        self.navBarLabel =tk.Label(self.navBarFrame,font=font.Font(family='Courier New',size=14,weight='bold'),text=f"{self.menus[0]} Inventory",background=self.navBarBg)
        self.navBarLabel.place(relx=0.14,rely=0.5,anchor=CENTER)
            
    def _back_button(self):
        self.back_btn = tk.Button(self,font=font.Font(family='Courier New',size=9,weight='bold'), 
                                  text="Back", background="Grey89",command=lambda:self.inventoryController.manager_view())
        self.back_btn.place(relx=0.09,rely=0.9,anchor='s')