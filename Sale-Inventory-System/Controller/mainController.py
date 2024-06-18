from View import MainView

class MainController:
    def __init__(self):
        self.view = MainView(self)

    def main(self):
        self.view.main()
    
    def login_page(self,frame):
        from Controller import LoginController
        login_page = LoginController(frame)
        login_page.main()
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def register(self, data:list):
        self.model.registerUser(data)
        return 0

    def checkInput(self,credentials:list)->str:
        value = self.model.getLevelOfAccess(credentials)
        return value