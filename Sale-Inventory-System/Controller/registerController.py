from View import RegisterView
from Model import RegisterModel
from Utils import Functions

class RegisterController():
    def __init__(self,master):
        self.master = master
        self.view = RegisterView(self, self.master)

    def main(self):
        self.view.main()

    def register(self, data:list):
        reg_model = RegisterModel(data)
        return reg_model.create_user()

    def check_password_criteria(self, data:list):
        pass_model = RegisterModel(data)
        return pass_model.check_password_criteria() 
    

if __name__ == "__main__":
    import tkinter as tk
    registerController = RegisterController(tk.Tk)

    

    