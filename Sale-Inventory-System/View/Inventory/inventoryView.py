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
        self.table = []
        self.pack(fill=tk.BOTH,expand=True)

    def main(self):
        self._inventory_frame()  
        self._entry_frame()
        self._inventory_widgets()

    def _inventory_widgets(self):
        self._back_button()

    def _nav_bar_frame(self):
        w = self.master.winfo_width()
        h = 23
        self.navBarFrame = tk.Frame(self,background="GhostWhite")
        self.navBarFrame.place(relx=0,rely=0,width=w,height=h)

    def _tree_dropdown(self):
        self.selectTable = ttk.Combobox(self.navBarFrame,values=self.menus)
        self.selectTable.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.selectTable.bind('<<ComboboxSelected>>', lambda event: self._update_table(self.selectTable.get()))
        self.selectTable.set(self.menus[0])

    def display_table(self):
        self.tree = ttk.Treeview(self, columns=self.table, show='headings',selectmode='browse')
        for col in self.table:
            self.tree.heading(col, text=col)    
            self.tree.column(col, anchor='center')
        self.tree.bind('<Configure>',Functions.adjust_column_widths)

    def _update_table(self,table):
        self.tree

    def _nav_bar_label(self):
        self.navBarLabel =tk.Label(self.navBarFrame,font=font.Font(family='Courier New',size=9,weight='bold'),text=)
    
    def _entry_frame(self):
        self.entryFrame = tk.Frame(self.inventoryFrame,background="Gray82")
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)
            
    def _back_button(self):
        back_btn = tk.Button(self.entryFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Back", command=lambda:self.destroy())
        back_btn.grid(row=5,column=2,sticky='e',padx=5,pady=5)