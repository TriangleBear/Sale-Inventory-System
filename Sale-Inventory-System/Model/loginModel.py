# user.py
from hashlib import sha256
from Utils import Database,Credentials,Functions
from email.message import EmailMessage
import smtplib

class LoginModel:
    def __init__(self,provided_credentials:list):
        self.username = provided_credentials[0]
        self.password = provided_credentials[1]
        self.user_id = None
        self.otp = Functions.generate_otp()       

    def hash_pass(self,password):
        return sha256(password.encode('utf-8')).hexdigest()
    
    def check_password(self):
        self.user_id = self.get_user_id()
        if not self.get_user_id():
            return ValueError('No account with provided username')
        if self.hash_pass(self.password) != self.get_user_password():
            return ValueError('Incorrect password')
        return 0

    
    def get_login_otp(self):
        return self.otp

    """GET USERDATA FUNCTIONS"""
    def get_user_id(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT user_id FROM User WHERE username=%s'
                cursor.execute(sql, (self.username,))
                user_id = cursor.fetchone()
                vivdb.close()
                if user_id:
                    return user_id.get('user_id')
                else:
                    return None

    def get_user_email(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT email FROM User WHERE user_id=%s'
                cursor.execute(sql, (self.user_id,))
                email = cursor.fetchone()
                vivdb.close()
                return email.get('email')

    def get_user_password(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT passwordHash FROM User WHERE user_id=%s'
                cursor.execute(sql, (self.user_id,))
                result = cursor.fetchone()
                if result:
                    vivdb.close()
                    return result.get('passwordHash')
                else:
                    return None

    def get_user_type(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT user_type FROM User WHERE user_id=%s'
                cursor.execute(sql, (self.user_id,))
                userType = cursor.fetchone()
                vivdb.close()
                return userType.get('user_type')
