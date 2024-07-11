from Utils import Database
import tkinter as tk
from tkinter import filedialog
from datetime import datetime, date
from icecream import ic
import os
import pymysql
class BackupDatabaseModel:

    def backupDatabase(self):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SHOW TABLES")
                tables = cursor.fetchall()
                if not tables:
                    print("No tables found in the database.")
                    return
                
                # Ensure the Sale-Inventory-System\Backups folder exists
                backup_folder = 'Sale-Inventory-System\\Backups'
                if not os.path.exists(backup_folder):
                    os.makedirs(backup_folder)
                
                # Format the current date and time to append to the file name
                date_time_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                backup_file_name = f"{backup_folder}\\backup_{date_time_str}.sql"

                with open(backup_file_name, 'w') as f:
                    # Ensure the User table is backed up first
                    user_table = None
                    other_tables = []
                    for table in tables:
                        table_name = table['Tables_in_viviandbTEST']  # Adjust the index if necessary
                        if table_name.lower() == 'user':
                            user_table = table_name
                        else:
                            other_tables.append(table_name)
                    
                    # Backup the User table first if it exists
                    if user_table:
                        self.backup_table(cursor, f, user_table)
                    
                    # Backup other tables
                    for table_name in other_tables:
                        self.backup_table(cursor, f, table_name)
                    
                    f.flush()
        print(f"Backup completed successfully. File saved in {backup_file_name}")

    def backup_table(self, cursor, file, table_name):
        # Fetch and write CREATE TABLE statement
        cursor.execute(f"SHOW CREATE TABLE {table_name}")
        create_table_stmt = cursor.fetchone()["Create Table"]
        file.write(f"{create_table_stmt};\n\n")
        
        # Fetch and write data
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                values = ', '.join([
                    "''" if val is None else f"'{val}'" if isinstance(val, (str, datetime, date)) else str(val)
                    for val in row.values()
                ])
                file.write(f"INSERT INTO {table_name} VALUES ({values});\n")
        else:
            print(f"No data found in table {table_name}.")

    def backup_table(self, cursor, file, table_name):
        # Fetch and write CREATE TABLE statement
        cursor.execute(f"SHOW CREATE TABLE {table_name}")
        create_table_stmt = cursor.fetchone()["Create Table"]
        file.write(f"{create_table_stmt};\n\n")
        
        # Fetch and write data
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                values = ', '.join([
                    "' '" if val is None else f"'{val}'" if isinstance(val, (str, datetime, date)) else str(val)
                    for val in row.values()
                ])
                file.write(f"INSERT INTO {table_name} VALUES ({values});\n")
        else:
            print(f"No data found in table {table_name}.")
        
    def restoreDatabase(self):
        file_name = filedialog.askopenfilename(
            title="Select a database backup file",
            filetypes=(("SQL Files", "*.sql"), ("All Files", "*.*"))
        )
        if not file_name:
            print("No file selected.")
            return

        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                try:
                    # Disable foreign key checks
                    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

                    # Drop existing tables
                    cursor.execute("SHOW TABLES")
                    tables = cursor.fetchall()
                    for table in tables:
                        table_name = table['Tables_in_viviandbTEST']
                        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

                    # Restore from backup
                    with open(file_name, 'r') as f:
                        sql_content = f.read()
                        sql_statements = sql_content.split(';')
                        for statement in sql_statements:
                            if not statement.strip():
                                continue
                            try:
                                cursor.execute(statement)
                            except pymysql.err.IntegrityError as e:
                                if e.args[0] == 1062:  # Duplicate entry error code
                                    print(f"Duplicate entry for statement: {statement}. Ignoring and continuing.")
                                    continue  # Ignore and move to the next statement
                                else:
                                    raise  # Re-raise the exception if it's not a duplicate entry error

                    # Re-enable foreign key checks
                    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
                    conn.commit()
                except Exception as e:
                    conn.rollback()
                    print(f"An error occurred: {e}")
                finally:
                    conn.close()