from Utils import Database
class InventoryModel:
    def __init__(self,data:list=None,search_entry=None,table_name=None):
        self.search_query = search_entry
        self.table_name = table_name
        if data is not None:
            self.product_id = data[0]
            self.product_name = data[1]
            self.quantity = data[2]
            self.supplier = data[3]
            self.expiration_date = data[4]
            self.menu = data[5]
            self.cost = data[6]
            self.category = data[7]

    def search_data(self):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            if self.table_name == "Items":
            # Modify the SQL query to search in relevant fields. Here, it searches in the 'user_log' field.
            # Use '%' wildcards for partial matches. Adjust the field name as per your database schema.
                sql = """SELECT * FROM Items 
                        WHERE item_id LIKE %s 
                        OR user_id LIKE %s 
                        OR item_name LIKE %s 
                        OR quantity LIKE %s 
                        OR unit LIKE %s 
                        OR supplier LIKE %s 
                        OR exp_date LIKE %s 
                        OR category LIKE %s 
                        OR flooring LIKE %s 
                        OR ceiling LIKE %s 
                        OR stock_level LIKE %s"""
                search_pattern = f"%{self.search_query}%"
                cursor.execute(sql, (search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern))
            if self.table_name == "Supply":
                sql = """SELECT * FROM Supply 
                        WHERE supply_id LIKE %s 
                        OR user_id LIKE %s 
                        OR item_name LIKE %s 
                        OR quantity LIKE %s 
                        OR unit LIKE %s 
                        OR supplier LIKE %s 
                        OR exp_date LIKE %s 
                        OR menu_type LIKE %s 
                        OR flooring LIKE %s 
                        OR ceiling LIKE %s 
                        OR stock_level LIKE %s"""
                search_pattern = f"%{self.search_query}%"
                cursor.execute(sql, (search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,))
            if self.table_name == "Product":
                sql = """SELECT * FROM Product 
                        WHERE product_id LIKE %s 
                        OR user_id LIKE %s
                        OR product_name LIKE %s 
                        OR quantity LIKE %s 
                        OR price LIKE %s
                        OR exp_date LIKE %s
                        OR category LIKE %s
                        OR flooring LIKE %s
                        OR ceiling LIKE %s
                        OR stock_level LIKE %s"""
                search_pattern = f"%{self.search_query}%"
                cursor.execute(sql, (search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern,search_pattern))
            if self.table_name == "Recipes":
                sql = """SELECT * FROM Recipes 
                        WHERE recipe_id LIKE %s 
                        OR recipe_name LIKE %s 
                        OR user_id LIKE %s"""
                search_pattern = f"%{self.search_query}%"
                cursor.execute(sql, (search_pattern,search_pattern,search_pattern))
            result = cursor.fetchall()
        conn.close()
        return result

    def get_recipe_ingredients(self, recipe_id):
        # This is a placeholder. Implement the actual database query here.
        # It should return a list of tuples, each containing (ingredient_name, quantity)
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            query = """SELECT ingd_name, description, quantity, unit FROM Ingredients WHERE recipe_id = %s"""
            cursor.execute(query, (recipe_id,))
            ingds = cursor.fetchall()
        conn.close()
        return ingds if ingds else None
    
    
    def get_recipe_on_database(self):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            sql = """SELECT * FROM Recipes"""
            cursor.execute(sql)
            result = cursor.fetchall()
        conn.close()
        return result
    
    def get_recipe_column_names(self):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            sql = """SELECT * FROM Recipes LIMIT 0"""  # Modified to limit the results to 0 to avoid fetching data
            cursor.execute(sql)
            # Extracting column names from the cursor's description attribute
            column_names = [desc[0] for desc in cursor.description]
        conn.close()
        return column_names
    
    def get_supply_on_database(self):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            sql = """SELECT * FROM Supply"""
            cursor.execute(sql)
            result = cursor.fetchall()
        conn.close()
        return result
    
    def get_supply_column_names(self):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            sql = """SELECT * FROM Supply LIMIT 0"""  # Modified to limit the results to 0 to avoid fetching data
            cursor.execute(sql)
            # Extracting column names from the cursor's description attribute
            column_names = [desc[0] for desc in cursor.description]
        conn.close()
        return column_names

    def get_product_on_database(self):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            sql = """SELECT * FROM Product"""
            cursor.execute(sql)
            result = cursor.fetchall()
        conn.close()
        return result
    
    def get_product_column_names(self):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            sql = """SELECT * FROM Product LIMIT 0"""  # Modified to limit the results to 0 to avoid fetching data
            cursor.execute(sql)
            # Extracting column names from the cursor's description attribute
            column_names = [desc[0] for desc in cursor.description]
        conn.close()
        return column_names
    
    def get_items_on_database(self):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            sql = """SELECT * FROM Items"""
            cursor.execute(sql)
            result = cursor.fetchall()
        conn.close()
        return result
    
    def get_items_column_names(self):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            sql = """SELECT * FROM Items LIMIT 0"""  # Modified to limit the results to 0 to avoid fetching data
            cursor.execute(sql)
            # Extracting column names from the cursor's description attribute
            column_names = [desc[0] for desc in cursor.description]
        conn.close()
        return column_names
    
    def get_supplies_on_database(self):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            sql = """SELECT * FROM Supply"""
            cursor.execute(sql)
            result = cursor.fetchall()
        conn.close()
        return result
    
    def get_supplies_column_names(self):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            sql = """SELECT * FROM Supply LIMIT 0""" # Modified to limit the results to 0 to avoid fetching data
            cursor.execute(sql)
            # Extracting column names from the cursor's description attribute
            column_names = [desc[0] for desc in cursor.description]
        conn.close()
        return column_names