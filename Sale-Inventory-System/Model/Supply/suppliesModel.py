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

    def fetch_supply_quantity(self, item_name):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT quantity FROM Supply WHERE item_name = %s"
                cursor.execute(query, (item_name,))
                data = cursor.fetchone()
            cursor.close()
        return data['quantity'] if data else None
    
    def update_item_quantity_in_database(self, item_name, new_quantity):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                query0 = "SELECT item_id FROM Items WHERE item_name = %s"
                cursor.execute(query0, (item_name,))
                item_id = cursor.fetchone()
                print('debug1')
                # Update the quantity of the specific item in the database
                query = "UPDATE Items SET quantity = %s WHERE item_id = %s"
                cursor.execute(query, (new_quantity, item_id['item_id']))
                print('debug2')
                query1 = "INSERT INTO Supply_Order (item_id, name) VALUES (%s, %s)"
                cursor.execute(query1, (item_id['item_id'], item_name))
                print('debug3')
                query_stock = "SELECT quantity, flooring, ceiling FROM Items WHERE item_id = %s"
                cursor.execute(query_stock, (item_id['item_id'],))
                data = cursor.fetchone()  # Use fetchone() to get a single row
                print(data)
                print('debug4')
                if data:  # Check if data is not None
                    quantity = data['quantity']
                    flooring = data['flooring']
                    ceiling = data['ceiling']  
                    print('Quantity, Flooring, Ceiling:', quantity, flooring, ceiling)

                    # Determine stock_level based on data
                    if quantity > flooring and quantity < ceiling:
                        stock_level = 'Average'
                    elif quantity <= flooring:
                        stock_level = 'Danger'
                    elif quantity >= ceiling:
                        stock_level = 'Maximum'
                    else:
                        stock_level = None  # Or some default value, if needed

                    # Update the database only if stock_level is determined
                    if stock_level is not None:
                        stock_level_query = "UPDATE Supply_Order SET stock_level = %s WHERE item_id = %s"
                        cursor.execute(stock_level_query, (stock_level, item_id['item_id']))

                        print('debug5')
                else:
                    print("No data found for supply_id:", item_id['item_id'])
                conn.commit()
                print('debug PASSED!')
            cursor.close()
        return True

    def update_supply_quantity_in_database(self, item_name, new_quantity):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                query0 = "SELECT supply_id FROM Supply WHERE item_name = %s"
                cursor.execute(query0, (item_name,))
                supply_id = cursor.fetchone()
                print('debug1')
                query = "UPDATE Supply SET quantity = %s WHERE supply_id = %s"
                cursor.execute(query, (new_quantity, supply_id['supply_id']))
                print('debug2')
                query1 = "INSERT INTO Supply_Order (supply_id, name) VALUES (%s, %s)"
                cursor.execute(query1, (supply_id['supply_id'], item_name))
                print('debug3')
                query_stock = "SELECT quantity, flooring, ceiling FROM Supply WHERE supply_id = %s"
                cursor.execute(query_stock, (supply_id['supply_id'],))
                data = cursor.fetchone()  # Use fetchone() to get a single row
                print('debug4')
                if data:  # Check if data is not None
                    quantity = data['quantity']
                    flooring = data['flooring']
                    ceiling = data['ceiling']
                    print('Quantity, Flooring, Ceiling:', quantity, flooring, ceiling)

                    # Determine stock_level based on data
                    if quantity > flooring and quantity < ceiling:
                        stock_level = 'Average'
                    elif quantity <= flooring:
                        stock_level = 'Danger'
                    elif quantity >= ceiling:
                        stock_level = 'Maximum'
                    else:
                        stock_level = None  # Or some default value, if needed

                    # Update the database only if stock_level is determined
                    if stock_level is not None:
                        stock_level_query = "UPDATE Supply SET stock_level = %s WHERE supply_id = %s"
                        cursor.execute(stock_level_query, (stock_level, supply_id['supply_id']))
                        print('debug5')
                else:
                    print("No data found for supply_id:", supply_id['supply_id'])
                conn.commit()
                print('debug PASSED!')
            cursor.close()
        return True

    def fetch_items_below_or_equal_flooring(self):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT item_id, item_name, quantity, stock_level FROM Items WHERE quantity <= flooring"
                cursor.execute(query)
                data = cursor.fetchall()
            cursor.close()
        return data

    def fetch_supply_below_or_equal_flooring(self):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT supply_id, item_name, quantity, stock_level FROM Supply WHERE quantity <= flooring"
                cursor.execute(query)
                data = cursor.fetchall()
            cursor.close()
        return data
    
    def get_item_type_by_id(self, item_id):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                # Check in the Items table first
                query_items = "SELECT 'Items' as type FROM Items WHERE item_id = %s"
                cursor.execute(query_items, (item_id,))
                data = cursor.fetchone()
                if data:
                    return data['type']

                # If not found in Items, check in the Supply table
                query_supply = "SELECT 'Supply' as type FROM Supply WHERE supply_id = %s"
                cursor.execute(query_supply, (item_id,))
                data = cursor.fetchone()
                if data:
                    return data['type']

        # If not found in either table, return None
        return None
    

    def calculate_stock_level_items(self):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT item_name, quantity FROM Items"
                cursor.execute(query)
                data = cursor.fetchall()
            cursor.close()
        return data


    

   