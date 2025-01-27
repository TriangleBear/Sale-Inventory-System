from Utils import Database
class SecurityModel:
    def __init__(self,search_entry=None,activityData:list=None):
        self.search_query = search_entry
        self.userActivityData = activityData
                
    
    def log_user_activity(self):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
                
            sql = """INSERT INTO UserActivity (user_id, user_log, log_date) VALUES (%s, %s, %s)"""
            cursor.execute(sql, (self.userActivityData[0], self.userActivityData[1], self.userActivityData[2]))
        conn.commit()
        conn.close()

    def fetch_data_from_user_activity(self):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            sql = """SELECT * FROM UserActivity"""
            cursor.execute(sql)
            result = cursor.fetchall()
        conn.close()
        return result
    
    def search_data(self):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            # Modify the SQL query to search in relevant fields. Here, it searches in the 'user_log' field.
            # Use '%' wildcards for partial matches. Adjust the field name as per your database schema.
            sql = """SELECT * FROM UserActivity WHERE log_id LIKE %s OR user_id LIKE %s OR user_log LIKE %s OR log_date LIKE %s"""
            search_pattern = f"%{self.search_query}%"
            cursor.execute(sql, (search_pattern,search_pattern,search_pattern,search_pattern))
            result = cursor.fetchall()
        conn.close()
        return result
    

    
    

