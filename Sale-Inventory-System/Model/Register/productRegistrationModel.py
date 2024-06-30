from Utils import Database
class ProductRegistrationModel:
    def __init__(self, data:list):
        #product_id, supply_id, product_name, quantity, price, expiration_date, category, stock_level, flooring, celling
        self.product_id = data[0]
        self.supply_id = data[1]
        self.product_name = data[2]
        self.product_price = data[3]
        self.product_quantity = data[4]
        self.expiry_date = data[5]
        self.category = data[6]
        self.stock_level = self.checkStockLevel()
        self.flooring = data[7]
        self.ceiling = data[8]
        
    def get_recipe_name_by_id(self, recipe_id):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT recipe_id, recipe_name FROM Recipes"""
                cursor.execute(sql)
                recipes = cursor.fetchall()
        return recipes

    def get_product_details(self, product_id):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT p.product_name, p.quantity, p.price, p.expiration_date, p.category, p.stock_level, p.flooring, p.celling, r.recipe_id
                        FROM Product p
                        LEFT JOIN Recipes r ON p.recipe_id = r.recipe_id
                        WHERE p.product_id = %s"""
                cursor.execute(sql, (product_id,))
                product_details = cursor.fetchone()
        return product_details
        
    def update_product(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """UPDATE Product SET product_name = %s, quantity = %s, price = %s, expiration_date = %s, category = %s, stock_level = %s, flooring = %s, celling = %s WHERE product_id = %s"""
                cursor.execute(sql, (self.product_name, self.product_quantity, self.product_price, self.expiry_date, self.category, self.stock_level, self.flooring, self.ceiling, self.product_id))
                connection.commit()
            connection.close()
        return 0

    def get_product_name(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT product_name FROM Product WHERE product_name = %s"""
                cursor.execute(sql, (self.product_name,))
                product_name = cursor.fetchone()
            connection.close()
        return product_name
    
    def register_product(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """INSERT INTO Product (product_id, supply_id, product_name, quantity, price, expiration_date, category, stock_level, flooring, celling) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                #supply_id should pass from supply module
                cursor.execute(sql, (self.product_id, self.supply_id, self.product_name, self.product_quantity, self.product_price, self.expiry_date, self.category, self.stock_level, self.flooring, self.ceiling))
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
    
    # Stock level is