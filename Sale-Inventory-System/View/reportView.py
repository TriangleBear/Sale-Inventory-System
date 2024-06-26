import tkinter as tk
from tkinter import ttk

class ReportView(tk.Frame):
    def __init__(self, reportController, master):
        self.master = master
        super().__init__(master)
        self.reportController = reportController
        self.table = ['user_id', 'username', 'activity', 'datetime']
    
    def main(self):
        self.display_table()
        self.pack()
        self.insert_data()

    def insert_data(self):
        # Fetch data from the model
        data = self.reportController.fetch_data_from_user_activity()
        # Insert data into the treeview
        for row in data:
            self.tree.insert('', 'end', values=row)

    def display_table(self):
        # Create a treeview with 4 columns
        self.tree = ttk.Treeview(self, columns=self.table, show='headings')
        # Set column headings
        for col in self.table:
            self.tree.heading(col, text=col)
        self.tree.pack()
        # Insert data into the treeview
        self.insert_data()