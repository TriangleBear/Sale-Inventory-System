from View import ProductUpdateView
class ProductUpdateController:
    def __init__(self, managerController, product_data, master):
        self.mC = managerController
        self.master = master
        self.product_data = product_data
        self.view = ProductUpdateView(self, self.master, product_data=self.product_data)

    def main(self):
        self.view.main()