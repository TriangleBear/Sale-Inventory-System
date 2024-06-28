import tkinter as tk
from tkinter import ttk

class AuditView(tk.Frame):
    def __init__(self,AuditController, master):
        self.master = master
        self._main_window_attributes()
        super().__init__(self.master, background="GhostWhite")
        self.AuditController = AuditController
        self.pack(fill=tk.BOTH, expand=True)
        self.table_frame.pack()

    def main(self):
        self._header_frame()
        self._center_frame()
        self.display_table()
        self.display_entries(self.AuditController.model.get_entries())

    def _main_window_attributes(self):
        # main window
        self.h = 720
        self.w = 900
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        self.master.title('S.I.M.S')
        self.master.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.master.resizable(False, False)

    def _header_frame(self):
        self.headerFrame = tk.Frame(self,background=self.mainBg)
        self.headerFrame.place(x=0,y=0, width=900,height=45)
    
    def _center_frame(self):
        self.centerFrame = tk.Frame(self,background=self.mainBg)
        self.centerFrame.place(x=0,y=45, width=900,height=675)

    def _body_buttons(self):
        for i, btn in enumerate(self.main_btn_lbls):
            self.btns.append(ttk.Button(self.centerFrame, text=btn, width=20))
            self.btns[i].place(x=50, y=50 + (i * 50))
        
    def display_table(self):
        self.table = ttk.Treeview(self.table_frame, columns=("User ID", "Username", "User Activity", "Datetime"), show="headings")
        self.table.pack()

        self.table.heading("User ID", text="User ID")
        self.table.heading("Username", text="Username")
        self.table.heading("User Activity", text="User Activity")
        self.table.heading("Datetime", text="Datetime")

    def display_entries(self, entries):
        for entry in entries:
            self.table.insert('', 'end', values=entry)

    def _back_button(self, page):
        back_btn = ttk.Button(self.centerFrame, text="Back", width=20, command=lambda: self.managerController.show_page(page))
        back_btn.place(x=50, y=50 + (len(self.main_btn_lbls) * 50))