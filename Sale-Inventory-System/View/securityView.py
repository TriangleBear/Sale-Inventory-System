import tkinter as tk
from tkinter import ttk,font
class SecurityView(tk.Frame):
    def __init__(self, securityController, master):
        self.master = master
        self.securityController = securityController
        super().__init__(master,background="Gray90")
        self.mainBg = 'Grey90'
        self.table = ['Log ID', 'User ID', 'Activiy Log', 'Date and Time Logged']
        self.pack(fill='both',expand=True)
    
    def main(self):
        self.table_frame()
        self.display_table()
        self.insert_data()
        self._search_entry()
        self._search_button() # Ensure the frame expands to fill available space
        self._refresh_button()
        self._back_button()
    
    def table_frame(self):
        self.tableFrame = tk.Frame(self,background=self.mainBg)
        self.tableFrame.place(relx=0.5,rely=0.5,anchor='center')
        
        
    def insert_data(self):
        data = self.securityController.fetch_data_from_user_activity()
        if data is None:
            data = []
        for row in data:
            # Convert dictionary row to a list in the order of self.table columns
            if isinstance(row, dict):
                try:
                    row = [row['log_id'], row['user_id'], row['user_log'], row['log_date']]
                except KeyError as e:
                    print(f"Missing key in row data: {e}")
                    continue
            elif not isinstance(row, (list, tuple)) or len(row) != len(self.table):
                print(f"Row format error: {row}")
                continue
            self.tree.insert('', 'end', values=row)

    def display_table(self):
        self.tree = ttk.Treeview(self.tableFrame, columns=self.table, show='headings')
        for col in self.table:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor='center')
        self.tree.pack(fill='both', expand=True)

    def update_display_table(self):
        # Clear the treeview
        self.tree.delete(*self.tree.get_children())
        self.insert_data()

    def search_data(self, search_query):
        # Clear the table
        self.tree.selection_remove(*self.tree.get_children())

        # Search for data based on the search query
        search_results = self.securityController.search_data(search_query)

        # Convert search results to a list of values for comparison
        search_values = []
        for row in search_results:
            if isinstance(row, dict):
                try:
                    row_values = [row['log_id'], row['user_id'], row['user_log'], row['log_date']]
                    search_values.append(row_values)
                except KeyError as e:
                    print(f"Missing key in row data: {e}")

        # Iterate through all items in the treeview
        for child in self.tree.get_children():
            item_values = self.tree.item(child, 'values')
            # If the item's values match any of the search results, select the item
            if list(item_values) in search_values:
                self.tree.selection_toggle(child)

    def _search_entry(self):
        self.search_entry = tk.Entry(self, borderwidth=0, width=23)
        self.search_entry.place(x=5, y=5)  # Place the entry at the top with some padding

    def _search_button(self):
        search_button = tk.Button(self, font=font.Font(family='Courier New', size=9, weight='bold'), text="Search",
                                    command=lambda: self.search_data(self.search_entry.get()), padx=5, pady=10)
        search_button.place(x=5, y=25)  # Place the button at the bottom with some padding

    def _back_button(self):
        back_button = tk.Button(self, font=font.Font(family='Courier New',size=9,weight='bold'),text="Back", command=lambda:self.securityController.manager_view())
        back_button.place(relx=0.1,rely=0.9,anchor='sw')  # Place the button at the bottom with some padding

    def _refresh_button(self):
        refresh_button = tk.Button(self, font=font.Font(family='Courier New',size=9,weight='bold'),text="Refresh", command=lambda:self.update_display_table())
        refresh_button.place(relx=0.9,rely=0.9,anchor='se')
