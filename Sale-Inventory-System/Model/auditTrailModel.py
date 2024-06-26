import datetime
from Utils.database import Database
class AuditLog:
    def __init__(self):
        self.entries = []

    def add_entry(self, log_id, user_id, user_log):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                datetime_now = datetime.now()
                sql = """INSERT INTO UserActivity (log_id, user_id, user_log, created_on) VALUES (%s, %s, %s, %s)"""
                cursor.execute(sql, (log_id, user_id, user_log, datetime_now))
            connection.commit()
            connection.close()

    def get_entries(self):
        return self.entries