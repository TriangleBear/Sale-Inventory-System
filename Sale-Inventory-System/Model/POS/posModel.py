from Utils import Database
from Utils import Functions
class PosModel:
    def __init__(self, cart_items:list=None,total_price:float=None,amount_tendered=None,user_id=None,datetime=None):
        self.sales_id = Functions.generate_unique_id('Sales')
        self.amount_tendered = amount_tendered
        self.sold_on = datetime
        self.user_id = user_id
        self.total_price = total_price
        self.cart_items = cart_items

    def get_product_name_by_id(self, product_id):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT product_id FROM Product WHERE product_name= %s"
                cursor.execute(query, (product_id,))
                data = cursor.fetchone()
            cursor.close()
        return data[0] if data else None

    def search_product(self, search_query):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                # Adjust the query to select only the product_id
                query = """SELECT * FROM Product 
                        WHERE product_name LIKE %s 
                        OR quantity LIKE %s 
                        OR category LIKE %s 
                        OR price LIKE %s 
                        OR exp_date LIKE %s"""
                cursor.execute(query, (search_query, search_query,search_query,search_query,search_query,))
                data = cursor.fetchall()
        return data if data else None

    def fetch_all_products(self):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT * FROM Product"
                cursor.execute(query)
                data = cursor.fetchall()
            cursor.close()
        return data

    def fetch_product_quantity(self, product_name):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                query = "SELECT quantity FROM Product WHERE product_name = %s"
                cursor.execute(query, (product_name,))
                data = cursor.fetchone()
            cursor.close()
        return data['quantity'] if data else None
    
    def update_product_quantity_in_database(self):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                for product_name, quantity, total_price in self.cart_items:
                    current_quantity = self.fetch_product_quantity(product_name)
                    new_quantity = int(current_quantity) - int(quantity)
                    query = "UPDATE Product SET quantity = %s WHERE product_name = %s"
                    cursor.execute(query, (new_quantity, product_name))
                    conn.commit()
            cursor.close()
        return True
    
    def fetch_product_id(self, product_name):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = "SELECT product_id FROM Product WHERE product_name = %s"
                cursor.execute(sql, (product_name,))
                data = cursor.fetchone()
            cursor.close()
        return data['product_id'] if data else None
    
    def fetch_product_unit_price(self,product_id):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = "SELECT price FROM Product WHERE product_id = %s"
                cursor.execute(sql, (product_id,))
                data = cursor.fetchone()
            cursor.close()
        return data['price'] if data else None

    def save_transaction(self,sales_id):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                for item in self.cart_items:
                    product_id = self.fetch_product_id(item[0])
                    invoice_id = Functions.generate_unique_id('Invoice')
                    price = self.fetch_product_unit_price(product_id)
                    # Insert transaction record (adjust according to your schema)
                    sql = """INSERT INTO Invoice (
                            invoice_id, 
                            sales_id,
                            product_id,
                            user_id, 
                            product_name,
                            price, 
                            amount, 
                            total,
                            sold_on
                        ) VALUES 
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    cursor.execute(sql, (
                        invoice_id,
                        sales_id,
                        product_id,
                        self.user_id,
                        item[0],
                        price,
                        item[1],
                        item[2],
                        self.sold_on,))
                connection.commit()
            connection.close()
        return

    def save_sales(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                changed = self.amount_tendered - self.total_price
                print(self.sold_on)
                sql = "INSERT INTO Sales (sales_id, user_id, amount_tendered, total, amount_changed, created_on) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (self.sales_id, self.user_id, self.amount_tendered, self.total_price, changed, self.sold_on ))
                connection.commit()
            connection.close()
        return [self.sales_id,self.sold_on]
        