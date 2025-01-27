from Utils import Database
import sqlite3
class MaintenanceModel:
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
        result = []
        try:
            with Database.get_db_connection() as connection:
                cursor = conn.cursor()
                search_pattern = f"%{self.search_query}%"
                if self.table_name == "Items":
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
                    cursor.execute(sql, (search_pattern,) * 11)
                elif self.table_name == "Supply":
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
                    cursor.execute(sql, (search_pattern,) * 11)
                elif self.table_name == "Product":
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
                    cursor.execute(sql, (search_pattern,) * 10)
                elif self.table_name == "Recipes":
                    sql = """SELECT * FROM Recipes 
                            WHERE recipe_id LIKE %s 
                            OR recipe_name LIKE %s 
                            OR user_id LIKE %s"""
                    cursor.execute(sql, (search_pattern,) * 3)
                elif self.table_name == "User":
                    sql = """SELECT * FROM User
                            WHERE user_id LIKE %s 
                            OR fname LIKE %s
                            OR lname LIKE %s
                            OR user_type LIKE %s
                            OR birthdate LIKE %s
                            OR contact_num LIKE %s
                            OR email LIKE %s
                            OR address LIKE %s
                            OR username LIKE %s
                            OR created_on LIKE %s"""
                    cursor.execute(sql, (search_pattern,) * 10)
                else:
                    raise ValueError("Invalid table name")
                result = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
        except ValueError as e:
            print(e)
        finally:
            connection.close()
        return result
    
    def fetch_data_from_user_activity(self):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            sql = """SELECT * FROM UserActivity"""
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.close()
        return result
    
    def get_recipe_on_database(self):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            sql = """SELECT * FROM Recipes"""
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.close()
        return result
    
    def get_recipe_column_names(self):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            sql = """SELECT * FROM Recipes LIMIT 0"""  # Modified to limit the results to 0 to avoid fetching data
            cursor.execute(sql)
            # Extracting column names from the cursor's description attribute
            column_names = [desc[0] for desc in cursor.description]
        connection.close()
        return column_names
    
    def get_supply_on_database(self):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            sql = """SELECT * FROM Supply"""
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.close()
        return result
    
    def get_supply_column_names(self):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            sql = """SELECT * FROM Supply LIMIT 0"""  # Modified to limit the results to 0 to avoid fetching data
            cursor.execute(sql)
            # Extracting column names from the cursor's description attribute
            column_names = [desc[0] for desc in cursor.description]
        connection.close()
        return column_names

    def get_product_on_database(self):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            sql = """SELECT * FROM Product"""
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.close()
        return result
    
    def get_product_column_names(self):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            sql = """SELECT * FROM Product LIMIT 0"""  # Modified to limit the results to 0 to avoid fetching data
            cursor.execute(sql)
            # Extracting column names from the cursor's description attribute
            column_names = [desc[0] for desc in cursor.description]
        connection.close()
        return column_names
    
    def get_items_on_database(self):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            sql = """SELECT * FROM Items"""
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.close()
        return result
    
    def get_items_column_names(self):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            sql = """SELECT * FROM Items LIMIT 0"""  # Modified to limit the results to 0 to avoid fetching data
            cursor.execute(sql)
            # Extracting column names from the cursor's description attribute
            column_names = [desc[0] for desc in cursor.description]
        connection.close()
        return column_names
    
    def get_supplies_on_database(self):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            sql = """SELECT * FROM Supply"""
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.close()
        return result
    
    def get_supplies_column_names(self):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            sql = """SELECT * FROM Supply LIMIT 0""" # Modified to limit the results to 0 to avoid fetching data
            cursor.execute(sql)
            # Extracting column names from the cursor's description attribute
            column_names = [desc[0] for desc in cursor.description]
        connection.close()
        return column_names
    
    def get_users_on_database(self):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            sql = """SELECT * FROM User"""
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.close()
        return result
    
    def get_users_column_names(self):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            sql = """SELECT * FROM User LIMIT 0""" # Modified to limit the results to 0 to avoid fetching data
            cursor.execute(sql)
            # Extracting column names from the cursor's description attribute
            column_names = [desc[0] for desc in cursor.description]
        connection.close()
        return column_names
    