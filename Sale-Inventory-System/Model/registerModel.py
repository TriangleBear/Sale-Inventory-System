import datetime
from Utils.Database import get_db_connection
from hashlib import sha256

def hash_pass(password):
    return sha256(password.encode('utf-8')).hexdigest()

class RegisterModel:
    @staticmethod
    def check_password_criteraia(email, username, password):
        if len(password) < 8 or len(username) > 15:
            raise ValueError("Password must be at least 8-15 characters long")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must have at least one numeral")
        if not any(char.isupper() for char in password):
            raise ValueError("Password must have at least one uppercase letter")
        if not any(char.islower() for char in password):
            raise ValueError("Password must have at least one lowercase letter")
        if not any(char in ['$', '@', '#', '%', '!', '&', '*'] for char in password):
            raise ValueError("Password must have at least one special character")
        return 0

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
