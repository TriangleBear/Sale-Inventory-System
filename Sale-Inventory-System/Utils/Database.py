#database.py
import pymysql
import pymysql.cursors
from Utils import Credentials
from contextlib import contextmanager


class Database:
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