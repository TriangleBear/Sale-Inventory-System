from View import ManagerDashboard
from Model import ManagerModel
from Utils import Functions

class ManagerController:
    def __init__(self, master,user_id=None):
        self.master = master
        self.id = user_id
        self.view = ManagerDashboard(self,self.master,self.id)
    
    def main(self):
        self.view.main()

    def loginController(self,master):
        Functions.destroy_page(master)
        from Controller import LoginController
        login_page = LoginController(master)
        login_page.main()

    def userRegisterController(self,master):
        Functions.destroy_page(master)
        from Controller import UserRegisterController
        user_register_page = UserRegisterController(master,self)
        user_register_page.main()

    def itemRegisterController(self,master):
        Functions.destroy_page(master)
        from Controller import ItemRegisterController
        item_register_page = ItemRegisterController(master,self)
        item_register_page.main()

    