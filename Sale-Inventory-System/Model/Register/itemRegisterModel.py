from Utils import Functions
from Controller.Dashboard import managerController
from Utils import Database
class ItemRegisterModel:
    def __init__(self,data:list,user_id=None,status=None):
        #item name,quantity,price,supplier,expiry date, category, flooring, ceiling, stock_level
        self.status = status
        self.item_id = Functions.generate_unique_id("Item")
        self.user_id = user_id
        self.item_name = data[0]
        self.quantity = data[1]
        self.unit = data[2]
        self.price = data[3]
        self.supplier = data[4]
        self.expiry_date = data[5]
        self.category = data[6]
        self.flooring = data[7]
        self.ceiling = data[8]
        self.stock_level = self.checkStockLevel()
        

    def checkInput(self):
        #check error if error return ValueError else return 0
        if not self.item_name:
            return ValueError("Item name cannot be empty")
        if not self.quantity:
            return ValueError("Quantity cannot be empty")
        if not self.price:
            return ValueError("Price cannot be empty")
        if not self.supplier:
            return ValueError("Supplier cannot be empty")
        if not self.expiry_date:
            return ValueError("Expiry date cannot be empty")
        if self.category == "Select Category" and self.status == "Raw item":
            return ValueError("Category cannot be empty")
        if self.category == "Select Menu Type" and self.status == "Supply Item":
            return ValueError("Menu Type cannot be empty")
        if not self.stock_level:
            return ValueError("Stock level cannot be empty")
        if not self.flooring:
            return ValueError("Flooring cannot be empty")
        if not self.ceiling:
            return ValueError("Ceiling cannot be empty")
        return 0

    def registerItemData(self):
        #register item to data base
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                if self.status == "Supply Item":
                    sql = """INSERT INTO Supply (supply_id, user_id, product_name, quantity, unit,price, supplier, exp_date, menu_type, flooring, ceiling, stock_level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    cursor.execute(sql, (
                        self.item_id,
                        self.user_id,
                        self.item_name,
                        self.quantity,
                        self.unit,
                        self.price,
                        self.supplier,
                        self.expiry_date,
                        self.category,
                        self.flooring,
                        self.ceiling,
                        self.stock_level
                    ))
                if self.status == "Raw Item":
                    sql = """INSERT INTO Items (item_id, user_id, item_name, quantity, unit, price, supplier, exp_date, category, flooring, ceiling, stock_level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    cursor.execute(sql, (
                        self.item_id,
                        self.user_id,
                        self.item_name,
                        self.quantity,
                        self.unit,
                        self.price,
                        self.supplier,
                        self.expiry_date,
                        self.category,
                        self.flooring,
                        self.ceiling,
                        self.stock_level
                    ))
            connection.commit()
            connection.close()
        return 0

    def checkStockLevel(self):
        if self.quantity > self.flooring and self.quantity < self.ceiling:
            return "Average"
        if self.quantity < self.flooring:
            return "Danger"
        if self.quantity >= self.ceiling:
            return "Maximum"