# user.py
from hashlib import sha256
from Utils import Database,Credentials,Functions
from email.message import EmailMessage
import smtplib

class LoginModel:
    def __init__(self,provided_credentials:list):
        self.username = provided_credentials[0]
        self.password = provided_credentials[1]
        self.otp = Functions.generate_otp()       

    def hash_pass(self,password):
        return sha256(password.encode('utf-8')).hexdigest()
            
    def check_password(self):
        return self.stored_password == self.hash_pass(self.password)
    
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
                elif user_id == None:
                    return ValueError("User ID not found")

    def get_user_email(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT email FROM User WHERE username=%s'
                cursor.execute(sql, (self.username,))
                email = cursor.fetchone()
                vivdb.close()
                if email:
                    return email.get('email')
                elif email == None:
                    return ValueError('User Email not found')

    def get_user_password(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT passwordHash FROM User WHERE username=%s'
                cursor.execute(sql, (self.username,))
                result = cursor.fetchone()
                print(result)
                if result:
                    vivdb.close()
                    return result.get('passwordHash')
                elif result == None:
                    return ValueError('User Password not found')

    def get_user_type(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT user_type FROM User WHERE username=%s'
                cursor.execute(sql, (self.username,))
                userType = cursor.fetchone()
                print(userType)
                vivdb.close()
                if userType:
                    return userType.get('user_type')
                elif userType == None:
                    return ValueError('User Type not found')
