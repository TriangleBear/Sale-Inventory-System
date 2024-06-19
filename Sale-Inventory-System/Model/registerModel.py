import datetime
from Utils.Database import get_db_connection
from hashlib import sha256

def hash_pass(password):
    return sha256(password.encode('utf-8')).hexdigest()

class RegisterModel:
    @staticmethod
    def create_user(user_id, access, username, password, email):
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                hash_password = hash_pass(password)
                created_on = datetime.datetime.now()
                sql = """INSERT INTO User (user_id, user_type, username, passwordHash, email, created_on) 
                VALUES (%s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql, (user_id, access, username, hash_password, email, created_on))
                connection.commit()
            connection.close()
        return 0
