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

    def userRegisterController(self):
        from Controller import UserRegisterController
        user_register_page = UserRegisterController(self)
        user_register_page.main()

    def recipeRegisterController(self,master):
        Functions.destroy_page(master)
        from Controller import RecipeRegisterController
        recipe_register_page = RecipeRegisterController(self,master)
        recipe_register_page.main()

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

    def reportController(self,master):
        from Controller import ReportController
        report_page = ReportController(self,master)
        report_page.main()

    def itemRegisterController(self,status):
        from Controller import ItemRegisterController
        item_register_page = ItemRegisterController(self,status)
        item_register_page.main()

    def mainController(self):
        self.master.destroy()
        from Controller import MainController
        logout = MainController()
        logout.main()
    
    def ingredientRegisterController(self,recipeDetails):
        #recipeDetails = [recipe_id,recipe_name, user_id]
        from Controller import IngredientRegisterController
        ingredient_register_page = IngredientRegisterController(self,recipeDetails[0])
        ingredient_register_page.main()

    def productRegisterController(self,recipe_id):
        from Controller import ProductRegisterController
        product_register_page = ProductRegisterController(self,recipe_id)
        product_register_page.main()

    def get_rid_rname(self):
        from Model import ManagerModel
        model = ManagerModel()
        return model.get_recipe_name_and_recipe_id()