from Utils import Functions
from View import LoginView
from Model import LoginModel
class LoginController:
    def __init__(self,master):
        self.master = master #window
        self.view = LoginView(self, self.master)

    def main(self):
        self.view.main()

    def _switch_page(self,page):
        self.loginController._switch_page(page)

    def staffPage(self,master,user_id):
        Functions.destroy_page(master)
        from Controller import StaffController
        staff_dashboard = StaffController(master,user_id)
        staff_dashboard.main()
    
    def forgotPasswordController(self,master):
        Functions.destroy_page(master)
        from Controller import ForgotPasswordController
        forgot_password = ForgotPasswordController(master)
        forgot_password.main()


    def checkInput(self, data:list):
        self.model = LoginModel(data)
        userId = self.model.get_user_id()
        userType = self.model.get_user_type()
        storedPassword = self.model.get_user_password()
        email = self.model.get_user_email()
        otp = self.model.get_login_otp()
        if userId == None:
            return ValueError("Invalid Username or Password")
        elif self.model.check_password:
            return [userId,userType,email,otp]

    def user_otp_verification(self, user_data:list):
        Functions.send_otp_email(user_data[2], user_data[3])#(user_data[2]:email,user_data[3]:otp)