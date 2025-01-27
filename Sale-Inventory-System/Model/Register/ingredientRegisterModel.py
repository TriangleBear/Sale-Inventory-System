from Utils import Database, Functions
from icecream import ic
class IngredientRegisterModel():
    def __init__(self,data:list=None,user_id=None,current_recipe_id=None):
        self.user_id = user_id
        self.current_recipe_id = current_recipe_id
        if data is not None and len(data) > 1:
            self.recipe_id = data[0]
            self.data = data[1:]
            self.product_quantity = self.data[0]
        #self.data = [[ingredient_name, description, quantity, unit], [ingredient_name, description, quantity, unit], ...]
        #OR
        #self.data = [recipe_id, quantity]

    def delete_recipe_ingd(self,recipe_id):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            delete_sql = """DELETE FROM Ingredients WHERE recipe_id = %s"""
            cursor.execute(delete_sql,(recipe_id,))
            connection.commit() 
        connection.close()
        return

    def delete_removed_data(self):
        current_recipe_ingredients = Functions.convert_dicc_data(Functions.filter_ingredient_columns(self.fetch_current_data(self.recipe_id)))
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            for inner_list in current_recipe_ingredients:
                if inner_list not in self.data:
                    delete_sql = """DELETE FROM Ingredients WHERE recipe_id = %s AND ingd_name = %s"""
                    cursor.execute(delete_sql,(self.recipe_id,inner_list[0],))
                connection.commit() 
        connection.close()
        return

    def update_new_data(self):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            for inner_list in self.data:
                formattedInnerList = Functions.format_ingredient_data(inner_list) # convert data to proper format for checking                    
                ingd_id = """SELECT ingd_id FROM Ingredients WHERE recipe_id = %s AND ingd_name = %s"""
                cursor.execute(ingd_id,(self.recipe_id,formattedInnerList[0]))
                ingd_id = cursor.fetchone()
                if ingd_id:
                    ingd_id = ingd_id['ingd_id']
                    get_quantity = """SELECT quantity FROM Ingredients WHERE recipe_id = %s AND ingd_name = %s"""
                    cursor.execute(get_quantity,(self.recipe_id,formattedInnerList[0])) #formattedInnetList[0] = ingd_name
                    existing_quantity = float(cursor.fetchone()['quantity'])
                    new_quantity = Functions.check_stock_amount(existing=existing_quantity,input=formattedInnerList[2])
                    update_sql = """UPDATE Ingredients SET quantity = %s WHERE recipe_id = %s AND ingd_name = %s"""
                    cursor.execute(update_sql,(new_quantity,self.recipe_id,formattedInnerList[0]))
                else:
                    ingd_id = Functions.generate_unique_id("Ingredient")
                    insert_sql = """INSERT INTO Ingredients (recipe_id, ingd_id,user_id, ingd_name, description, quantity, unit) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                    cursor.execute(insert_sql, (self.recipe_id, ingd_id, self.user_id,formattedInnerList[0], formattedInnerList[1], formattedInnerList[2],formattedInnerList[3]))
                connection.commit() 
        connection.close()
        return


    def save_transaction(self):
        self.delete_removed_data()
        self.update_new_data()
    
    def fetch_current_data(self,recipe_id):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            sql = """SELECT * FROM Ingredients WHERE recipe_id = %s"""
            cursor.execute(sql, (recipe_id,))
            result = cursor.fetchall()
        connection.close()
        return result
    
    def get_total_quantity(self):
        ingredient_totals = {}
        with Database.get_db_connection() as connection:  # Assuming you have a method to get DB connection
            cursor = conn.cursor()
            # Query to retrieve ingredients for the given recipe_id
            cursor.execute("SELECT ingd_name, quantity FROM Ingredients WHERE recipe_id = %s", (self.recipe_id,))
            ingredients = cursor.fetchall()
            ingredients = Functions.convert_dicc_data(ingredients)
            
            for ingredient_name, quantity in ingredients:
                # Calculate total quantity required for the ingredient
                total_quantity = float(self.product_quantity) * float(quantity)
                ingredient_totals[ingredient_name] = total_quantity
        ic(ingredient_totals)
        return ingredient_totals
    
    def get_total_quantity_for_update(self,recipe_name,product_quantity):
        ingredient_totals = {}
        with Database.get_db_connection() as connection:  # Assuming you have a method to get DB connection
            cursor = conn.cursor()
            # Query to retrieve ingredients for the given recipe_id
            cursor.execute("SELECT ingd_name, quantity FROM Ingredients WHERE ingd_name = %s", (recipe_name,))
            ingredients = cursor.fetchall()
            ingredients = Functions.convert_dicc_data(ingredients)
            
            for ingredient_name, quantity in ingredients:
                # Calculate total quantity required for the ingredient
                total_quantity = float(self.product_quantity) * float(quantity)
                ingredient_totals[ingredient_name] = total_quantity
        ic(ingredient_totals)
        return ingredient_totals