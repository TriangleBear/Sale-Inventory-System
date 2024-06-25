from Utils import Functions
from View import ForgotPasswordView
from Model import ForgotPasswordModel
class ForgotPasswordController:
    def __init__(self,master):
        self.master = master
        self.view = ForgotPasswordView(self,self.master)
    
    def main(self):
        self.view.main()

    def update_password(self,data:list):
        pass

    def checkPassInput(self,data:list):
        password_model = ForgotPasswordModel()
        pass

    def checkAccountInput(self, data:list):
        email_model = ForgotPasswordModel(provided_username=data[0]
                                          ,provided_email=data[1])
        noAccount = email_model.check_account_existence()
        
        if noAccount == 0: 
            return [email_model.provided_username,email_model.provided_email,email_model.get_forgot_password_otp()]
        else: 
            return noAccount
    
    def loginController(self,master):
        Functions.destroy_page(master)
        from Controller import LoginController
        login_page = LoginController(master)
        login_page.main()


    def user_otp_verification(self, user_data:list):
        Functions.send_otp_email(user_data[1], user_data[2])