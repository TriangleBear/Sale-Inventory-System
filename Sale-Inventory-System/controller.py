import sys
from Model.model import User, Registration
from View.view import View

class Controller:
    def __init__(self):
        self.view = View(self)

    def main(self):
        self.view.main()

    def register(self, number, access, email, username, password):
        Registration.create_user(number, access, username, password, email)

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


if __name__ == '__main__':
    controller = Controller()
    controller.main()