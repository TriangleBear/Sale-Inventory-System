from View import MainView
from View import Functions

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
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def register(self, data:list):
        self.model.registerUser(data)
        return 0

    def checkInput(self,credentials:list)->str:
        value = self.model.getLevelOfAccess(credentials)
        return value