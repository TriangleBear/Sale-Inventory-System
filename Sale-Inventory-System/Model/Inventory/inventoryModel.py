from Utils import Database
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
    
    def get_recipe_on_database(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT * FROM Recipes"""
                cursor.execute(sql)
                result = cursor.fetchall()
            connection.close()
        return result
    
    def get_recipe_column_names(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT * FROM Recipes LIMIT 0"""  # Modified to limit the results to 0 to avoid fetching data
                cursor.execute(sql)
                # Extracting column names from the cursor's description attribute
                column_names = [desc[0] for desc in cursor.description]
            connection.close()
        return column_names

    def get_product_on_database(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT * FROM Product"""
                cursor.execute(sql)
                result = cursor.fetchall()
            connection.close()
        return result
    
    def get_product_column_names(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT * FROM Product LIMIT 0"""  # Modified to limit the results to 0 to avoid fetching data
                cursor.execute(sql)
                # Extracting column names from the cursor's description attribute
                column_names = [desc[0] for desc in cursor.description]
            connection.close()
        return column_names
    
    def get_items_on_database(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT * FROM Items"""
                cursor.execute(sql)
                result = cursor.fetchall()
            connection.close()
        return result
    
    def get_items_column_names(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT * FROM Items LIMIT 0"""  # Modified to limit the results to 0 to avoid fetching data
                cursor.execute(sql)
                # Extracting column names from the cursor's description attribute
                column_names = [desc[0] for desc in cursor.description]
            connection.close()
        return column_names
    
    def get_supplies_on_database(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT * FROM Supply"""
                cursor.execute(sql)
                result = cursor.fetchall()
            connection.close()
        return result
    
    def get_supplies_column_names(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT * FROM Supply LIMIT 0""" # Modified to limit the results to 0 to avoid fetching data
                cursor.execute(sql)
                # Extracting column names from the cursor's description attribute
                column_names = [desc[0] for desc in cursor.description]
            connection.close()
        return column_names