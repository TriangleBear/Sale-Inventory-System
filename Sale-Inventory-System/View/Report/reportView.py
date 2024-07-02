import tkinter as tk
from tkinter import ttk, messagebox
from Utils import Functions
class ReportView(tk.Frame):
    def __init__(self,reportController,master):
        self.master = master
        self.mainBg = 'Grey89'
        super().__init__(self.master, background="GhostWhite")
        self.reportController = reportController
        self.pack(fill=tk.BOTH,expand=True)

    def main(self):
        self._display_graph()
        self._back_button()

    def _stock_level_display_btn(self):
        stock_level_btn = tk.Button(self, text="Stock Level", font=('Courier', 12), command=self.reportController.display_stock_level)
        stock_level_btn.place(relx=0.05,rely=0.05,anchor='nw')
            
    def _back_button(self):
        back_btn = tk.Button(self, text="Back", font=('Courier', 12), command=self.reportController.managerController)
        back_btn.place(relx=0.05,rely=0.05,anchor='nw')