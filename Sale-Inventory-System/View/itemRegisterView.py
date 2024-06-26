from tkinter import *
import tkinter as tk
from tkinter import ttk

class ItemRegisterView(tk.Frame):
    def __init__(self,itemRegisterController,master):
        self.master = master
        super().__init__(self.master, background="GhostWhite")
        self.itemRegisterController = itemRegisterController
        self.pack(fill=tk.BOTH,expand=True)

        #frames attributes
        self.mainBg = 'Grey90'

    def main(self):
        self.item_register_frame()

    def item_register_frame(self):
        self.registerPage = tk.Frame(self,background=self.mainBg)
        self.registerPage.pack(fill=tk.BOTH,expand=True)

    def registered_display_table(self):
        self.tree = ttk.Treeview(self.registerPage, columns=("Item ID", "Item Name", "Item Description", "Item Price", "Item Quantity"), show='headings')
        self.tree.heading("Item ID", text="Item ID")
        self.tree.heading("Item Name", text="Item Name")
        self.tree.heading("Item Description", text="Item Description")
        self.tree.heading("Item Price", text="Item Price")
        self.tree.heading("Item Quantity", text="Item Quantity")
        # self.tree.pack()        

    def _back_button(self):
        back_btn = tk.Button(self.registerPage, text="Back", command=lambda: self.managerController.manager_body(self.master))
        back_btn.place(relx=0.9, rely=0.5,anchor=CENTER)
