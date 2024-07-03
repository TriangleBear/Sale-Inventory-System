from Utils import Database
from Utils import Functions
class PosModel:
    def __init__(self, user_id=None, product_id=None, price=None, amount=None, total=None):
        self.sales_id = Functions.generate_unique_id('Sales')
        self.product_id = product_id
        self.user_id = user_id
        self.product_name = self.get_product_name_by_id(product_id)
        self.price = price
        self.amount = amount
        self.total = total
        self.sold_on = Functions.get_current_date('date')



    def get_product_name_by_id(self, product_id):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT product_name FROM Product WHERE product_id = %s"
                cursor.execute(query, (product_id,))
                data = cursor.fetchone()
            cursor.close()
        return data[0] if data else None

    def search_product(self, product_name):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                # Adjust the query to select only the product_id
                query = "SELECT product_id FROM Product WHERE product_name = %s"
                cursor.execute(query, (product_name,))
                data = cursor.fetchone()
            # No need to explicitly close the cursor when using 'with' statement
        # Return the product_id if a product was found, else return None
        return data['product_id'] if data else None

    def fetch_all_products(self):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT * FROM Product"
                cursor.execute(query)
                data = cursor.fetchall()
            cursor.close()
        return data
    
    def update_product_quantity_in_database(self, product_name, quantity):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "UPDATE Product SET quantity = %s WHERE product_name = %s"
                cursor.execute(query, (quantity, product_name))
                conn.commit()
            cursor.close()
        return True
    
    def save_transaction(self, cart_items):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                # Insert transaction record (adjust according to your schema)
                transaction_query = "INSERT INTO Transactions (date, total_amount) VALUES (NOW(), %s)"
                cursor.execute(transaction_query, (total_amount,))
                transaction_id = cursor.lastrowid
    
                # Insert each cart item as a transaction detail
                for product_name, quantity, total_price in cart_items:
                    # Find product_id based on product_name (adjust query as needed)
                    cursor.execute("SELECT product_id FROM Products WHERE product_name = %s", (product_name,))
                    product_id = cursor.fetchone()[0]
    
                    # Insert transaction detail (adjust according to your schema)
                    detail_query = "INSERT INTO TransactionDetails (transaction_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)"
                    cursor.execute(detail_query, (transaction_id, product_id, quantity, total_price))
    
                    # Update product quantity in inventory (adjust query as needed)
                    update_query = "UPDATE Products SET quantity = quantity - %s WHERE product_id = %s"
                    cursor.execute(update_query, (quantity, product_id))
    
                conn.commit()

        