from View import PosView
from Model import PosModel
class PosController:
    def __init__(self,managerController,master):
        self.master = master
        self.mC = managerController
        self.view = PosView(self,master)

    def main(self):
        self.view.main()

    def managerController(self):
        from Controller import ManagerController
        manager_page = ManagerController()
        manager_page.main()

    def posController(self):
        from Controller import PosController
        pos_page = PosController()
        pos_page.main()

    def add_product(self,sales):
        model = PosModel()

    def update_product_quantity_in_database(self,cart_items):
        model = PosModel(cart_items=cart_items)
        model.update_product_quantity_in_database()
        return

    def save_transaction_to_sales(self,cart_items,sales_id):
        model = PosModel(cart_items=cart_items,user_id=self.mC.user_id)
        return model.save_transaction(sales_id=sales_id)

    def search_product(self,search):
        model = PosModel()
        return model.search_product(search)

    def fetch_all_products(self):
        model = PosModel()
        return model.fetch_all_products()
    
    def save_sales(self,amount_tendered,total_price):
        model = PosModel(total_price=total_price,amount_tendered=amount_tendered,user_id=self.mC.user_id)
        model.save_sales()



