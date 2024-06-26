from View import MainView
from Utils import Functions

class MainController:
    def __init__(self):
        self.view = MainView(self)

    def main(self):
        self.view.main()
    
    def loginController(self,master):
        Functions.destroy_page(master)
        from Controller import LoginController
        login_page = LoginController(master)
        login_page.main()
    
    def registerController(self,master):
        Functions.destroy_page(master)
        from Controller import RegisterController
        register_page = RegisterController(master)
        register_page.main()

    def managerController(self,master,user_id):
        Functions.destroy_page(master)
        from Controller import ManagerController
        manager_dashboard = ManagerController(master,user_id)
        manager_dashboard.main()
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def register(self, data:list):
        self.model.registerUser(data)
        return 0

    def checkInput(self,credentials:list)->str:
        value = self.model.getLevelOfAccess(credentials)
        return value