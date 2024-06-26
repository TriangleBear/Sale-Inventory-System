from Model.inventoryModel import InventoryModel
from View.inventoryView import InventoryView
class InventoryController:
    def __init__(self,master):
        self.master = master
        self.view = InventoryView(self, master)

    def main(self):
        self.view.main()

    def inventoryController(self):
        from Controller.inventoryController import InventoryController
        inventory_page = InventoryController(self.master)
        inventory_page.main()

    def create_product(self,data):
        model = InventoryModel(data)
        return model.create_product()
    
    def _get_products_on_database(self):
        model = InventoryModel([])
        return model.get_products_on_database()