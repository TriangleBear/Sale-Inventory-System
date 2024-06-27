import tkinter as tk
from tkinter import ttk
class ReportView(tk.Frame):
    def __init__(self, reportController, master):
        self.master = master
        super().__init__(master)
        self.reportController = reportController
        self.table = ['Log ID', 'User ID', 'Activiy Log', 'Date and Time Logged']
    
    def main(self):
        self.display_table()
        self.insert_data()
        self.create_widgets()
        self._back_button()
        self._search_entry()
        self._search_button()


    def create_widgets(self):
        self.pack(expand=True, fill='both')  # Ensure the frame expands to fill available space
    
    def insert_data(self):
        data = self.reportController.fetch_data_from_user_activity()
        if data is None:
            data = []
        for row in data:
            # Convert dictionary row to a list in the order of self.table columns
            if isinstance(row, dict):
                try:
                    row = [row['log_id'], row['user_id'], row['user_log'], row['created_on']]
                except KeyError as e:
                    print(f"Missing key in row data: {e}")
                    continue
            elif not isinstance(row, (list, tuple)) or len(row) != len(self.table):
                print(f"Row format error: {row}")
                continue
            self.tree.insert('', 'end', values=row)

    def display_table(self):
        self.tree = ttk.Treeview(self, columns=self.table, show='headings')
        for col in self.table:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor='center')
        self.tree.pack(expand=True, fill='both')

    def _search_entry(self):
        search_entry = tk.Entry(self)
        search_entry.pack(side='top', pady=10)  # Place the entry at the top with some padding

    def _search_button(self):
        search_button = tk.Button(self, text="Search", command=self.reportController.search_data)
        search_button.pack(side='bottom', pady=10)  # Place the button at the bottom with some padding

    def _back_button(self):
        back_button = tk.Button(self, text="Back to Manager View", command=self.reportController.back_to_manager_view)
        back_button.pack(side='bottom', pady=10)  # Place the button at the bottom with some padding