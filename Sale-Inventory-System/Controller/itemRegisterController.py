from View import ItemRegisterView
from Utils import Functions
class ItemRegisterController:
    def __init__(self,managerController):
        self.managerController = managerController
        self.view = ItemRegisterView(self)
        self.user_id = self.managerController.user_id

    def main(self):
        self.view.main()

    def checkInput(self,data:list):
        from Model import ItemRegisterModel
        noItem = ItemRegisterModel(data)
        return noItem.checkInput()
    
    def register(self,data:list):
        from Model import ItemRegisterModel
        item = ItemRegisterModel(data,self.user_id)
        item.registerItemData()

    def logUserActivity(self):
        Functions.logUserActivity([self.user_id,"Item Registered",Functions.get_current_date("datetime")])