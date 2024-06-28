import tkinter as tk
from tkinter import ttk,font
from Utils import Functions
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
        self.insert_data(self.securityController.fetch_data_from_user_activity())
        self._user_log_lbl()
        self._search_entry()
        self._search_button() # Ensure the frame expands to fill available space
        self._refresh_button()
        self._back_button()
    
    def table_frame(self):
        self.tableFrame = tk.Frame(self,background=self.mainBg)
        self.tableFrame.place(relx=0.5,rely=0.5,anchor='center')
        
    def display_table(self):
        self.tree = ttk.Treeview(self.tableFrame, columns=self.table, show='headings')
        for col in self.table:
            self.tree.heading(col, text=col)    
            self.tree.column(col, anchor='center')
        self.tree.pack(fill='both', expand=True)
        
    def insert_data(self,data):
        self.tree.delete(*self.tree.get_children())
        converted_data = Functions.convert_dicc_data(data)
        for item in converted_data:
            self.tree.insert('', 'end', values=item)

    def search_data(self, search_query):
        search_results = self.securityController.search_data(search_query)
        self.insert_data(search_results)

    def _search_entry(self):
        self.search_entry = tk.Entry(self, borderwidth=0, width=23,font=font.Font(size=12))
        self.search_entry.place(relx=0.9, rely=0.25,anchor='e')  # Place the entry at the top with some padding

    def _user_log_lbl(self):
        self.user_loglbl = tk.Label(self, background=self.mainBg,font=font.Font(family='Courier New',size=12,weight='bold'),text="User Log Activity")
        self.user_loglbl.place(relx=0.03,rely=0.25,anchor='w')

    def _search_button(self):
        search_button = tk.Button(self, font=font.Font(family='Courier New', size=9, weight='bold'), text="Search",
                                    command=lambda: self.search_data(self.search_entry.get()), padx=7, pady=2)
        search_button.place(relx=0.64,rely=0.25, anchor='e')  # Place the button at the bottom with some padding

    def _back_button(self):
        back_button = tk.Button(self, font=font.Font(family='Courier New',size=9,weight='bold'),text="Back", command=lambda:self.securityController.manager_view())
        back_button.place(relx=0.1,rely=0.9,anchor='sw')  # Place the button at the bottom with some padding

    def _refresh_button(self):
        refresh_button = tk.Button(self, font=font.Font(family='Courier New',size=9,weight='bold'),text="Refresh", 
                                   command=lambda:self.insert_data(self.securityController.fetch_data_from_user_activity()))
        refresh_button.place(relx=0.9,rely=0.9,anchor='se')