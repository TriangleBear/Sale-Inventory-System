from View import StaffDashboard
from Model import ManagerModel
from Utils import Functions

class StaffController:
    def __init__(self, master,user_id,session):
        self.master = master
        self.user_id = user_id
        self.session = session
        self.view = StaffDashboard(self,self.master,self.user_id,self.session)
    
    def main(self):
        self.view.main()

    def posController(self,master):
        from Controller import PosController
        pos_page = PosController(self,master)
        pos_page.main()

    def forgotPasswordController(self,master,session,user_id):
        Functions.destroy_page(master)
        from Controller import ForgotPasswordController
        forgot_password = ForgotPasswordController(controller=self,master=master,session=session,user_id=user_id)
        forgot_password.main()

    def mainController(self):
        self.master.destroy()
        from Controller import MainController
        logout = MainController()
        logout.main()    
