import tkinter as tk
from tkinter import ttk, messagebox, CENTER
import tkcalendar as tkc
from Utils import CustomDialog
from Utils import Functions
class ReportView(tk.Frame):
    def __init__(self,reportController,master):
        self.master = master
        self.mainBg = 'Grey89'
        super().__init__(self.master, background="Gray89")
        self.reportController = reportController
        self.pack(fill=tk.BOTH,expand=True)
        self.report_btn_lbls = ["Stock Level Report","Sales Report"]
        self.btns = []

        
        # self._display_graph()
        # self._back_button()

    def main(self):
        self._report_frame()
        self._report_buttons()
        pass

    def _report_frame(self):
        self.reportFrame = tk.Frame(self,background="GhostWhite")
        self.reportFrame.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _date_report(self):
        date_label = tk.Label(self.reportFrame, text="Date Report", font=('Courier', 12))
        date_label.grid(row=0,column=0)
        date_entry = tkc.DateEntry(self.reportFrame, width=12, background='darkblue', foreground='white', borderwidth=2)
        date_entry.grid(row=0,column=1)
        date_entry.config(font=('Courier', 12))
        date_entry._top_cal.overrideredirect(False)
        date_entry._top_cal.geometry('+500+300')
        date_entry._top_cal.withdraw()
        date_entry._calendar.pack()

    def _report_buttons(self):
        Functions.create_buttons_using_grid(self.reportFrame,
                                            labels=self.report_btn_lbls,
                                            entryList=self.btns,
                                            max_columns=1,
                                            w=21,
                                            h=1,
                                            fontSize=12,
                                            gridxPadding=10,
                                            gridyPadding=10,
                                            btnyPadding=2,
                                            btnxPadding=5,
                                            cmd=self._report_button_commands,
                                            )
        self._back_button()
     
    def _back_button(self): 
        back_btn = tk.Button(self, text="Back", font=('Courier', 12), command=self.reportController.manager_view)
        back_btn.place(relx=0.05,rely=0.05,anchor='nw')

    def _report_button_commands(self,string):
        if string == "Stock Level Report":
            self.reportController.display_stock_level()
        if string == "Sales Report":
            self.reportController.display_sales_report()