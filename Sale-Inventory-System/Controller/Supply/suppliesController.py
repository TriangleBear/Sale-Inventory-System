from View import SuppliesView
from Model import SuppliesModel
from Utils import Functions
class SuppliesController:
    def __init__(self,managerController,master):
        self.master = master
        self.mC = managerController
        self.view = SuppliesView(self,master)

    def main(self):
        self.view.main()

    def suppliesPage(self):
        Functions.destroy_page(self.master)
        self.mC.view.supplies_page()

    def reorderController(self,item_reorder):
        from Controller import ReorderSuppliesController
        reorder = ReorderSuppliesController(self,item_reorder)
        reorder.main()

    def fetch_items_quantity(self, item_name, new_quantity):
        model = SuppliesModel()
        return model.fetch_items_quantity(item_name, new_quantity)
    
    def fetch_supply_quantity(self, item_name, new_quantity):
        model = SuppliesModel()
        return model.fetch_supply_quantity(item_name, new_quantity)

    def fetch_items_below_or_equal_flooring(self):
        model = SuppliesModel()
        return model.fetch_items_below_or_equal_flooring()

    def fetch_supply_below_or_equal_flooring(self):
        model = SuppliesModel()
        return model.fetch_supply_below_or_equal_flooring()
    
    def update_item_quantity_in_database(self, item_name, new_quantity):
        model = SuppliesModel()
        return model.update_item_quantity_in_database(item_name, new_quantity)

    def update_supply_quantity_in_database(self, item_name, new_quantity):
        model = SuppliesModel()
        return model.update_supply_quantity_in_database(item_name, new_quantity)
    
    def reorder(self,cart_items):
        model = SuppliesModel()
        return model.reorder(cart_items)

    def logUserActivity(self,items_id):
        Functions.logUserActivity([
            self.mC.user_id,
            f"{items_id}|Supply Ordered", 
            Functions.get_current_date("datetime")
            ]
        )

    def get_item_type_by_id(self, item_id):
        model = SuppliesModel()
        return model.get_item_type_by_id(item_id)



