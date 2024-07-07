from View import UserUpdateView
from Utils import Functions
class UserUpdateController:
    def __init__(self,managerController, current_user_data, master):
        self.mC = managerController
        self.master = master
        self.current_user_data = current_user_data
        self.view = UserUpdateView(self, self.master, user_data=self.current_user_data)

    def main(self):
        self.view.main()

    def checkInput(self,data:list) -> int: 
        from Model import UserRegisterModel
        noUser = UserRegisterModel(data)
        return noUser.checkInput()
    
    def registerUser(self,data:list) -> None:
        from Model import UserRegisterModel
        user = UserRegisterModel(data)
        user.registerUserData()

    def logUserActivity(self):
        Functions.logUserActivity([self.mC.user_id,"User Registered",Functions.get_current_date("datetime")])