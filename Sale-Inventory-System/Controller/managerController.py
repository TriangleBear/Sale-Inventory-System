from View import ManagerDashboard
from Model import ManagerModel
from Utils import Functions
from Controller.suppliesController import SuppliesController
from Controller.posController import PosController

class ManagerController:
    def __init__(self, master,user_id=None):
        self.master = master
        self.id = user_id
        self.view = ManagerDashboard(self,self.master,self.id)
    
    def main(self):
        self.view.main()

    def loginController(self,master):
        Functions.destroy_page(master)
        from Controller import LoginController
        login_page = LoginController(master)
        login_page.main()

    def registerController(self,master):
        Functions.destroy_page(master)
        from Controller import UserRegisterController
        user_register_page = UserRegisterController(master,self)
        user_register_page.main()

    def reportController(self,master):
        Functions.destroy_page(master)
        from Controller import ReportController
        report_page = ReportController(master)
        report_page.main()

    def inventoryController(self,master):
        Functions.destroy_page(master)
        from Controller import InventoryController
        inventory_page = InventoryController(master)
        inventory_page.main()

    def suppliesController(self,master):
        Functions.destroy_page(master)
        from Controller import SuppliesController
        supplies_page = SuppliesController(master)
        supplies_page.main()

    def posController(self,master):
        Functions.destroy_page(master)
        from Controller import POSController
        pos_page = POSController(master)
        pos_page.main()
