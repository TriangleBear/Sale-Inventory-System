import pymysql
import json

creds = r".creds/credentials.json"

with open(creds, "r") as f:
    credentials = json.load(f)

timeout = 10
vivdb = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="viviandb",
    host=credentials["host"],
    password=credentials["password"],
    read_timeout=timeout,
    port=22577,
    user=credentials["username"],
    write_timeout=timeout,
)

print("test for database connection")
print()
print(vivdb)
