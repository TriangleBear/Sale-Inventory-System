from Utils.database import Database
class ManagerModel:
    def __init__(self,data:list):
        self.username = data[0]

    def get_manager_username(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT username FROM User WHERE user_type = 'Manager' AND username = %s""" 
                cursor.execute(sql, (self.username,))
                result = cursor.fetchone()
            connection.close()
        return result