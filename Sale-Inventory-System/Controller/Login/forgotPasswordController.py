from Utils import Functions
from View import ForgotPasswordView
from Model import ForgotPasswordModel
class ForgotPasswordController:
    def __init__(self,controller,master,session:bool,user_id=None):
        self.user_id = user_id
        self.master = master
        self.controller = controller
        self.view = ForgotPasswordView(self,self.master,session)
    
    def main(self):
        self.view.main()

    def update_password(self,data:list):
        change_pass = ForgotPasswordModel(new_password=data[0],
                                          user_id=data[2])
        change_pass.update_password()

    def checkPassInput(self,data:list):
        password_model = ForgotPasswordModel(user_id=data[2],
                                             provided_email=data[4],
                                             provided_username=data[3],
                                             new_password=data[0],
                                             confirm_password=data[1])
        return password_model.confirm_password_update()

    def checkAccountInput(self, data:list):
        email_model = ForgotPasswordModel(provided_username=data[0]
                                          ,provided_email=data[1])
        noAccount = email_model.check_account_existence()
        
        if noAccount == 0: 
            return [email_model.get_user_id(),
                    email_model.provided_username,
                    email_model.provided_email,
                    email_model.get_forgot_password_otp()]
        else: 
            return noAccount
    
    def loginController(self,master):
        Functions.destroy_page(master)
        from Controller import LoginController
        login_page = LoginController(master)
        login_page.main()

    def staffView(self,master):
        Functions.destroy_page(master)
        from Controller import StaffController
        staff_dashboard = StaffController(master,self.user_id)
        staff_dashboard.main()

    def user_otp_verification(self, user_data:list):
        Functions.send_otp_email(user_data[2], user_data[3])