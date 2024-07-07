import tkinter as tk
from Utils import Functions
class MaintenanceView(tk.Frame):
    def __init__(self, maintenanceController, master):
        self.master = master
        self.mainBg = "Grey89"
        super().__init__(self.master, background=self.mainBg)
        self.maintenanceController = maintenanceController
        self.main_btn_lbls = ['Edit Data', 'Backup Data', 'Software Update']
        self.pack(fill=tk.BOTH, expand=True)
        self.btns = []

    def main(self):
        self._buttons_maintenance_frame()
        self._maintenance_buttons()

    def _buttons_maintenance_frame(self):
        self.headerFrame = tk.Frame(self, background=self.mainBg)
        self.headerFrame.place(relx=0.5, rely=0.5, anchor='n')

    def _maintenance_buttons(self):
        Functions.create_buttons_using_grid(
            self.headerFrame,
            labels=self.main_btn_lbls,
            entryList=self.btns,
            max_columns=1,
            w=30,
            h=2,
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
        if btn == 'Backup Data':
            pass
        elif btn == 'Software Update':
            pass

    