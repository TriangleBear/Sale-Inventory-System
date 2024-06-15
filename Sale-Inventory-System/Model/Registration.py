import pymysql.cursors
import json
import datetime
from Utils.Database import get_db_connection
from hashlib import sha256

credentials = json.load(open("D:\Programming\CS 304\Sale-Inventory-System\Sale-Inventory-System\Model\credentials.json"))

def hash_pass(password):
    return sha256(password.encode('utf-8')).hexdigest()

class Registration:
    @staticmethod
    def create_user(number, access, username, password, email):
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                hash_password = hash_pass(password)
                created_on = datetime.datetime.now()
                sql = "INSERT INTO User (user_id, user_type, username, passwordHash, email, created_on) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (number, access, username, hash_password, email, created_on))
                connection.commit()
            connection.close()