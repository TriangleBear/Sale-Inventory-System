from Utils import Functions
from View import LoginView
from Model import LoginModel
class LoginController:
    def __init__(self,master):
        self.master = master #window
        self.view = LoginView(self, self.master)

    def main(self):
        self.view.main()

    def managerPage(self,master,user_id):
        Functions.destroy_page(master)
        from Controller import ManagerController
        manager_dashboard = ManagerController(master,user_id)
        manager_dashboard.main()
    
    def forgotPasswordController(self,master):
        Functions.destroy_page(master)
        from Controller import ForgotPasswordController
        forgot_password = ForgotPasswordController(master)
        forgot_password.main()


    def checkInput(self, data:list):
        self.model = LoginModel(data)
        self.userId = self.model.get_user_id()
        self.userType = self.model.get_user_type()
        self.storedPassword = self.model.get_user_password()
        self.email = self.model.get_user_email()
        self.otp = self.model.get_login_otp()
        if self.model.check_password:
            return [self.userId,self.userType, self.email, self.otp]

    def user_otp_verification(self, user_data:list):
        self.model.send_otp_email(user_data[2], user_data[3])#(user_data[2]:email,user_data[3]:otp)