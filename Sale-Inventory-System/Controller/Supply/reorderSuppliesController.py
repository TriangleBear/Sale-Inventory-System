from View import ReorderSuppliesView
from icecream import ic
class ReorderSuppliesController:
    def __init__(self,suppliesController,item_reorder):
        self.suppliesController = suppliesController
        self.item_reorder = item_reorder
        self.view = ReorderSuppliesView(self,self.item_reorder)

    def main(self):
        self.view.main()

    def insert_into_cart(self,data:list):
        self.suppliesController.view.add_to_cart(data)

    def checkInput(self,data:list):
        ic(data)
    #check error if error return ValueError else return 0
        if not data[0] or data[0] <= 0:
            return ValueError("Quantity cannot be empty")
        if not data[1]:
            return ValueError("Expected Payment cannot be empty")
        if not data[2]:
            return ValueError("Arrival date cannot be empty")
        return 0