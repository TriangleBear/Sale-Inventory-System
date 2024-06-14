import pymysql.cursors
import json
import os
import datetime
from hashlib import sha256

creds = r".creds/credentials.json"

# Check if the credentials file exists
if not os.path.exists(creds):
    raise FileNotFoundError(f"Credentials file not found: {creds}")

with open(creds, "r") as f:
    credentials = json.load(f)

def hash_pass(password):
    return sha256(password.encode('utf-8')).hexdigest()

class Registration:
    @staticmethod
    def create_user(number, access, username, password, email):
        connection = pymysql.connect(
            host=credentials["host"],
            user=credentials["username"],
            password=credentials["password"],
            db="viviandbTEST",
            port=22577,
            cursorclass=pymysql.cursors.DictCursor,
        )
        try:
            with connection.cursor() as cursor:
                hash_password = hash_pass(password)
                created_on = datetime.datetime.now()
                sql = "INSERT INTO User (user_id, user_type, username, passwordHash, email, created_on) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (number, access, username, hash_password, email, created_on))
                connection.commit()
        finally:
            connection.close()
