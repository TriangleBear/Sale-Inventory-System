from View import LoginPage
from Model import LoginModel
class LoginController:
    def __init__(self,frame):
        self.windowFrame = frame #self.windowFrame
        self.view = LoginPage(self,self.windowFrame)

    def main(self):
        self.view.main()

    def checkInput(self, credentials):
        self.model = LoginModel(credentials)
        return self.model.getLevelOfAccess()

    # def manager_dashboard(self,frame):
    #     from Controller import ManagerDashboard
    #     manager_page = ManagerDashboard(frame)
    #     self.model.provided_credentials

    def register_page(self,frame):
        from Controller import RegisterController
        register_page = RegisterController(frame)
        register_page.main()
