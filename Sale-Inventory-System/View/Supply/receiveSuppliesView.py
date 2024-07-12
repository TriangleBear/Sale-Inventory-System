import tkinter as tk
from tkinter import font, ttk, CENTER, messagebox
from Utils import Functions
from PIL import Image,ImageTk
from icecream import ic
import copy

class ReceiveSuppliesView(tk.Toplevel):
    def __init__(self, receiveSuppliesController):
        self.receiveSuppliesController = receiveSuppliesController
        self._pending_orders = self.receiveSuppliesController.fetch_all_pending_orders()
        super().__init__(background="GhostWhite")
        self._window_attributes()
        self.mainBg = "Gray89"

        self.table_reorder = ['Item ID','Item Name', 'Amount to Pay', 'Quantity', 'Arrival Date','Ordered On','Status']


    @property
    def pending_orders(self):
        return copy.deepcopy(self._pending_orders)

    def main(self):
        self._header_frame()
        self._reorder_label()
        self._display_reorder_table()
        self._receive_button()
        self._refresh_button()
        self._back_button()
        self.mainloop()

    def _window_attributes(self):
        self.h = 690
        self.w = 880
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        image = Image.open('Assets\\icon.jpg')
        photo_image = ImageTk.PhotoImage(image)
        self.iconphoto(False, photo_image)
        self.title('Recieve Supplies')
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()

    def _header_frame(self):
        self.header_frame = tk.Frame(self, background=self.mainBg,width=880,height=40)
        self.header_frame.place(x=0,y=0)

    def _reorder_label(self):
        reorder_label = tk.Label(self.header_frame, font=font.Font(family='Courier New', size=14, weight='bold'),
                                  text="Unreceived Orders", background=self.mainBg)
        reorder_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def _display_reorder_table(self):
        self.tree_reorder = ttk.Treeview(self, 
                                         columns=self.table_reorder,
                                         show="headings",
                                         selectmode="browse")
        for col in self.table_reorder:
            self.tree_reorder.heading(col, text=col)
            self.tree_reorder.column(col, anchor='center')

        self.tree_reorder.bind('<Configure>', Functions.adjust_column_widths)
        self.tree_reorder.place(relx=0.5, rely=0.45, anchor=CENTER, width=790, height=500)
        self._insert_data(self.tree_reorder,Functions.convert_dicc_data(self.pending_orders))
                                
    def _insert_data(self, tree: ttk.Treeview, data: list):
        for item in data:
            tree.insert('', 0, values=item)

    def _receive_button(self):
        confirm_button = tk.Button(self, font=font.Font(family='Courier New', size=9, weight='bold'),
                                   text="Receive Order", command=lambda: self._on_receive())
        confirm_button.place(relx=0.9,rely=0.9,anchor='se')

    def _refresh_button(self):
        refresh_button = tk.Button(self,font=font.Font(family='Courier New', size=9, weight='bold'),
                                   text="Refresh", command=lambda: self.refresh_table())
        refresh_button.place(relx=0.7,rely=0.9,anchor='se')
        
    def refresh_table(self):
        self._pending_orders = self.receiveSuppliesController.fetch_all_pending_orders()
        self.tree_reorder.delete(*self.tree_reorder.get_children())
        self._insert_data(self.tree_reorder,Functions.convert_dicc_data(self.pending_orders))

    def _back_button(self):
        back_button = tk.Button(self, font=font.Font(family='Courier New', size=9, weight='bold'),
                                text="Back", command=lambda: self.destroy())
        back_button.place(relx=0.1,rely=0.9,anchor='sw')

    def _on_receive(self):
        selected_item = self.tree_reorder.item(self.tree_reorder.selection()[0],'values')
        if not selected_item:
            return messagebox.showerror("Error", "Please select an item to receive")
        self.receiveSuppliesController.add_to_items(selected_item)
        self.receiveSuppliesController.logUserActivity(selected_item[0])
        self.refresh_table()
        return messagebox.showinfo("Items Received",'Items have been added to Inventory')


