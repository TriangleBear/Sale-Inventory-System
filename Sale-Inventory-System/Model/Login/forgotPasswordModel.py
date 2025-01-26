from hashlib import sha256
from Utils import Database, Functions
import smtplib

class ForgotPasswordModel:
    def __init__(self, user_id=None,provided_email=None,provided_username=None,new_password=None,confirm_password=None):
        self.provided_email = provided_email
        self.user_id = user_id
        self.provided_username = provided_username
        self.new_password = new_password
        self.confirm_password = confirm_password
        self.generate_otp()

    
    def generate_otp(self):
        if self.new_password == None:
            self.otp = Functions.generate_otp()

    def send_otp_email(self,email,otp):
        Functions.send_otp_email(email,otp)

    def confirm_password_update(self):
        error = self._checkPassInput()
        if error != None:
            return error
        
        error2 = self._check_old_password()
        if error2 != None:
            return error2
        
        return Functions.check_password_criteria(password=self.new_password,
                                                 username=self.provided_username,
                                                 email=self.provided_email,
                                                 fname=self.get_user_fname(),
                                                 lname=self.get_user_lname(),
                                                 old_password=self.get_user_password())

    def _checkPassInput(self):
        if self.new_password=='':
            return ValueError('No provided Password')
        if self.confirm_password=='':
            return ValueError('No provided confirm Password')
        if self.confirm_password != self.new_password:
            return ValueError('Please confirm Password')
        return

    def _check_old_password(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT passwordHash FROM User WHERE username=%s'
                cursor.execute(sql, (self.provided_username,))
                stored_password = cursor.fetchone()
                vivdb.close()
                if sha256(self.new_password.encode()).hexdigest() == stored_password.get('passwordHash')  :
                    return ValueError('New password must be different from old password')
                return

    def update_password(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'UPDATE User SET passwordHash=%s WHERE user_id=%s'
                cursor.execute(sql, (sha256(self.new_password.encode()).hexdigest(), self.user_id))
                vivdb.commit()
                vivdb.close()
                return

    def checkEmailInput(self):
        if self.provided_username == '' and self.provided_email == '':
            return ValueError('No provided Username and Email')
        if self.provided_username == '':
            return ValueError('No provided Username')
        if self.provided_email == '':
            return ValueError('No provided Email')
        return

    def check_account_existence(self):
        error = self.checkEmailInput()
        if error != None:
            return error
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT user_id FROM User WHERE username=%s AND email=%s'
                cursor.execute(sql, (self.provided_username,self.provided_email))
                userID = cursor.fetchone()
                vivdb.close()
                if userID:
                    return 0
                else:
                    return ValueError('No account found with provided Username or Email')

    """GETTERS"""            
    def get_forgot_password_otp(self):
        return self.otp
    
    def get_user_fname(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT fname FROM User WHERE user_id=%s'
                cursor.execute(sql, (self.user_id))
                fname = cursor.fetchone()
                vivdb.close()
                return fname.get('fname')
                    
    def get_user_lname(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT lname FROM User WHERE user_id=%s'
                cursor.execute(sql, (self.user_id))
                lname = cursor.fetchone()
                vivdb.close()
                return lname.get('lname')
    
    def get_user_password(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT passwordHash FROM User WHERE user_id=%s'
                cursor.execute(sql, (self.user_id,))
                password = cursor.fetchone()
                vivdb.close()
                return password.get('passwordHash')
            
    def get_user_id(self):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                sql = 'SELECT user_id FROM User WHERE username=%s AND email=%s'
                cursor.execute(sql, (self.provided_username,self.provided_email))
                userID = cursor.fetchone()
                vivdb.close()
                return userID.get('user_id')