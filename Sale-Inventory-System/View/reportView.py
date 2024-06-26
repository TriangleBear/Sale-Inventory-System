import tkinter as tk
from tkinter import ttk

class ReportView:
    def __init__(self):
        self.table = []

    def add_activity(self, user_id, username, activity, datetime):
        self.table.append((user_id, username, activity, datetime))

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