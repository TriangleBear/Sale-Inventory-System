from View import MaintenanceView
from Model import MaintenanceModel
from Utils import Functions
class MaintenanceController:
    def __init__(self,managerController, master):
        self.master = master
        self.mC = managerController
        self.view = MaintenanceView(self, master)

    def main(self):
        self.view.main()

    def get_recipe_on_database(self):
        model = MaintenanceModel()
        return model.get_recipe_on_database()
    
    def get_recipe_column_names(self):
        model = MaintenanceModel()
        return model.get_recipe_column_names()

    def get_product_on_database(self):
        model = MaintenanceModel()
        return model.get_product_on_database()
    
    def get_product_column_names(self):
        model = MaintenanceModel()
        return model.get_product_column_names()
    
    def get_items_on_database(self):
        model = MaintenanceModel()
        return model.get_items_on_database()
    
    def get_items_column_names(self):
        model = MaintenanceModel()
        return model.get_items_column_names()
    
    def get_supply_on_database(self):
        model = MaintenanceModel()
        return model.get_supply_on_database()
    
    def get_supply_column_names(self):
        model = MaintenanceModel()
        return model.get_supply_column_names()
    
    def get_users_on_database(self):
        model = MaintenanceModel()
        return model.get_users_on_database()

    def get_users_column_names(self):
        model = MaintenanceModel()
        return model.get_users_column_names()

    def update_item_data(self,table_name,update_data):
        db_table = table_name
        if table_name == "Supplies":
            db_table = "Supply"
        elif table_name == "Products":
            db_table = "Product"
        model = MaintenanceModel(update_data=update_data,table_name=db_table)
        return model.update_data()
    
    def manager_view(self):
        Functions.destroy_page(self.master)
        self.mC.view.maintenance_page()

    def recipeUpdate(self,current_recipe_data):
        from Controller import RecipeUpdateController
        recipe_update = RecipeUpdateController(self.mC,self,current_recipe_data)
        recipe_update.main()

    def recipeIngredientUpdate(self,current_recipe_data):
        #current_recipe_data = [ingd_name, description,quantity,unit]
        from Controller import IngredientUpdateController
        ingredient_update = IngredientUpdateController(self.mC,recipeDetails=current_recipe_data)
        ingredient_update.main()

    def itemUpdate(self,current_item_data):
        from Controller import ItemUpdateController
        item_update = ItemUpdateController(self.mC,self,current_item_data)
        item_update.main()

    def supplyUpdate(self,current_item_data):
        from Controller import SupplyUpdateController
        supply_update = SupplyUpdateController(self.mC,self,current_item_data)
        supply_update.main()

    def productUpdate(self, current_product_data):
        from Controller import ProductUpdateController
        product_update = ProductUpdateController(self.mC, self.master, current_product_data)
        product_update.main()

    def recipeIngredientDelete(self,current_recipe_data):
        recipe_id,recipe_name,user_id= current_recipe_data
        from Controller import IngredientUpdateController, RecipeUpdateController
        ingredient_update = IngredientUpdateController(self.mC)
        ingredient_update.delete_recipe_ingredients(recipe_id)
        recipe_update = RecipeUpdateController(self.mC,self)
        recipe_update.delete_recipe(recipe_id)
        return
    
    def userUpdate(self,current_user_data):
        from Controller import UserUpdateController
        user_update = UserUpdateController(self.mC,self,current_user_data)
        user_update.main()

    def search_data(self,table_name,search_query):
        db_table = table_name
        search = search_query
        if table_name == "Supplies":
            db_table = "Supply"
        elif table_name == "Products":
            db_table = "Product"
        elif table_name == "Users":
            db_table = "User"
        model = MaintenanceModel(search_entry=search_query,table_name=db_table)
        return model.search_data()