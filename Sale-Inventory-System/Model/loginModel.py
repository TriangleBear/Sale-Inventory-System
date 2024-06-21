# user.py
from hashlib import sha256
from Utils.Database import get_db_connection
from Utils.credentials import Credentials
from email.message import EmailMessage
import smtplib
import random

def hash_pass(password):
    return sha256(password.encode('utf-8')).hexdigest()


class LoginModel:
    def __init__(self,provided_credentials:list):
        self.provided_credentials = [cred for cred in provided_credentials]
    
    def getLevelOfAccess(self)->str:
        #check if username and password exists and matches data within database if true get levelaccess and return it as a string "Manager/Admin" or Staff, else return false
        username = self.provided_credentials[0]
        password = self.provided_credentials[1]
        print(f"username: {username}, password: {password}")
        if username == "ej" and password == "abcdefg":
            return ["Manager", "010102"] #and return userID// return ["Manger", user ID]
        elif username == "kurt" and password == "123":
            return ["Staff","010103"]
        else:
            return False
    def generate_otp():
        otp = random.randint(100000, 999999)
        return otp

    @staticmethod
    def check_username(username):
        with get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT * FROM User WHERE username=%s'
                cursor.execute(sql, (username,))
                userdata = cursor.fetchone()
                print(userdata)
                vivdb.close()
                return userdata

    @staticmethod
    def check_password(stored_password, provided_password):
        return stored_password == hash_pass(provided_password)

    @staticmethod
    def get_password(username):
        with get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT passwordHash FROM User WHERE username=%s'
                cursor.execute(sql, (username,))
                result = cursor.fetchone()
                print(result)
                if result:
                    vivdb.close()
                    return result['passwordHash']
                return None
    @staticmethod     
    def get_email(username):
        with get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT email FROM User WHERE username=%s'
                cursor.execute(sql, (username,))
                user = cursor.fetchone()
                vivdb.close()
                return user.get('email')

    def send_otp_email(email, otp):
        sender_email = Credentials.appemail
        sender_password = Credentials.apppass

        msg = EmailMessage()
        msg['Subject'] = "OTP Verification"
        msg['From'] = sender_email
        msg['To'] = email
        msg.set_content(f"Your OTP is {otp}")

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                print(f"From send_otp_email (sender_email): {sender_email}")
                server.send_message(msg)
            print("OTP sent successfully!")
        except Exception as e:
            print(f"Failed to send OTP: {e}")