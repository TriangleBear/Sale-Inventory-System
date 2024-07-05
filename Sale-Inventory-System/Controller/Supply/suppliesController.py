from View import SuppliesView
from Model import SuppliesModel
from Utils import Functions
class SuppliesController:
    def __init__(self,controller,master):
        self.master = master
        self.controller = controller
        self.view = SuppliesView(self,master)

    def main(self):
        self.view.main()

    def managerController(self):
        from Controller import ManagerController
        manager_page = ManagerController()
        manager_page.main()

    def fetch_items_quantity(self, item_name, new_quantity):
        model = SuppliesModel()
        return model.fetch_items_quantity(item_name, new_quantity)

    def fetch_items_below_or_equal_flooring(self):
        model = SuppliesModel()
        return model.fetch_items_below_or_equal_flooring()

    def fetch_supply_below_or_equal_flooring(self):
        model = SuppliesModel()
        return model.fetch_supply_below_or_equal_flooring()

    def update_quantity(self,reorder_items):
        model = PosModel(reorder_items=reorder_items)
        return model.update_quantity(reorder_items[0], reorder_items[1])
    
    def update_item_quantity_in_database(self, item_name, new_quantity):
        model = SuppliesModel()
        return model.update_item_quantity_in_database(item_name, new_quantity)

    def update_supply_quantity_in_database(self, item_name, new_quantity):
        model = SuppliesModel()
        return model.update_supply_quantity_in_database(item_name, new_quantity)

    def logUserActivity(self,items_id):
        Functions.logUserActivity([
            self.mC.user_id,
            f"{items_id}|Supply Purchased", 
            Functions.get_current_date("datetime")
            ]
        )

    def get_supply_id(self, supply_name):
        model = SuppliesModel()
        return model.get_supply_id(supply_name)
    
    def get_item_id(self, item_name):
        model = SuppliesModel()
        return model.get_item_id(item_name)



