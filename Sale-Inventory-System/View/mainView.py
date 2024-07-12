# mainView.py adjustment
import tkinter as tk
from tkinter import font, ttk, messagebox
from PIL import Image, ImageTk

class MainView(tk.Tk): 
    def __init__(self, mainController):
        super().__init__()
        self.mainController = mainController
        self._main_window_attributes()  # set window attributes
        # self._start_button()
        self.managerController()
        # self.loginController()
        # self.staffController()
        # self.registerController()

    def _main_window_attributes(self):
        # main window
        w = 580
        h = 420
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (w / 2)) - 12
        y = int((screen_height / 2) - (h / 2)) - 40

        # Set the window icon
        self.iconphoto(False, ImageTk.PhotoImage(Image.open("Assets\\icon.jpg")))
        self.title('Tapsi Ni Vivian at Bulaluhan')
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.resizable(False, False)

    def _start_button(self):
        self.start_btn = tk.Button(self, text="Start", font=font.Font(family='Courier New', size=12, weight='bold'), 
                                   command=lambda: self.temp_access_ingredientRegister())## remove start
        self.start_btn.place(relx=0.5,rely=0.5,anchor='center')

    def main(self):
        self.protocol("WM_DELETE_WINDOW", self.quit())
        self.mainloop() 

    def loginController(self):
        self.mainController.loginController(self)

    def registerController(self):
        self.mainController.registerController(self)
    
    def managerController(self):
        self.mainController.managerController(self,'M1203') #test user id
    
    def temp_access_ingredientRegister(self):
        self.mainController.ingredientRegisterController('R4461')

    def staffController(self):
        self.mainController.staffController(self,'S1203') #test user id
