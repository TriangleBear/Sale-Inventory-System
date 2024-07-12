from icecream import ic
from View import ReceiveSuppliesView
from Utils import Functions
class RecieveSuppliesController:
    def __init__(self,managerController):
        self.mC = managerController
        self.view = ReceiveSuppliesView(self)

    def main(self):
        self.view.main()

    def fetch_all_pending_orders(self):
        from Model import SuppliesModel
        model = SuppliesModel()
        return model.fetch_all_pending_orders()
    
    def add_to_items(self,data):
        from Model import SuppliesModel
        model = SuppliesModel()
        return model.add_to_items(data)
    
    def logUserActivity(self,item_id):
        Functions.logUserActivity([self.mC.user_id,f"{item_id}|Order Received",Functions.get_current_date('datetime')])