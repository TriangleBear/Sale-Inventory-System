from Utils.database import Database
class InventoryModel:
    def __init__(self,data:list):
        self.product_id = data[0]
        self.product_name = data[1]
        self.quantity = data[2]
        self.supplier = data[3]
        self.expiration_date = data[4]
        self.menu = data[5]
        self.cost = data[6]
        self.category = data[7]

    def create_product(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """INSERT INTO Product (product_id, product_name, quantity, supplier, expiration_date, menu, cost, category) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql, (self.product_id, self.product_name, self.quantity, self.supplier, self.expiration_date, self.menu, self.cost, self.category))
                connection.commit()
            connection.close()
        return 0
    
    def get_products_on_database(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT * FROM Product"""
                cursor.execute(sql)
                result = cursor.fetchall()
            connection.close()
        return result