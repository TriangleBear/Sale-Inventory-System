import datetime
from Utils import Database, Functions
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

    def check_password_criteria(self):
        Functions.check_password_criteria(self.password, self.username, self.email, self.fname, self.lname)

    def create_user(self):
        user_id = Functions.generate_unique_id(self.user_type)
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                hash_password = self.hash_pass(self.password)
                created_on = datetime.datetime.now()
                sql = """INSERT INTO User (user_id, fname, lname, user_type,birthdate,contact_num, email, address, username, passwordHash,created_on) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"""
                #user_id,fname, lname, user_type, birthdate, contact_num, email,address, username, password, created_on
                cursor.execute(sql, (user_id, self.fname, self.lname, self.user_type,self.birthdate,self.contact_num,self.email, self.address, self.username, hash_password, created_on))
                connection.commit()
            connection.close()
        return 0


    
