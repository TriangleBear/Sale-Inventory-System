import datetime
from Utils import Database
from hashlib import sha256



class RegisterModel:
    def __init__(self,data:list):
        #user_id,fname, lname, user_type, birthdate, contact_num, email,address, username, password, created_on
        self.fname = data[0]
        self.lname = data[1]
        self.user_type = data[2]
        self.birthdate = data[3]
        self.contact_num = data[4]
        self.email = data[5]
        self.address = data[6]
        self.username = data[7]
        self.password = data[8]

    def hash_pass(self,password):
        return sha256(password.encode('utf-8')).hexdigest()

    def check_password_criteria(self,data:list):
        # first, last, username, password, email
        if len(self.password) < 8 or len(self.username) > 15:
            return ValueError("Password must be at least 8-15 characters long")
        if not any(char.isdigit() for char in self.password):
            return ValueError("Password must have at least one numeral")
        if not any(char.isupper() for char in self.password):
            return ValueError("Password must have at least one uppercase letter")
        if not any(char.islower() for char in self.password):
            return ValueError("Password must have at least one lowercase letter")
        if not any(char in ['$', '@', '#', '%', '!', '&', '*'] for char in self.password):
            return ValueError("Password must have at least one special character")
        if self.username in self.password:
            return ValueError("Username and password cannot be the same")
        if self.email in self.username:
            return ValueError("Email and username cannot be the same")
        if (self.fname in self.password) or (self.lname in self.password):
            return ValueError("First and last name cannot be part of the Password")
        return 0

    @staticmethod
    def create_user(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                hash_password = hash_pass(password)
                created_on = datetime.datetime.now()
                sql = """INSERT INTO User (user_id, user_type, fname, lname, username, passwordHash, email, address, created_on) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql, (user_id, access, first, last, username, hash_password, email, address, created_on))
                connection.commit()
            connection.close()
        return 0
