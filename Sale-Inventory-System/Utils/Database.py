import pymysql
import pymysql.cursors
import json
from contextlib import contextmanager

# Load credentials once to avoid repeated file I/O operations
with open("D:\Programming\CS 304\Sale-Inventory-System\Sale-Inventory-System\Model\credentials.json") as f:
    credentials = json.load(f)

@contextmanager
def get_db_connection():
    vivdb = pymysql.connect(
        host=credentials["host"],
        user=credentials["username"],
        password=credentials["password"],
        db="viviandbTEST",
        port=22577,
        cursorclass=pymysql.cursors.DictCursor,
    )
    try:
        yield vivdb
    finally:
        vivdb.close()
