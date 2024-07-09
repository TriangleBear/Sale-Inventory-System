from Model import SuppliesModel
from View import ReceiveSuppliesView
from Utils import Functions
class RecieveSuppliesController:
    def __init__(self,controller,reorder_items=None):
        self.mC = controller
        self.reorder_items = reorder_items
        self.view = ReceiveSuppliesView(self,self.reorder_items)

    def main(self):
        self.view.main()

    def managerController(self):
        from Controller import ManagerController
        manager_page = ManagerController()
        manager_page.main()

    