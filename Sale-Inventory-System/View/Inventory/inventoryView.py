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

    def _inventory_widgets(self):
        self._back_button()

    def _inventory_frame(self):
        self.inventoryFrame = tk.Frame(self,background="GhostWhite")
        self.inventoryFrame.pack(fill=tk.BOTH,expand=True)
    
    def _entry_frame(self):
        self.entryFrame = tk.Frame(self.inventoryFrame,background="Gray82")
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)
            
    def _back_button(self):
        back_btn = tk.Button(self.entryFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Back", command=lambda:self.destroy())
        back_btn.grid(row=5,column=2,sticky='e',padx=5,pady=5)