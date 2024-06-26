from Utils.database import Database
class ItemRegisterModel:
    def __init__(self, data:list):
        self.item_name = data[0]
        self.quantity = data[1]
        self.price = data[2]
        self.supplier = data[3]
        self.expiry_date = data[4]
        self.flooring = data[5]
        self.ceiling = data[6]
        self.stock_level = data[7]

    def create_item(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """INSERT INTO Item (item_name, quantity, price, supplier, expiry_date, flooring, ceiling, stock_level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql, (self.item_name, self.quantity, self.price, self.supplier, self.expiry_date, self.flooring, self.ceiling, self.stock_level))
            connection.commit()
            connection.close()
        return 0
    
    def checkStockLevel(self):
        if self.quantity > self.flooring and self.quantity < self.ceiling:
            self.stock_level = "Average"
        if self.quantity < self.flooring:
            self.stock_level = "Danger"
        if self.quantity >= self.ceiling:
            self.stock_level = "Maximum"