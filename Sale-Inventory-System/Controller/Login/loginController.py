from Utils import Functions
from View import LoginView
from Model import LoginModel
class LoginController:
    def __init__(self,master):
        self.master = master #window
        self.view = LoginView(self, self.master)

    def main(self):
        self.view.main()

    def managerController(self,master,user_id):
        Functions.destroy_page(master)
        from Controller import ManagerController
        manager_dashboard = ManagerController(master,user_id)
        manager_dashboard.main()

    def staffController(self,master,user_id):
        Functions.destroy_page(master)
        from Controller import StaffController
        staff_dashboard = StaffController(master, user_id)
        staff_dashboard.main()
    
    def forgotPasswordController(self,master):
        Functions.destroy_page(master)
        from Controller import ForgotPasswordController
        forgot_password = ForgotPasswordController(self,master)
        forgot_password.main()

    def logUserActivity(self,user_id):
        Functions.logUserActivity([user_id,"Logged In",Functions.get_current_date("datetime")])

    def checkInput(self, data:list):
        print(f"from checkInput;loginController|data:{data}")
        model = LoginModel(data)
        invalidInput = model.check_password()
        if invalidInput == 0:
            return [model.user_id,
                    model.get_user_type(),
                    model.get_user_email(),
                    model.get_login_otp()]
        else:
            return invalidInput

    def user_otp_verification(self, user_data:list):
        Functions.send_otp_email(user_data[2], user_data[3])#(user_data[2]:email,user_data[3]:otp)