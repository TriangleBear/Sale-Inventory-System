from tkinter import font, CENTER
import tkinter as tk
class SuppliesView(tk.Frame ):
    def __init__(self,master,user_id):
        self.master = master
        self.user_id = user_id
        self.pack(fill=tk.BOTH,expand=True)

    def main(self):
        self._main_window_attributes()
        self._supplies_frame()
        self._temp_label()

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

    def _supplies_frame(self):
        self.suppliesFrame = tk.Frame(self,background="GhostWhite")
        self.suppliesFrame.pack(fill=tk.BOTH,expand=True)

    def _temp_label(self):
        temp_label = tk.Label(self.suppliesFrame,text=f"supplies dasherboard | Hello! {self.username}")
        temp_label.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _back_button(self):
        self.back_btn = tk.Button(self.suppliesFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Back", command=lambda:self.posController.managerController(self.master))
        self.back_btn.pack()