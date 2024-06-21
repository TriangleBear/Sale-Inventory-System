from View import LoginView
from Model import LoginModel
from View import Functions
class LoginController:
    def __init__(self,master):
        self.master = master #self.windowFrame
        self.view = LoginView(self, self.master)

    def main(self):
        self.view.main()
    
    def checkInput(self, data:list):
        self.model = LoginModel(data)
        self.userType = self.model.get_user_type()
        self.storedPassword = self.model.get_user_password()
        self.email = self.model.get_user_email()
        self.otp = self.model.get_login_otp()
        if self.storedPassword == self.model.password:
                return [self.userType, self.email, self.otp]

    def user_otp_verification(self, user_data:list):
        self.model.send_otp_email(user_data[1], user_data[2])