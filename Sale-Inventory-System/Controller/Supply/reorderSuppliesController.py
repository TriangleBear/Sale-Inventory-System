from View import ReorderSuppliesView

class ReorderSuppliesController:
    def __init__(self,suppliesController,item_reorder):
        self.suppliesController = suppliesController
        self.item_reorder = item_reorder
        self.view = ReorderSuppliesView(self,self.item_reorder)

    def main(self):
        self.view.main()

    def insert_into_cart(self,data:list):
        self.suppliesController.view.add_to_cart(data)