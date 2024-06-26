from View import ItemRegisterView
from Utils import Functions
class ItemRegisterController:
    def __init__(self,managerController):
        self.managerController = managerController
        self.view = ItemRegisterView(self)

    def main(self):
        self.view.main()

    def checkInput(self,data:list):
        from Model import ItemRegisterModel
        noItem = ItemRegisterModel(data)
        return noItem.checkInput()
    
    def register(self,data:list):
        from Model import ItemRegisterModel
        item = ItemRegisterModel(data)
        item.registerItemData()