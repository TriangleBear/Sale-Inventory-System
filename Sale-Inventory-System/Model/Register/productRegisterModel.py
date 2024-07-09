from Utils import Database, Functions
class ProductRegisterModel:
    def __init__(self, data:list=None, user_id=None,product_id=None,product_name=None):
        #product_id, supply_id, product_name, quantity, price, expiration_date, category, stock_level, flooring, celling        self.image_id = ''
        self.user_id = user_id
        self.product_id = product_id
        self.product_name = product_name
        if data is not None:
            self.product_quantity = data[0]
            self.product_price = data[1]
            self.expiry_date = data[2]
            self.category = data[3]
            self.flooring = data[4]
            self.ceiling = data[5]
            self.stock_level = self.checkStockLevel()

    
        
    def set_product_id(self,state):
        if state == "Recipe":
            return Functions.generate_unique_id("ProductR")
        if state == "Supply":
            return Functions.generate_unique_id("ProductS")

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

    def product_existence_check(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT product_id FROM Product WHERE product_name = %s"""
                cursor.execute(sql, (self.product_name,))
                product_id = cursor.fetchone()
            connection.close()
        return product_id['product_id'] if product_id else None
    
    def fetch_existing_product_quantity(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT quantity FROM Product WHERE product_name = %s AND product_id = %s"""
                cursor.execute(sql, (self.product_name,self.product_id,))
                quantity = cursor.fetchone()
            connection.close()
        return quantity['quantity'] if quantity else None

    def register_product(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                if not self.product_existence_check():
                    sql = """INSERT INTO Product (product_id, user_id, product_name, quantity, price, exp_date, category, flooring, ceiling, stock_level) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
                    #supply_id should pass from supply module
                    cursor.execute(sql, (self.product_id, 
                                        self.user_id, 
                                        self.product_name, 
                                        self.product_quantity, 
                                        self.product_price, 
                                        self.expiry_date, 
                                        self.category, 
                                        self.flooring, 
                                        self.ceiling,
                                        self.stock_level))
                    connection.commit()
                else:
                    current_quantity = self.fetch_existing_product_quantity()
                    self.product_quantity += current_quantity  
                    self.stock_level = self.checkStockLevel()
                    sql = """UPDATE Product SET 
                            quantity = %s,
                            price = %s,
                            exp_date = %s,
                            category = %s,
                            flooring = %s,
                            ceiling = %s,
                            stock_level = %s
                            WHERE product_id = %s;"""
                    cursor.execute(sql,(
                        self.product_quantity,
                        self.product_price,
                        self.expiry_date,
                        self.category,
                        self.flooring,
                        self.ceiling,
                        self.stock_level,
                        self.product_id
                        ))
                    connection.commit()
            connection.close()
        return 0
    
    def register_product(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                if not self.product_existence_check():
                    sql = """INSERT INTO Product (product_id, user_id, product_name, quantity, price, exp_date, category, flooring, ceiling, stock_level) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
                    cursor.execute(sql, (self.product_id, 
                                        self.user_id, 
                                        self.product_name, 
                                        self.product_quantity, 
                                        self.product_price, 
                                        self.expiry_date, 
                                        self.category, 
                                        self.flooring, 
                                        self.ceiling,
                                        self.stock_level))
                    connection.commit()
                else:
                    current_quantity = self.fetch_existing_product_quantity()
                    self.product_quantity += current_quantity  
                    self.stock_level = self.checkStockLevel()
                    sql = """UPDATE Product SET 
                            product_name = %s,
                            quantity = %s,
                            price = %s,
                            exp_date = %s,
                            category = %s,
                            flooring = %s,
                            ceiling = %s,
                            stock_level = %s
                            WHERE product_id = %s;"""
                    cursor.execute(sql,(
                        self.product_name,
                        self.product_quantity,
                        self.product_price,
                        self.expiry_date,
                        self.category,
                        self.flooring,
                        self.ceiling,
                        self.stock_level,
                        self.product_id
                        ))
                    connection.commit()
            connection.close()
        return 0
    
    def checkStockLevel(self):
        if self.product_quantity > self.flooring and self.product_quantity < self.ceiling:
            return "Average"
        if self.product_quantity <= self.flooring:
            return "Danger"
        if self.product_quantity >= self.ceiling:
            return "Maximum"
        
    def check_existing_product(self,product_name):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT product_id FROM Product WHERE product_name = %s"""
                cursor.execute(sql, (product_name,))
                product_id= cursor.fetchone()
        return product_id if product_id else None

    def checkInput(self):
        #check error if error return ValueError else return 0
        if not self.product_quantity or self.product_quantity <= 0:
            return ValueError("Quantity cannot be empty")
        if not self.product_price:
            return ValueError("price/unit cannot be empty")
        if self.category == "Select Category":
            return ValueError("Category cannot be empty")
        if not self.flooring:
            return ValueError("Flooring cannot be empty")
        if not self.ceiling:
            return ValueError("Ceiling cannot be empty")
        if not self.stock_level:
            return ValueError("Stock level cannot be empty")
        return 0
    
    def verifyQuantityInput(self):
        #check error if error return ValueError else return 0
        if not self.product_quantity or self.product_quantity <= 0:
            return ValueError("Quantity cannot be empty")
        if not self.product_price:
            return ValueError("price/unit cannot be empty")
        if self.category == "Select Category":
            return ValueError("Category cannot be empty")
        if not self.flooring:
            return ValueError("Flooring cannot be empty")
        if not self.ceiling:
            return ValueError("Ceiling cannot be empty")
        if not self.stock_level:
            return ValueError("Stock level cannot be empty")
        return 0