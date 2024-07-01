from Utils import Database, Functions
class IngredientRegisterModel():
    def __init__(self,data:list=None):
        self.recipe_id = data[0]
        self.data = data[1:]
        self.product_quantity = self.data[0]
        #self.data = [[ingredient_name, quantity, unit], [ingredient_name, quantity, unit], ...]
        #OR
        #self.data = [recipe_id, quantity]


    def save_transaction(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                for inner_list in self.data:
                    formattedInnerList = Functions.format_ingredient_data(inner_list) # convert data to proper format for checking
                    indg_id = """SELECT indg_id FROM Ingredients WHERE recipe_id = %s AND indg_name = %s"""
                    cursor.execute(indg_id,(self.recipe_id,formattedInnerList[0]))
                    ing_id = cursor.fetchone()
                    if ing_id:
                        ing_id = ing_id['indg_id']
                        get_quantity = """SELECT quantity FROM Ingredients WHERE recipe_id = %s AND indg_name = %s"""
                        cursor.execute(get_quantity,(self.recipe_id,formattedInnerList[0]))
                        existing_quantity = float(cursor.fetchone()['quantity'])
                        new_quantity = existing_quantity + formattedInnerList[1]
                        update_sql = """UPDATE Ingredients SET quantity = %s WHERE recipe_id = %s AND indg_name = %s"""
                        cursor.execute(update_sql,(new_quantity,self.recipe_id,formattedInnerList[0]))
                    else:
                        ing_id = Functions.generate_unique_id("Ingredient")
                        insert_sql = """INSERT INTO Ingredients (recipe_id, indg_id, indg_name, quantity, unit) VALUES (%s, %s, %s, %s, %s)"""
                        cursor.execute(insert_sql, (self.recipe_id, ing_id, formattedInnerList[0], formattedInnerList[1], formattedInnerList[2]))
                    connection.commit()
            connection.close()
        return
    
    def get_total_quantity(self):
        ingredient_totals = {}
        with Database.get_db_connection() as connection:  # Assuming you have a method to get DB connection
            with connection.cursor() as cursor:
                # Query to retrieve ingredients for the given recipe_id
                cursor.execute("SELECT indg_name, quantity FROM Ingredients WHERE recipe_id = %s", (self.recipe_id,))
                ingredients = cursor.fetchall()
                ingredients = Functions.convert_dicc_data(ingredients)
                
                for ingredient_name, quantity in ingredients:
                    # Calculate total quantity required for the ingredient
                    total_quantity = float(self.product_quantity) * float(quantity)
                    ingredient_totals[ingredient_name] = total_quantity
        
        return ingredient_totals