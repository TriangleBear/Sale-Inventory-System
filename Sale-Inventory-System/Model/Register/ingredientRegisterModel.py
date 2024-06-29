from Utils import Database, Functions
class IngredientRegisterModel():
    def __init__(self,data:list):
        self.recipe_id = data[0]
        self.data = data[1:]


    def save_transaction(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                for inner_list in self.data:
                    ing_id = Functions.generate_unique_id("Ingredient")
                    print(f'inner_list | ingredientRegisterModel: {inner_list[0]}')
                    # Check if the ingredient already exists for the given recipe_id
                    check_sql = """SELECT quantity FROM Ingredients WHERE recipe_id = %s AND indg_name = %s"""
                    cursor.execute(check_sql, (self.recipe_id, inner_list[0]))
                    result = cursor.fetchone()
                    print(f"Debug - Result fetched: {result}")  # Debugging print statement
                    if result:
                        try:
                            # Directly attempt to convert to float, assuming result[0] is the correct format
                            existing_quantity = float(result[0])
                        except TypeError as e:
                            print(f"Error converting result to float: {e}, result: {result}")
                            continue  # Skip this iteration if there's a conversion error
                        additional_quantity = float(inner_list[1])  # Convert to float
                        new_quantity = existing_quantity + additional_quantity
                        update_sql = """UPDATE Ingredients SET quantity = %s WHERE recipe_id = %s AND indg_name = %s"""
                        cursor.execute(update_sql, (new_quantity, self.recipe_id, inner_list[0]))
                    else:
                        # Ingredient does not exist, insert new
                        new_quantity = float(inner_list[1])  # Convert to float to ensure consistency in data type
                        insert_sql = """INSERT INTO Ingredients (recipe_id, indg_id, indg_name, quantity, unit) VALUES (%s, %s, %s, %s, %s)"""
                        cursor.execute(insert_sql, 
                                        (self.recipe_id, ing_id, inner_list[0], new_quantity, inner_list[2]))
                    connection.commit()
            connection.close()
        return