#database.py
import sqlite3
from contextlib import contextmanager
import os
import icecream as ic

class Database:
    @contextmanager
    def get_db_connection():
        db_path = 'SIMS.db'
        if not os.path.exists(db_path):
            ic.ic('Database not found, creating new database')
            open(db_path, 'w').close()

        simsdb = sqlite3.connect(db_path)
        ic.ic('Database connected')
        simsdb.row_factory = sqlite3.Row
        ic.ic('Database row factory set')

        yield simsdb

    @staticmethod
    def init_db_all():
        

        user_table = '''CREATE TABLE IF NOT EXISTS User (
            user_id TEXT PRIMARY KEY,
            fname TEXT,
            lname TEXT,
            user_type TEXT,
            birthdate DATE,
            contact_num TEXT,
            email TEXT,
            address TEXT,
            username TEXT,
            passwordHash TEXT,
            created_on DATETIME
        )'''

        userActivity_table = '''CREATE TABLE IF NOT EXISTS UserActivity (
            log_id TEXT PRIMARY KEY,
            user_id TEXT,
            user_log TEXT,
            log_date DATETIME,
            FOREIGN KEY (user_id) REFERENCES Members(user_id)
        )'''

        ingredient_table = '''CREATE TABLE IF NOT EXISTS Ingredient (
            ingd_id TEXT PRIMARY KEY,
            recipe_id TEXT,
            user_id TEXT,
            ingd_name TEXT,
            description TEXT,
            quantity INT,
            unit TEXT,
            FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id),
            FOREIGN KEY (user_id) REFERENCES User(user_id)
        )'''

        recipe_table='''CREATE TABLE IF NOT EXISTS Recipe (
            recipe_id TEXT PRIMARY KEY,
            recipe_name TEXT,
            user_id TEXT,
            FOREIGN KEY (user_id) REFERENCES User(user_id)
        )'''

        product_table = '''CREATE TABLE IF NOT EXISTS Product (
            product_id TEXT PRIMARY KEY,
            user_id TEXT,
            product_name TEXT,
            quantity INT,
            price FLOAT,
            exp_date DATE,
            category TEXT,
            flooring FLOAT,
            ceiling FLOAT,
            stock_level TEXT,
            FOREIGN KEY (user_id) REFERENCES User(user_id)
        )'''

        sales_table = '''CREATE TABLE IF NOT EXISTS Sales (
            sales_id TEXT PRIMARY KEY,
            user_id TEXT,
            amount_tendered FLOAT,
            total FLOAT,
            amount_changed FLOAT,
            created_on DATETIME,
            FOREIGN KEY (user_id) REFERENCES User(user_id)
        )'''

        invoice_table = '''CREATE TABLE IF NOT EXISTS Invoice (
            invoice_id TEXT PRIMARY KEY,
            sales_id TEXT,
            product_id TEXT,
            user_id TEXT,
            product_name TEXT,
            price FLOAT,
            amount INT,
            total FLOAT,
            sold_on DATETIME,
            FOREIGN KEY (product_id) REFERENCES Product(product_id),
            FOREIGN KEY (user_id) REFERENCES User(user_id),
            FOREIGN KEY (sales_id) REFERENCES Sales(sales_id)
        )
        '''

        supply_table = '''CREATE TABLE IF NOT EXISTS Supply (
            supply_id TEXT PRIMARY KEY,
            user_id TEXT,
            item_name TEXT,
            quantity INT,
            unit TEXT,
            exp_date DATE,
            menu_type TEXT,
            flooring FLOAT,
            ceiling FLOAT,
            stock_level TEXT,
            FOREIGN KEY (user_id) REFERENCES User(user_id)
        )'''

        reorder_table = '''CREATE TABLE IF NOT EXISTS Reordered (
            ro_id TEXT PRIMARY KEY,
            item_id TEXT,
            item_name INT,
            amount_to_pay INT,
            quantity INT,
            arrival_date DATETIME,
            ordered_on DATETIME,
            Status TEXT,
            FOREIGN KEY (item_id) REFERENCES Items(item_id)
        )'''

        item_table = '''
        CREATE TABLE IF NOT EXISTS Items
        (
            item_id TEXT PRIMARY KEY,
            user_id TEXT,
            item_name TEXT,
            quantity FLOAT,
            unit TEXT,
            supplier TEXT,
            exp_date DATE,
            category TEXT,
            flooring FLOAT,
            ceiling FLOAT,
            stock_level TEXT,
            FOREIGN KEY (user_id) REFERENCES User(user_id)
        )'''

        supply_order_table = '''CREATE TABLE IF NOT EXISTS SupplyOrder (
            so_id TEXT PRIMARY KEY,
            supply_id TEXT,
            item_id TEXT,
            name TEXT,
            stock_level TEXT,
            FOREIGN KEY (supply_id) REFERENCES Supply(supply_id),
            FOREIGN KEY (item_id) REFERENCES Items(item_id)
        )'''
        with Database.get_db_connection() as conn:
            ic.ic('Database connection established')
            cursor = conn.cursor()
            ic.ic('Database cursor created')
            cursor.execute(user_table)
            cursor.execute(userActivity_table)
            cursor.execute(ingredient_table)
            cursor.execute(recipe_table)
            cursor.execute(product_table)
            cursor.execute(sales_table)
            cursor.execute(invoice_table)
            cursor.execute(supply_table)
            cursor.execute(reorder_table)
            cursor.execute(item_table)
            cursor.execute(supply_order_table)
            conn.commit()
            conn.close()

    @staticmethod
    def db_exist():
        db_path = 'SIMS.db'
        return os.path.exists(db_path)

Database.init_db_all()