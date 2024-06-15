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
    try:
        yield vivdb
    finally:
        vivdb.close()
