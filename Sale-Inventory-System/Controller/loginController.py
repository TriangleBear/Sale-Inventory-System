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
        # else:
        #     return "Incorrect password"
        # else:
        #     return "No such user was found"

    def user_otp_verification(self, user_data:list):
        self.model.send_otp_email(user_data[1], user_data[2])

    # self.controller.send_otp_email(email, otp) # Replace send_otp_email() with your email sending logic
        

    #     message = askstring('OTP Verification', 'Enter OTP sent to your email')
    #     print(message)
    #     #print(f'FROM otp_verification: {message}')
    #     try:
    #         if message == otp:
    #             self._switch_page(self._login_page)
    #     except Exception as e:
    #         print(f'Error: {e}')
    #         messagebox.showerror('OTP Verification Error', 'Invalid OTP')
