from Utils import Database
class StaffModel:
    def __init__(self):
        pass

    def get_staff_username(self):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            sql = """SELECT username FROM User WHERE user_type = 'Staff' AND username = %s""" 
            cursor.execute(sql, (self.username,))
            result = cursor.fetchone()
        conn.close()
        return result