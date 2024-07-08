from Utils import Database
import tkinter as tk
from tkinter import filedialog
from icecream import ic
class BackupDatabaseModel:
    def backupDatabase(self):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SHOW TABLES")
                tables = cursor.fetchall()
                if not tables:
                    print("No tables found in the database.")
                    return

                with open("backup.sql", 'w') as f:
                    for table in tables:
                        # Ensure table has at least one element
                        if table:  # Check if the tuple is not empty
                            ic(tables)
                            table_name = table['Tables_in_viviandbTEST']  # Adjust the index if necessary
                            cursor.execute(f"SELECT * FROM {table_name}")
                            rows = cursor.fetchall()
                            if rows:
                                for row in rows:
                                    values = ', '.join([f"'{val}'" if isinstance(val, str) else str(val) for val in row.values()])
                                    f.write(f"INSERT INTO {table_name} VALUES ({values});\n")
                            else:
                                print(f"No data found in table {table_name}.")
                    f.flush()
        print("Backup completed successfully.")
        conn.close()

    def restoreDatabase(self):
        file_name = filedialog.askopenfilename(
            title="Select a database backup file",
            filetypes=(("SQL Files", "*.sql"), ("All Files", "*.*"))
        )
        # Check if a file was selected
        if not file_name:
            print("No file selected.")
            return

        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                try:
                    with open(file_name, 'r') as f:
                        # Read the file line by line
                        lines = f.readlines()
                        table_name = None
                        create_table_stmt = None
                        insert_stmt = None
                        for line in lines:
                            # Skip empty lines
                            if not line.strip():
                                continue
                            
                            # Check if the line is a comment
                            if line.startswith('--'):
                                # Extract the table name from the comment
                                table_name = line.split()[2]
                            elif line.startswith('CREATE TABLE'):
                                # Extract the CREATE TABLE statement
                                create_table_stmt = line
                            elif line.startswith('INSERT INTO'):
                                # Extract the INSERT statement
                                insert_stmt = line
                            else:
                                # Execute the statement
                                cursor.execute(line)
                finally:
                    conn.close()