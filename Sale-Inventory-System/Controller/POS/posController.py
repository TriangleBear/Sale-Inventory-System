from View import PosView
from Model import PosModel
from Utils import Functions
class PosController:
    def __init__(self,controller,master):
        self.master = master
        self.controller = controller
        self.view = PosView(self,master)

    def main(self):
        self.view.main()

    def managerController(self):
        from Controller import ManagerController
        manager_page = ManagerController()
        manager_page.main()

    def add_product(self,sales):
        model = PosModel()

    def update_product_quantity_in_database(self,cart_items):
        model = PosModel(cart_items=cart_items)
        model.update_product_quantity_in_database()
        return

    def save_transaction_to_sales(self,cart_items,sales_id,datetime):
        model = PosModel(cart_items=cart_items,user_id=self.mC.user_id,datetime=datetime)
        return model.save_transaction(sales_id=sales_id)

    def search_data(self,search):
        model = PosModel()
        return model.search_product(search)

    def fetch_all_products(self):
        model = PosModel()
        return model.fetch_all_products()
    
    def save_sales(self,amount_tendered,total_price,datetime):
        model = PosModel(total_price=total_price,amount_tendered=amount_tendered,user_id=self.mC.user_id,datetime=datetime)
        return model.save_sales()
    
    def logUserActivity(self,sales_id):
        Functions.logUserActivity([
            self.mC.user_id,
            f"{sales_id}|Product Sold", 
            Functions.get_current_date("datetime")
            ]
        )



