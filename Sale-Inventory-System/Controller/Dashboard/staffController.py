from View import StaffDashboard
from Model import ManagerModel
from Utils import Functions

class StaffController:
    def __init__(self, master,user_id):
        self.master = master
        self.id =user_id
        self.view = StaffDashboard(self,self.master,self.id)
    
    def main(self):
        self.view.main()

    def posController(self,master):
        from Controller import PosController
        pos_page = PosController(self,master)
        pos_page.main()

    def forgotPasswordController(self,master):
        Functions.destroy_page(master)
        from Controller import ForgotPasswordController
        forgot_password = ForgotPasswordController(master)
        forgot_password.main()