from View import ManagerDashboard
from Model import ManagerModel
from Utils import Functions
from Controller.suppliesController import SuppliesController
from Controller.posController import PosController

class ManagerController:
    def __init__(self,master,user_id):
        self.master = master
        self.user_id = user_id
        # Assuming SuppliesController and POSController can be instantiated here
        self.suppliesController = SuppliesController(self.master,self.user_id)
        self.posController = PosController(self.master,self.user_id)
        # Now, pass all required arguments to ManagerDashboard
        self.view = ManagerDashboard(self.suppliesController, self.posController, self.master, self.user_id)
    
    def main(self):
        self.view.main()

    def homePage(self,master):
        Functions.destroy_page(master)
        self.main()

    def loginController(self,master):
        Functions.destroy_page(master)
        from Controller import LoginController
        login_page = LoginController(master)
        login_page.main()

    def registerController(self,master):
        Functions.destroy_page(master)
        from Controller import RegisterController
        register_page = RegisterController(master)
        register_page.main()

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