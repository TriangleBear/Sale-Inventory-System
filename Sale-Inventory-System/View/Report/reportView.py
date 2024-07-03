import tkinter as tk
from tkinter import ttk, messagebox, CENTER, simpledialog
from tkcalendar import Calendar, DateEntry
from Utils import Functions
from datetime import datetime
class ReportView(tk.Frame):
    def __init__(self,reportController,master):
        self.master = master
        self.mainBg = 'Grey89'
        super().__init__(self.master, background="Gray89")
        self.reportController = reportController
        self.fetch_report_button = tk.Button(text="Fetch Report", command=self.on_fetch_report_clicked)
        self.pack(fill=tk.BOTH,expand=True)
        self.report_btn_lbls = ["Stock Level Report","Sales Report"]
        self.btns = []

        
        # self._display_graph()
        # self._back_button()

    def main(self):
        self._report_frame()
        self._report_buttons()

    def _report_frame(self):
        self.reportFrame = tk.Frame(self,background="GhostWhite")
        self.reportFrame.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _date_report(self):
        date_label = tk.Label(self.reportFrame, text="Date Report", font=('Courier', 12))
        date_label.grid(row=0,column=0)
        date_entry = DateEntry(self.reportFrame, width=12, background='darkblue', foreground='white', borderwidth=2)
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

    def on_fetch_report_clicked(self):
        date = self.get_selected_date()  # Method to get the date from the UI
        self.reportController.get_sales_report(date)
     
    def _back_button(self): 
        back_btn = tk.Button(self, text="Back", font=('Courier', 12), command=self.reportController.manager_view)
        back_btn.place(relx=0.05,rely=0.05,anchor='nw')

    def _report_button_commands(self,string):
        if string == "Stock Level Report":
            self.reportController.display_stock_level()
        if string == "Sales Report":
            self._ask_for_date_and_display_sales_report() 
    
    def _ask_for_date_and_display_sales_report(self):
        # Create a simple dialog to ask for the date
        def on_date_selected():
            # Assuming date_entry.get() returns a date string, e.g., "MM/DD/YYYY"
            date_str = date_entry.get()

            # Parse the date string into a datetime object
            date_obj = datetime.strptime(date_str, "%m/%d/%y")  # Use '%y' for two-digit year

            # Format the datetime object for MySQL
            mysql_date_str = date_obj.strftime('%Y-%m-%d')
            print(f"Selected date view: {mysql_date_str}")
            try:
                self.reportController.display_sales_report(mysql_date_str)
            except Exception as e:
                print(f"Error in displaying sales report: {e}")                                     
            dialog.destroy()  # Destroy the dialog after selection

        dialog = tk.Toplevel(self)  # Use the existing root window
        dialog.title("Select Date")
        date_entry = DateEntry(dialog)  # Create a DateEntry widget
        date_entry.pack(pady=10)
        select_button = tk.Button(dialog, text="Select", command=on_date_selected)
        select_button.pack(pady=5)
        print(f"date_entry: {date_entry.get()}")
        dialog.transient(self)  # Make the dialog transient to the root window
        dialog.grab_set()  # Optional: Make the dialog modal
        self.wait_window(dialog)