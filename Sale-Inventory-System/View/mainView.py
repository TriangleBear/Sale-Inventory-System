import tkinter as tk
from View import *
from tkinter import *
from tkinter import font, ttk, messagebox

#initialization of

class MainView(tk.Tk):
    def __init__(self, mainController):
        super().__init__()
        self.mainController = mainController
        
        self._main_window_attributes() #set window attributes
        self._win_frame() # put a main frame inside main window
        self._start_button()

    def _main_window_attributes(self):
        #main window
        w = 580
        h = 420
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width/2) - (w/2))-12
        y = int((screen_height/2)-(h/2))-40

        self.title('S.I.M.S')
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.resizable(False,False)

    def main(self):
        self.protocol("WM_DELETE_WINDOW",self.quit())
        self.mainloop()

    def _win_frame(self):
        self.windowFrame = tk.Frame(self)
        self.windowFrame.pack(fill=tk.BOTH,expand=True)
        
    def _start_button(self):
        start_btn = tk.Button(self.windowFrame,font=font.Font(family='Poppins',weight='bold'),text="Start",borderwidth=0,background="Gray82", command=lambda:Functions.switch_page(self.windowFrame,self.mainController.loginController))
        start_btn.place(relx=0.5,rely=0.5,anchor=CENTER)