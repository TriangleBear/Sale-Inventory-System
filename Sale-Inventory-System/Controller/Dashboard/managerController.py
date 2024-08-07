from View import ManagerDashboard
#from Model import ManagerModel
from Utils import Functions

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

    def maintenanceController(self,master):
        Functions.destroy_page(master)
        from Controller import MaintenanceController
        maintenance_page = MaintenanceController(self,master)
        maintenance_page.main()

    def securityController(self,master):
        Functions.destroy_page(master)
        from Controller import SecurityController
        security_page = SecurityController(master,self)
        security_page.main()
        
    def userRegisterController(self):
        from Controller import UserRegisterController
        user_register_page = UserRegisterController(self)
        user_register_page.main()

    def recipeRegisterController(self,master):
        Functions.destroy_page(master)
        from Controller import RecipeRegisterController
        recipe_register_page = RecipeRegisterController(self,master)
        recipe_register_page.main()

    def ingredientRegisterController(self,recipeDetails):
        #recipeDetails = [recipe_id,recipe_name, user_id]
        from Controller import IngredientRegisterController
        ingredient_register_page = IngredientRegisterController(self,recipeDetails)
        ingredient_register_page.main()

    def itemRegisterController(self,status):
        from Controller import ItemRegisterController
        item_register_page = ItemRegisterController(self,status)
        item_register_page.main()

    def inventoryController(self,master):
        Functions.destroy_page(master)
        from Controller import InventoryController
        inventory_page = InventoryController(master,self)
        inventory_page.main()

    def suppliesController(self,master):
        Functions.destroy_page(master)
        from Controller import SuppliesController
        supplies_page = SuppliesController(self,master)
        supplies_page.main()

    def receiveSuppliesController(self):
        from Controller import RecieveSuppliesController
        receive_supplies_page = RecieveSuppliesController(self)
        receive_supplies_page.main()

    def posController(self,master):
        Functions.destroy_page(master)
        from Controller import PosController
        pos_page = PosController(self,master)
        pos_page.main()

    def reportController(self,master):
        from Controller import ReportController
        report_page = ReportController(self,master)
        report_page.main()

    def backupDatabaseController(self,master):
        from Controller import BackupDatabaseController
        backup_page = BackupDatabaseController(self,master)
        backup_page.main()

    def mainController(self):
        self.master.destroy()
        from Controller import MainController
        logout = MainController()
        logout.main()

    def productRegisterController(self,id,name):
        from Controller import ProductRegisterController
        product_register_page = ProductRegisterController(self,id,name)
        product_register_page.main()

    def userManualController(self,master):
        Functions.destroy_page(master)
        from Controller import UserManualController
        user_manual_page = UserManualController(self,master)
        user_manual_page.main()

    def get_rid_rname(self):
        from Model import ManagerModel
        model = ManagerModel()
        return model.get_recipe_name_and_recipe_id()
    
    def get_sid_sname(self):
        from Model import ManagerModel
        model = ManagerModel()
        return model.get_supply_name_and_supply_id()
    
    def get_ingd_id(self):
        from Model import IngredientRegisterModel
        model = IngredientRegisterModel()
        return model.get_ingd_id()
    
    def logUserActivity(self):
        Functions.logUserActivity([self.user_id,"Logged Out",Functions.get_current_date("datetime")])