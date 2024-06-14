import datetime
import pymysql
from pymysql.cursors import DictCursor
import json
from hashlib import sha256
#webhook applied
creds = r".creds/credentials.json"

with open(creds, "r") as f:
    credentials = json.load(f)


def hash_pass(password):
    return sha256(password.encode('utf-8')).hexdigest()


class User:
    @staticmethod
    def where_username(username):
        vivdb = pymysql.connect(
            host=credentials["host"],
            user=credentials["username"],
            password=credentials["password"],
            db="viviandbTEST",
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

    @staticmethod
    def check_password(stored_password, provided_password):
        return stored_password == hash_pass(provided_password)


class Registration:
    @staticmethod
    def create_user(username, password, email):
        connection = pymysql.connect(
            host=credentials["host"],
            user=credentials["username"],
            password=credentials["password"],
            db="viviandbTEST",
            cursorclass=pymysql.cursors.DictCursor,
        )
        try:
            with connection.cursor() as cursor:
                hash_password = hash_pass(password)
                created_on = datetime.datetime.now()
                sql = "INSERT INTO User (username, password, email, created_on) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (username, hash_password, email, created_on))
                connection.commit()
        finally:
            connection.close()
