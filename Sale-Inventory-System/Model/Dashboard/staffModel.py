from Utils import Database
class StaffModel:
    def __init__(self):
        pass

    def get_staff_username(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT username FROM User WHERE user_type = 'Staff' AND username = %s""" 
                cursor.execute(sql, (self.username,))
                result = cursor.fetchone()
            connection.close()
        return result