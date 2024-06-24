from Utils import Functions
from View import ForgotPasswordView
from Model import ForgotPasswordModel
class ForgotPasswordController:
    def __init__(self,master):
        self.master = master
        self.view = ForgotPasswordView(self,self.master)
    
    def main(self):
        self.view.main()

    def checkPassInput(self,data:list):
        old_password = data[0]
        username = data[2]
        password_model = ForgotPasswordModel(provided_username=username,old_password=old_password)
        return password_model.check_old_password()

    def checkUsernameInput(self,provided_username):
        username_model = ForgotPasswordModel(provided_username=provided_username)
        return username_model.check_provided_username()


    def checkAccountInputs(self, data:list):
        provided_username = data[0]
        provided_email = data[1]
        email_model = ForgotPasswordModel(provided_email=provided_email,provided_username=provided_username)
        if email_model.check_provided_username() and email_model.check_user_email():
            return [email_model.provided_username,email_model.provided_email,email_model.get_forgot_password_otp()]
    
    def user_otp_verification(self, user_data:list):
        Functions.send_otp_email(user_data[1], user_data[2])