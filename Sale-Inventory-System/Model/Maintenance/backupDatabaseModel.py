from Utils import Database
class BackupDatabaseModel:
    def backupDatabase(self):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                try:
                    # Fetch the list of tables
                    cursor.execute("SHOW TABLES")
                    tables = cursor.fetchall()
                    
                    with open(backup_file_path, 'w') as f:
                        for table_name in tables:
                            # Write a comment with the table name
                            f.write(f"\n-- Table: {table_name[0]}\n")
                            
                            # Fetch the table creation statement
                            cursor.execute(f"SHOW CREATE TABLE {table_name[0]}")
                            create_table_stmt = cursor.fetchone()[1]
                            f.write(f"{create_table_stmt};\n\n")
                            
                            # Fetch all rows from the table
                            cursor.execute(f"SELECT * FROM {table_name[0]}")
                            rows = cursor.fetchall()
                            
                            # Write INSERT statements for each row
                            for row in rows:
                                values = ', '.join([f"'{val}'" if isinstance(val, str) else str(val) for val in row])
                                f.write(f"INSERT INTO {table_name[0]} VALUES ({values});\n")
                finally:
                    connection.close()

    def restoreDatabase(self):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                try:
                    with open(backup_file_path, 'r') as f:
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
                    connection.close()