from View import LoginPage
from Model import LoginModel
class LoginController:
    def __init__(self,parentFrame):
        self.parentFrame = parentFrame #self.windowFrame
        self.view = LoginPage(self,self.parentFrame)

    def main(self):
        self.view.main()

    def checkInput(self, credentials):
        self.model = LoginModel(credentials)
        return self.model.getLevelOfAccess()

    def manager_dashboard(self,frame):
        from Controller import ManagerDashboard
        manager_page = ManagerDashboard(frame)
        self.model.provided_credentials

    def register_page(self):
        from Controller import RegisterPage
