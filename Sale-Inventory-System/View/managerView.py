from tkinter import font, CENTER
import tkinter as tk
class ManagerDashboard(tk.Frame):
    def __init__(self,managerController,master,user_id):
        self.master = master
        super().__init__(self.master)
        self.managerController = managerController
        self.user_id = user_id
        self.pack(fill=tk.BOTH,expand=True)
    
    def main(self):
        self._main_window_attributes()
        self._manager_frame()
        self._temp_label()
        self._register_button()
        self._inventory_button()
        self._supplies_button()
        self._pos_button()

    def _main_window_attributes(self):
        # main window
        w = 900
        h = 720
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (w / 2)) - 12
        y = int((screen_height / 2) - (h / 2)) - 40

        self.master.title('S.I.M.S')
        self.master.geometry(f"{w}x{h}+{x}+{y}")
        self.master.resizable(False, False)

    def _manager_frame(self):
        self.managerFrame = tk.Frame(self,background="GhostWhite")
        self.managerFrame.pack(fill=tk.BOTH,expand=True)

    def _temp_label(self):
        temp_label = tk.Label(self.managerFrame,text=f"manager dasherboard | user ID: {self.user_id}")
        temp_label.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _register_button(self):
        self.register_btn = tk.Button(self.managerFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Register", command=lambda:self.managerController.registerController(self.master))
        self.register_btn.pack()
