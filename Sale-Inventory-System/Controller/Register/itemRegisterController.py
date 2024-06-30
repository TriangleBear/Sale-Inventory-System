from View import ItemRegisterView
from Utils import Functions
class ItemRegisterController:
    def __init__(self,managerController,status):
        self.mC = managerController
        self.status = status
        self.view = ItemRegisterView(self,self.status)
        self.user_id = self.managerController.user_id

    def main(self):
        self.view.main()

    def checkInput(self,data:list):
        from Model import ItemRegisterModel
        noItem = ItemRegisterModel(data,self.status)
        return noItem.checkInput()
    
    def register(self,data:list):
        from Model import ItemRegisterModel
        item = ItemRegisterModel(data,self.user_id,self.status)
        item.registerItemData()

    def logUserActivity(self):
        Functions.logUserActivity([self.user_id,"Item Registered",Functions.get_current_date("datetime")])