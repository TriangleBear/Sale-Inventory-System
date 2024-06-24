from View import RegisterView
from Model import RegisterModel

class RegisterController():
    def __init__(self,master):
        self.master = master
        self.view = RegisterView(self, self.master)

    def main(self):
        self.view.main()

    def check_password_criteria(self, data:list):
        self.model = RegisterModel(data)
        return self.model.check_password_criteria()
    

if __name__ == "__main__":
    import tkinter as tk
    registerController = RegisterController(tk.Tk)

    

    