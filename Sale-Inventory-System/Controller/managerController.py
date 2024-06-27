from View import ManagerDashboard
#from Model import ManagerModel
from Utils import Functions
from Controller.suppliesController import SuppliesController
from Controller.posController import PosController

class ManagerController:
    def __init__(self, master,user_id=None):
        self.master = master
        self.user_id = user_id
        self.view = ManagerDashboard(self,self.master,self.user_id)
    
    def main(self):
        self.view.main()

    def loginController(self,master):
        Functions.destroy_page(master)
        from Controller import LoginController
        login_page = LoginController(master)
        login_page.main()

    def userRegisterController(self):
        from Controller import UserRegisterController
        user_register_page = UserRegisterController(self)
        user_register_page.main()

    def securityController(self,master):
        Functions.destroy_page(master)
        from Controller import SecurityController
        security_page = SecurityController(master,self)
        security_page.main()
        
    def inventoryController(self,master):
        Functions.destroy_page(master)
        from Controller import InventoryController
        inventory_page = InventoryController(master,self)
        inventory_page.main()

    def suppliesController(self,master):
        Functions.destroy_page(master)
        from Controller import SuppliesController
        supplies_page = SuppliesController(master,self)
        supplies_page.main()

    def posController(self,master):
        Functions.destroy_page(master)
        from Controller import POSController
        pos_page = POSController(master,self)
        pos_page.main()

    def itemRegisterController(self):
        from Controller import ItemRegisterController
        item_register_page = ItemRegisterController(self)
        item_register_page.main()

    
