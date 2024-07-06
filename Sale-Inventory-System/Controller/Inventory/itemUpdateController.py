from View import ItemUpdateView
from Utils import Functions
class ItemUpdateController:
    def __init__(self,managerController,inventoryController,item_data):
        self.mC = managerController
        self.inventoryController = inventoryController
        self.item_data = item_data
        self.view = ItemUpdateView(self,self.item_data)
        self.user_id = self.mC.user_id

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

    def get_item_id(self):
        from Model import ItemRegisterModel
        item = ItemRegisterModel()
        return item.set_item_id()

    def update_item_in_database(self,item_id,quantity):
        from Model import ItemRegisterModel
        item = ItemRegisterModel()
        item.update_item(item_id,quantity)

    def logUserActivity(self):
        Functions.logUserActivity([self.user_id,"Item Updated",Functions.get_current_date("datetime")])