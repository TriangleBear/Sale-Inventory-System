from Utils import Database
from Utils import Functions
class SuppliesModel:
    def __init__(self, cart_items:list=None,total_price:float=None,amount_tendered=None,user_id=None,datetime=None):
        self.sales_id = Functions.generate_unique_id('Sales')
        self.amount_tendered = amount_tendered
        self.sold_on = datetime
        self.user_id = user_id
        self.total_price = total_price
        self.cart_items = cart_items

    def fetch_items_quantity(self, item_name):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT quantity FROM Items WHERE item_name = %s"
                cursor.execute(query, (item_name,))
                data = cursor.fetchone()
            cursor.close()
        return data['quantity'] if data else None
    
    def update_item_quantity_in_database(self, item_name, new_quantity):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                # Fetch the current quantity of the specific item
                current_quantity = self.fetch_items_quantity(item_name)
                # Calculate the new quantity to be updated in the database
                updated_quantity = int(current_quantity) + int(new_quantity)
                # Update the quantity of the specific item in the database
                query = "UPDATE Items SET quantity = %s WHERE item_name = %s"
                cursor.execute(query, (updated_quantity, item_name))
                conn.commit()
            cursor.close()
        return True

    def update_supply_quantity_in_database(self, item_name, new_quantity):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                # Fetch the current quantity of the specific item
                current_quantity = self.fetch_items_quantity(item_name)
                # Calculate the new quantity to be updated in the database
                updated_quantity = int(current_quantity) + int(new_quantity)
                # Update the quantity of the specific item in the database
                query = "UPDATE Supply SET quantity = %s WHERE item_name = %s"
                cursor.execute(query, (updated_quantity, item_name))
                conn.commit()
            cursor.close()
        return True

    def fetch_items_below_or_equal_flooring(self):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT item_name, quantity FROM Items WHERE quantity <= flooring"
                cursor.execute(query)
                data = cursor.fetchall()
            cursor.close()
        return data

    def fetch_supply_below_or_equal_flooring(self):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT item_name, quantity FROM Supply WHERE quantity <= flooring"
                cursor.execute(query)
                data = cursor.fetchall()
            cursor.close()
        return data

   