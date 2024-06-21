import datetime
from Utils.Database import get_db_connection
from hashlib import sha256

def hash_pass(password):
    return sha256(password.encode('utf-8')).hexdigest()

class RegisterModel:
    def __init__(self):
        pass
    @staticmethod
    def check_password_criteria(first, last, username, password, email):
        if len(password) < 8 or len(username) > 15:
            return ValueError("Password must be at least 8-15 characters long")
        if not any(char.isdigit() for char in password):
            return ValueError("Password must have at least one numeral")
        if not any(char.isupper() for char in password):
            return ValueError("Password must have at least one uppercase letter")
        if not any(char.islower() for char in password):
            return ValueError("Password must have at least one lowercase letter")
        if not any(char in ['$', '@', '#', '%', '!', '&', '*'] for char in password):
            return ValueError("Password must have at least one special character")
        if username in password:
            return ValueError("Username and password cannot be the same")
        if email in username:
            return ValueError("Email and username cannot be the same")
        if (first in password) or (last in password):
            return ValueError("First and last name cannot be part of the Password")
        return 0

    @staticmethod
    def create_user(user_id, access, first, last, username, password,email):

        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                hash_password = hash_pass(password)
                created_on = datetime.datetime.now()
                sql = """INSERT INTO User (user_id, user_type, fname, lname, username, passwordHash, email, created_on) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql, (user_id, access, first, last, username, hash_password, email, created_on))
                connection.commit()
            connection.close()
        return 0
