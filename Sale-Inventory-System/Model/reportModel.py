from Utils import Database
class ReportModel:
    def __init__(self, master, reportController):
        super().__init__()
        self.reportController = reportController
        self.search_query = self.reportController.view.search_query.get()
        self.master = master

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
                sql = """SELECT * FROM UserActivity WHERE user_log LIKE %s"""
                search_pattern = f"%{self.search_query}%"
                cursor.execute(sql, (search_pattern,))
                result = cursor.fetchall()
            connection.close()
        return result

