from Utils import Database
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
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
                    for table in tables:
                        if table:  # Check if the tuple is not empty
                            table_name = table['Tables_in_nameit']  # Adjust the index if necessary
                            
                            # Fetch and write CREATE TABLE statement
                            cursor.execute(f"SHOW CREATE TABLE {table_name}")
                            create_table_stmt = cursor.fetchone()["Create Table"]
                            f.write(f"{create_table_stmt};\n\n")
                            
                            # Fetch and write data
                            cursor.execute(f"SELECT * FROM {table_name}")
                            rows = cursor.fetchall()
                            if rows:
                                for row in rows:
                                    values = ', '.join([f"'{val}'" if isinstance(val, str) else str(val) for val in row.values()])
                                    f.write(f"INSERT INTO {table_name} VALUES ({values});\n")
                            else:
                                print(f"No data found in table {table_name}.")
                    f.flush()
        print(f"Backup completed successfully. File saved in {backup_file_name}")

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
                    # Drop existing tables
                    cursor.execute("SHOW TABLES")
                    tables = cursor.fetchall()
                    for table in tables:
                        table_name = table['Tables_in_nameit']
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
                    conn.commit()
                except Exception as e:
                    conn.rollback()
                    print(f"An error occurred: {e}")
                finally:
                    conn.close()