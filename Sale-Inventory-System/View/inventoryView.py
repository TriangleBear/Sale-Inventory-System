from tkinter import *
import tkinter as tk
from Utils import Functions
from tkinter import font, messagebox
from tkcalendar import DateEntry
class InventoryView(tk.Frame):
    def __init__(self,inventoryController,managerController,master):
        self.inventoryController = inventoryController
        self.managerController = managerController
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

    def _inventory_frame(self):
        self.inventoryFrame = tk.Frame(self,background="GhostWhite")
        self.inventoryFrame.pack(fill=tk.BOTH,expand=True)
    
    def _entry_frame(self):
        self.entryFrame = tk.Frame(self.inventoryFrame,background="Gray82")
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)
    
    def _inventory_widgets(self):
        subset_one = {key:self.inventory_labels_with_colspan[key] for key in ["Product ID","Product Name","Quantity","Supplier"] if key in self.inventory_labels_with_colspan}
        Functions.create_entry_box_using_grid(frame=self.entryFrame,
                                              labels=subset_one,
                                              entryList=self.inventory_entry_boxes,
                                              max_columns=2,
                                              entryWidth=54)
        self._inventory_birthdate_widget()
        subset_two = {key:self.inventory_labels_with_colspan[key] for key in ["Expiration Date","Menu","Cost","Category"] if key in self.inventory_labels_with_colspan}
        Functions.create_entry_box_using_grid(frame=self.entryFrame,
                                              labels=subset_two,
                                              entryList=self.inventory_entry_boxes,
                                              max_columns=2,
                                              current_r=2,
                                              current_c=0,
                                              entryWidth=54)
        self.inventoryController._get_products_on_database()

    def _back_to_manager_button(self):
        self.back_btn = tk.Button(self.inventoryFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Back", command=lambda:self.managerController.managerController.main())
        self.back_btn.pack()