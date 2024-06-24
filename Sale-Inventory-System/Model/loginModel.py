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

    def send_otp_email(self,email, otp):
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

    """GET USERDATA FUNCTIONS"""
    def get_user_id(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT user_id FROM User WHERE username=%s'
                cursor.execute(sql, (self.username,))
                user_id = cursor.fetchone()
                vivdb.close()
                return user_id.get('user_id')

    def get_user_email(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT email FROM User WHERE username=%s'
                cursor.execute(sql, (self.username,))
                email = cursor.fetchone()
                vivdb.close()
                return email.get('email')

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
                else:
                    return None

    def get_user_type(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT user_type FROM User WHERE username=%s'
                cursor.execute(sql, (self.username,))
                userType = cursor.fetchone()
                print(userType)
                vivdb.close()
                return userType.get('user_type')
