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
                    sql = """INSERT INTO Ingredients (recipe_id, indg_id, indg_name, quantity, unit) VALUES (%s, %s, %s, %s, %s)"""
                    cursor.execute(sql, 
                                   (self.recipe_id, ing_id, inner_list[0], inner_list[1], inner_list[2]))
                    connection.commit()
            connection.close()
        return