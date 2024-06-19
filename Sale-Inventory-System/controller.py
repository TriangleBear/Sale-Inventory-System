#controller.py
from Model.loginModel import User
from Model.registerModel import Registration
from View.view import View

class Controller:
    def __init__(self):
        self.view = View(self)

    def main(self):
        self.view.main()

    def register(self, user_id, access, email, username, password):
        Registration.create_user(user_id, access, username, password, email)

    def checkInput(self, username, password):
        user = User.check_username(username)
        stored_password = User.get_password(username)
        if user is not None:  # Assuming 'password' is the column name in the database
            if User.check_password(stored_password, password):
                return user.get('user_type')  # Assuming 'user_type' is the column name in the database
            else:
                return "Incorrect password"
        else:
            return "No such user was found"
        
    def get_user_id(self, username):
        return User.check_username(username)
    
    def get_email(self, username):
        return User.get_email(username)
    
    def get_otp(self):
        return User.generate_otp()
    
    def send_otp_email(self, email, otp):
        User.send_otp_email(email, otp)

    def validate_otp(otp, user_input):
        return otp == int(user_input)

if __name__ == '__main__':
    controller = Controller()
    controller.main()