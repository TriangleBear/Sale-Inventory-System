import datetime
import pymysql
from pymysql.cursors import DictCursor
import json
from hashlib import sha256
import os

creds = r".creds/credentials.json"

# Check if the credentials file exists
if not os.path.exists(creds):
    raise FileNotFoundError(f"Credentials file not found: {creds}")

with open(creds, "r") as f:
    credentials = json.load(f)

def hash_pass(password):
    return sha256(password.encode('utf-8')).hexdigest()

class User:
    @staticmethod
    def check_username(username):
        vivdb = pymysql.connect(
            host=credentials["host"],
            user=credentials["username"],
            password=credentials["password"],
            db="viviandbTEST",
            port=22577,
            cursorclass=pymysql.cursors.DictCursor,
        )
        try:
            with vivdb.cursor() as cursor:
                sql = "SELECT * FROM User WHERE username=%s"
                cursor.execute(sql, (username,))
                result = cursor.fetchone()
                return result
        finally:
            vivdb.close()

    def check_password(store_password, provided_password):
        if store_password == hash_pass(provided_password):
            return True
        return False
        

    @staticmethod
    def get_password(username):
        vivdb = pymysql.connect(
            host=credentials["host"],
            user=credentials["username"],
            password=credentials["password"],
            db="viviandbTEST",
            port=22577,
            cursorclass=pymysql.cursors.DictCursor,
        )
        try:
            with vivdb.cursor() as cursor:
                sql = "SELECT passwordHash FROM User WHERE username=%s"
                cursor.execute(sql, (username,))
                stored_password = cursor.fetchone()
                if stored_password:
                    return stored_password['passwordHash']
                return None
        finally:
            vivdb.close()
            