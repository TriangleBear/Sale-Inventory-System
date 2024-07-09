import tkinter as tk
from tkinter import font, ttk, CENTER
from Utils import Functions
class ReceiveSuppliesView(tk.Toplevel):
    def __init__(self, managerController, receiveSuppliesController, reorder_items=None):
        self.mC = managerController
        self.receiveSuppliesController = receiveSuppliesController
        self.reorder_items = reorder_items
        super().__init__(background="Gray89")
        self._window_attributes()
        self.mainBg = "Gray89"

        self.table_reorder = ['Product Name', 'Quantity', 'Price', 'Arrival Date']

    def main(self):
        self._entry_frame()
        self._reorder_label()
        self._display_reorder_table()
        self._reieve_button()
        self._back_button()
        self.mainloop()

    def _window_attributes(self):
        self.h = 420
        self.w = 580
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        self.title('Recieve Supplies')
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()

    def _entry_frame(self):
        self.entryFrame = tk.Frame(self, background=self.mainBg, padx=40, pady=80)
        self.entryFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def _reorder_label(self):
        reorder_label = tk.Label(self, font=font.Font(family='Courier New', size=14, weight='bold'),
                                  text="Supplies Items", background=self.mainBg)
        reorder_label.place(relx=0.5, rely=0.38, anchor=CENTER)

    def _display_reorder_table(self):
        self.tree_reorder = ttk.Treeview(self, 
                                         columns=self.table_reorder,
                                         show="headings",
                                         selectmode="browse")
        for col in self.table_reorder:
            self.tree_reorder.heading(col, text=col)
            self.tree_reorder.column(col, anchor='center')

        self.tree_reorder.bind('<Configure>', Functions.adjust_column_widths)
        self.tree_reorder.place(relx=0.5, rely=0.5, anchor=CENTER, width=200, height=200)
        self._insert_reorder_data()

    def _load_reorder_items(self):
        self.tree_reorder.delete(*self.tree_reorder.get_children())
        reorder_items = Functions.convert_dicc_data(self.receiveSuppliesController.fetch_items_below_or_equal_flooring())
                                
        

    def _reieve_button(self):
        confirm_button = tk.Button(self.entryFrame, font=font.Font(family='Courier New', size=9, weight='bold'),
                                   text="Recieve", command=lambda: self._on_receive())
        confirm_button.grid(row=2, column=0)

    def _back_button(self):
        back_button = tk.Button(self.entryFrame, font=font.Font(family='Courier New', size=9, weight='bold'),
                                text="Back", command=lambda: self.destroy())
        back_button.grid(row=2, column=2)

    def _on_receive(self):
        try:
            # Your logic for receiving supplies goes here
            print("Receive button pressed")
            # Example: self.receiveSuppliesController.receive_supplies(self.reorder_items)
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {e}")
