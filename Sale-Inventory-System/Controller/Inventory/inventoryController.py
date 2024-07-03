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
    
    def search_data(self,table_name,search_query):
        db_table = table_name
        if table_name == "Supplies":
            db_table = "Supply"
        if table_name == "Products":
            db_table = "Product"
        model = InventoryModel(search_entry=search_query,table_name=db_table)
        return model.search_data()
    
    def manager_view(self):
        Functions.destroy_page(self.master)
        self.mC.view.body()