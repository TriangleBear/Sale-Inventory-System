from View import PosView
from Model import PosModel
class PosController:
    def __init__(self,managerController,master):
        self.master = master
        self.mC = managerController
        self.view = PosView(self,master)
        self.cart_items = []

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

    def fetch_all_cart_items(self):
        return self.cart_items

    def update_product_quantity_in_database(self,product_name,quantity_sold):
        model = PosModel(self)
        current_quantity = self.fetch_current_quantity_from_database(product_name)
        new_quantity = int(current_quantity) - int(quantity_sold)
        return model.update_product_quantity_in_database(product_name,new_quantity)

    def save_transaction_to_sales(self):
        model = PosModel()
        return model.save_transaction()
    
    def save_cart_items(self, cart_items):
        self.posModel.save_transaction(cart_items)

    def search_product(self,search):
        model = PosModel()
        return model.search_product(search)
    
    def fetch_current_quantity_from_database(self,product_name):
        model = PosModel()
        return model.search_product(product_name)[3]

    def fetch_all_products(self):
        model = PosModel(self.mC)
        print(f'fetch_all_products: {model.fetch_all_products()}')
        return model.fetch_all_products()



