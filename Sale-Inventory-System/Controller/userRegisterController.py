from View import UserRegisterView
from Model import UserRegisterModel
from Utils import Functions

class UserRegisterController():
    def __init__(self,master,managerController):
        self.master = master
        self.managerController = managerController
        self.view = UserRegisterView(self, self.master)

    def main(self):
        self.view.main()

    def register(self, data:list):
        reg_model = UserRegisterModel(data)
        return reg_model.create_user()

    def check_password_criteria(self, data:list):
        pass_model = UserRegisterModel(data)
        return pass_model.check_password_criteria()
    
    def manager_body(self,master):
        Functions.destroy_page(master)
        self.managerController.view.register_page()

    

    