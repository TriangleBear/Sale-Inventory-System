from View import UserUpdateView
from Model import UserRegisterModel
from Utils import Functions

class UserUpdateController():
    def __init__(self,managerController,maintenanceController,user_data):
        self.mC = managerController
        self.maintenanceController = maintenanceController
        self.user_data = user_data
        self.view = UserUpdateView(self,self.user_data)
        self.editor_id = self.mC.user_id

    def main(self):
        self.view.main()

    def updateUserData(self, data:list,user_id:str):
        update_model = UserRegisterModel(data)
        return update_model.update_user(user_id)

    def check_password_criteria(self, data:list):
        pass_model = UserRegisterModel(data)
        return pass_model.check_password_criteria()
    
    def logUserActivity(self):
        Functions.logUserActivity([self.mC.user_id,"User Updated",Functions.get_current_date("datetime")])
    

    