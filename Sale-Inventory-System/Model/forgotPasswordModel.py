from hashlib import sha256
from Utils import Database, Credentials,Functions
import smtplib

class ForgotPasswordModel:
    def __init__(self, provided_email=None,provided_username=None,old_password=None,new_password=None,confirm_password=None):
        self.provided_email = provided_email
        self.provided_username = provided_username
        self.old_password = old_password
        self.new_password = new_password
        self.confirm_password = confirm_password
        self.generate_otp()

    
    def generate_otp(self):
        if self.new_password == None:
            self.otp = Functions.generate_otp()
    

    def send_otp_email(self,email,otp):
        Functions.send_otp_email(email,otp)

    def check_old_password(self):
        pass

    def check_old_password(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT passwordHash FROM User WHERE username=%s'
                cursor.execute(sql, (self.provided_username,))
                stored_password = cursor.fetchone()
                vivdb.close()
                if stored_password.get('passwordHash') == sha256(self.old_password.encode()).hexdigest():
                    return True
                else:
                    return False


    def update_password(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'UPDATE User SET passwordHash=%s WHERE username=%s'
                cursor.execute(sql, (sha256(self.new_password.encode()).hexdigest(), self.provided_username))
                vivdb.commit()
                vivdb.close()
                return
            
    def check_account_existence(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT email FROM User WHERE username=%s AND email=%s'
                cursor.execute(sql, (self.provided_username,self.provided_email))
                username = cursor.fetchone()
                vivdb.close()
                if username.get('username'):
                    return True
                else:
                    return ValueError('No account found with provided Username and Email')

    

    """GETTERS"""            
    def get_forgot_password_otp(self):
        return self.otp
    
    def get_user_password(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT passwordHash FROM User WHERE username=%s'
                cursor.execute(sql, (self.provided_username,))
                result = cursor.fetchone()
                print(result)
                if result:
                    vivdb.close()
                    return result.get('passwordHash')
                else:
                    return None