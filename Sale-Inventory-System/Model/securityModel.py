from Utils import Database
class SecurityModel:
    def __init__(self,search_entry=None,activityData:list=None):
        self.search_query = search_entry
        self.userActivityData = activityData
        self.userActivity = []
        
        self.unpack_user_activity_data()

    def unpack_user_activity_data(self):
        if self.userActivityData != None:
            for data in self.userActivityData:
                self.userActivity.append(data)
        else:
            return
        
    
    def log_user_activity(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                
                sql = """INSERT INTO UserActivity (user_id, user_log, log_date) VALUES (%s, %s, %s)"""
                cursor.execute(sql, (self.userActivityData[0], self.userActivityData[1], self.userActivityData[2]))
            connection.commit()
            connection.close()

    def fetch_data_from_user_activity(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT * FROM UserActivity"""
                cursor.execute(sql)
                result = cursor.fetchall()
            connection.close()
        return result
    
    def search_data(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                # Modify the SQL query to search in relevant fields. Here, it searches in the 'user_log' field.
                # Use '%' wildcards for partial matches. Adjust the field name as per your database schema.
                sql = """SELECT * FROM UserActivity WHERE log_id LIKE %s"""
                search_pattern = f"%{self.search_query}%"
                cursor.execute(sql, (search_pattern,))
                result = cursor.fetchall()
            connection.close()
        return result
    

    
    

