from Utils import Functions
class ItemRegisterModel:
    def __init__(self,data:list):
        self.item_id = Functions.generate_unique_id("Item")
        self.item_name = data[0]
        self.quantity = data[1]
        self.price = data[2]
        self.supplier = data[3]
        self.expiry_date = data[4]
        self.category = data[5]
        self.flooring = data[6]
        self.ceiling = data[7]

    def checkInput(self):
        #check error if error return ValueError else return 0
        pass
    def registerItemData(self):
        #register item to data base
        pass

    def checkStockLevel(self):
        if self.quantity > self.flooring and self.quantity < self.ceiling:
            self.stock_level = "Average"
        if self.quantity < self.flooring:
            self.stock_level = "Danger"
        if self.quantity >= self.ceiling:
            self.stock_level = "Maximum"