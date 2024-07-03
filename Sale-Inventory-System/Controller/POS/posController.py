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

    def search_product(self,search):
        model = PosModel()
        return model.search_product(search)

    def fetch_all_products(self):
        model = PosModel()
        print(f'fetch_all_products: {model.fetch_all_products()}')
        return model.fetch_all_products()



