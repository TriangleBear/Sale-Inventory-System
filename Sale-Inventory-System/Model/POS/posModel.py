from Utils import Database
class PosModel:
    #def __init__(self):
    def search_product(self, search):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT * FROM Product WHERE product_name LIKE %s"
                cursor.execute(query, (search))
                data = cursor.fetchone()
            cursor.close()
        return data

    def fetch_all_products(self):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT * FROM Product"
                cursor.execute(query)
                data = cursor.fetchall()
            cursor.close()
        return data

        