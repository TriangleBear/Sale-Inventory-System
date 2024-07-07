from Utils import Database
class ManagerModel:
    def __init__(self):
        pass

    def get_manager_username(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT username FROM User WHERE user_type = 'Manager' AND username = %s""" 
                cursor.execute(sql, (self.username,))
                result = cursor.fetchone()
            connection.close()
        return result if result else None
    
    def get_recipe_name_and_recipe_id(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT recipe_id,recipe_name FROM Recipes"""
                cursor.execute(sql)
                result = cursor.fetchall()
            connection.close()
        return result
    
    def get_recipe_name_by_id(self, recipe_id):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT recipe_name FROM Recipes WHERE recipe_id = %s"""
                cursor.execute(sql, (recipe_id,))
                result = cursor.fetchone()
            connection.close()
        return result
    
    def get_supply_name_and_supply_id(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql ="""SELECT supply_id,item_name FROM Supply"""
                cursor.execute(sql)
                result = cursor.fetchall()
            connection.close()
        return result if result else None