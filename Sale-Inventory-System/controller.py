#controller.py
from Model.loginModel import LoginModel
from Model.registerModel import RegisterModel
from View.view import View

class Controller:
    def __init__(self):
        self.view = View(self)

    def main(self):
        self.view.main()

    def register(self, user_id, access, first, last, username, password, email):
        RegisterModel.create_user(user_id, access, first, last, username, password, email)

    def checkInput(self, username, password):
        user = LoginModel.check_username(username)
        stored_password = LoginModel.get_password(username)

        if stored_password is not None:  # Assuming 'password' is the column name in the database
            if LoginModel.check_password(stored_password, password):
                return user['user_type']  # Assuming 'user_type' is the column name in the database
            else:
                return "Incorrect password"
        else:
            return "No such user was found"
    
    # def otp_verify(self, otp, email, username):
    #     generated_otp = self.get_otp()
    #     emaildata = self.get_email(username)
        
    def check_password_criteria(self,first, last, username, password, email):
        return RegisterModel.check_password_criteria(first, last, username, password, email)

    def get_user_id(self, username):
        return LoginModel.check_username(username)
    
    def get_email(self, username):
        return LoginModel.get_email(username)
    
    def get_otp(self):
        return LoginModel.generate_otp()
    
    def send_otp_email(self, email, otp):
        LoginModel.send_otp_email(email, otp)

    # def validate_otp(otp, user_input):
    #     return otp == user_input

if __name__ == '__main__':
    controller = Controller()
    controller.main()