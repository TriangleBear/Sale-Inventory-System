import tkinter as tk
from tkinter import font, CENTER
class PosView(tk.Frame):
    def __init__(self,posController,master):
        self.master = master
        super().__init__(self.master)
        self.posController = posController

    def main(self):
        self._main_window_attributes()
        self._pos_frame()
        self._temp_label()
        self._back_button()

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

    def _pos_frame(self):
        self.posFrame = tk.Frame(self,background="GhostWhite")
        self.posFrame.pack(fill=tk.BOTH,expand=True)

    def _temp_label(self):
        temp_label = tk.Label(self.posFrame,text="POS")
        temp_label.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _back_button(self):
        self.back_btn = tk.Button(self.posFrame,font=font.Font(family='Courier New',size=9,weight='bold'), text="Back", command=lambda:self.posController.managerController(self.master))
        self.back_btn.pack()