# user.py
from hashlib import sha256
from Utils.Database import get_db_connection
from Utils.credentials import Credentials
from email.message import EmailMessage
import smtplib
import random

def hash_pass(password):
    return sha256(password.encode('utf-8')).hexdigest()



class User:
    def generate_otp():
        otp = random.randint(100000, 999999)
        return otp

    @staticmethod
    def check_username(username):
        with get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = """SELECT * FROM User WHERE username=%s"""
                cursor.execute(sql, (username,))
                return cursor.fetchone()

    @staticmethod
    def check_password(stored_password, provided_password):
        return stored_password == hash_pass(provided_password)

    @staticmethod
    def get_password(username):
        with get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = """SELECT passwordHash FROM User WHERE username=%s"""
                cursor.execute(sql, (username,))
                result = cursor.fetchone()
                if result:
                    return result['passwordHash']
                return None
            
    def get_email(self, user_id):
        with get_db_connection() as vivbd:
            with vivbd.cursor() as cursor:
                sql = """SELECT email FROM User WHERE user_id=%s"""
                cursor.execute(sql, (user_id,))
                user = cursor.fetchone()
                return user.get('email')
            
    def get_user_id(self, username):
        with get_db_connection() as vivbd:
            with vivbd.cursor() as cursor:
                sql = """SELECT user_id FROM User WHERE username=%s"""
                cursor.execute(sql, (username,))
                user = cursor.fetchone()
                return user.get('user_id')
            
    def send_otp_email(email, otp):
        sender_email = Credentials.appemail
        sender_password = Credentials.apppassword

        msg = EmailMessage()
        msg['Subject'] = "OTP Verification"
        msg['From'] = sender_email
        msg['To'] = email
        msg.set_content(f"Your OTP is {otp}")

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

    def validate_otp(otp, user_input):
        return otp == int(user_input)
