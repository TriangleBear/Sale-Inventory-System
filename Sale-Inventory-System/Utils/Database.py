#database.py
import pymysql
import pymysql.cursors
from Utils.credentials import Credentials
from contextlib import contextmanager


@contextmanager
def get_db_connection():
    vivdb = pymysql.connect(
        host=Credentials.host,
        user=Credentials.user,
        password=Credentials.password,
        db="viviandbTEST",
        port=22577,
        cursorclass=pymysql.cursors.DictCursor,
    )
    yield vivdb
    vivdb.close()

def get_sender_email():
    return Credentials.sender_email

def get_sender_password():
    return Credentials.sender_password