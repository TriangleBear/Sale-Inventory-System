import tkinter as tk
from tkinter import ttk

class ReportView(tk.Frame):
    def __init__(self, reportController, master):
        self.master = master
        super().__init__(self.master, background="Gray90")
        self.reportController = reportController
        self.table = ['user_id', 'username', 'activity', 'datetime']

    def display_table(self):
        root = tk.Tk()
        root.title("User Activity Table")

        table_frame = ttk.Frame(root)
        table_frame.pack()

        table = ttk.Treeview(table_frame, columns=("User ID", "Username", "User Activity", "Datetime"), show="headings")
        table.pack()

        table.heading("User ID", text="User ID")
        table.heading("Username", text="Username")
        table.heading("User Activity", text="User Activity")
        table.heading("Datetime", text="Datetime")

        for row in self.table:
            table.insert("", "end", values=row)

        root.mainloop()