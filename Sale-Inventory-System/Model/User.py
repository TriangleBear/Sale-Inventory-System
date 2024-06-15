# user.py
from hashlib import sha256
from Utils.Database import get_db_connection

def hash_pass(password):
    return sha256(password.encode('utf-8')).hexdigest()

class User:
    @staticmethod
    def check_username(username):
        with get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = "SELECT * FROM User WHERE username=%s"
                cursor.execute(sql, (username,))
                return cursor.fetchone()

    @staticmethod
    def check_password(stored_password, provided_password):
        return stored_password == hash_pass(provided_password)

    @staticmethod
    def get_password(username):
        with get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = "SELECT passwordHash FROM User WHERE username=%s"
                cursor.execute(sql, (username,))
                result = cursor.fetchone()
                if result:
                    return result['passwordHash']
                return None
