import tkinter as tk
from Utils import Functions
class MaintenanceView(tk.Frame):
    def __init__(self, maintenanceController, master):
        self.master = master
        self.mainBg = "Grey89"
        super().__init__(self.master, background=self.mainBg)
        self.maintenanceController = maintenanceController
        self.pack(fill=tk.BOTH, expand=True)

        self.main_btn_lbls = ['Edit Data', 'Backup Data', 'Software Update']
        self.btns = []

    def main(self):
        pass

    def _buttons_frame(self):
        self.headerFrame = tk.Frame(self, background=self.mainBg)
        self.headerFrame.place(relx=0.01, rely=0.05, anchor='nw')

    def _maintenance_buttons(self):
        Functions.create_buttons_using_grid(
            self.headerFrame,
            labels=self.main_btn_lbls,
            entryList=self.btns,
            max_columns=1,
            w=21,
            h=1,
            fontSize=12,
            gridxPadding=2,
            gridyPadding=3,
            btnyPadding=2,
            btnxPadding=2,
            cmd=self._maintenance_button_commands
        )

    def _maintenance_button_commands(self, btn):
        if btn == 'Edit Data':
            pass
        elif btn == 'Backup Data':
            pass
        elif btn == 'Software Update':
            pass