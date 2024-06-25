from View import ManagerDashboard
from Model import ManagerModel
from Utils import Functions

class ManagerController:
    def __init__(self, master,user_id):
        self.master = master
        self.id =user_id
        self.view = ManagerDashboard(self,self.master,self.id)
    
    def main(self):
        self.view.main()

    def homePage(self,master):
        Functions.destroy_page(master)
        self.main()

    def loginController(self,master):
        Functions.destroy_page(master)
        from Controller import LoginController
        login_page = LoginController(master)
        login_page.main()