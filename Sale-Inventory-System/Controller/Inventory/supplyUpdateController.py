from View import SupplyUpdateView
from Utils import Functions

class SupplyUpdateController:
    def __init__(self,managerController,inventoryController,item_data):
        self.mC = managerController
        self.inventoryController = inventoryController
        self.item_data = item_data
        self.view = SupplyUpdateView(self,self.item_data)
        self.user_id = self.mC.user_id

    def main(self):
        self.view.main()

    def checkInput(self,data:list,status:str) -> int: 
        from Model import ItemRegisterModel
        noItem = ItemRegisterModel(data,status)
        return noItem.checkInput()
    
    def updateItem(self,data:list,status:str) -> None:
        from Model import ItemRegisterModel
        item = ItemRegisterModel(data,self.user_id,status)
        item.updateItemData()

    def update_item_in_database(self,item_id,quantity):
        from Model import ItemRegisterModel
        item = ItemRegisterModel()
        item.update_item(item_id,quantity)

    def logUserActivity(self):
        Functions.logUserActivity([self.user_id,"Supply Updated",Functions.get_current_date("datetime")])