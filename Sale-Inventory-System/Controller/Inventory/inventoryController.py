from Model import InventoryModel
from View import InventoryView
from Utils import Functions
class InventoryController:
    def __init__(self,master,managerController):
        self.master = master
        self.mC = managerController
        self.view = InventoryView(self, master)

    def main(self):
        self.view.main()

    def inventoryController(self):
        from Controller import InventoryController
        inventory_page = InventoryController(self.master)
        inventory_page.main()
    
    def get_recipe_on_database(self):
        model = InventoryModel()
        return model.get_recipe_on_database()
    
    def get_recipe_column_names(self):
        model = InventoryModel()
        return model.get_recipe_column_names()

    def get_product_on_database(self):
        model = InventoryModel()
        return model.get_product_on_database()
    
    def get_product_column_names(self):
        model = InventoryModel()
        return model.get_product_column_names()
    
    def get_items_on_database(self):
        model = InventoryModel()
        return model.get_items_on_database()
    
    def get_items_column_names(self):
        model = InventoryModel()
        return model.get_items_column_names()
    
    def get_supply_on_database(self):
        model = InventoryModel()
        return model.get_supply_on_database()
    
    def get_supply_column_names(self):
        model = InventoryModel()
        return model.get_supply_column_names()
    
    def search_data(self,table_name,search_query):
        db_table = table_name
        if table_name == "Supplies":
            db_table = "Supply"
        elif table_name == "Products":
            db_table = "Product"
        model = InventoryModel(search_entry=search_query,table_name=db_table)
        return model.search_data()
    
    def manager_view(self):
        Functions.destroy_page(self.master)
        self.mC.view.body()

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

    def recipeIngredientDelete(self,current_recipe_data):
        recipe_id,recipe_name,user_id= current_recipe_data
        from Controller import IngredientUpdateController, RecipeUpdateController
        ingredient_update = IngredientUpdateController(self.mC)
        ingredient_update.delete_recipe_ingredients(recipe_id)
        recipe_update = RecipeUpdateController(self.mC,self)
        recipe_update.delete_recipe(recipe_id)
        return
