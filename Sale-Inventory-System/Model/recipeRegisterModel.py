from Utils import Database
class RecipeRegisterModel:
    def __init__(self,data:list):
        self.recipe_name = data[0]
        self.category = data[1]
        self.ingredients = data[2]
        self.details = data[3]

    def create_recipe(self, user_id):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """INSERT INTO Recipe (user_id, recipe_id, recipe_name, category, ingredients, details) 
                VALUES (%s, %s, %s, %s, %s, %s)"""
                # user_id should pass inside cursor.execute
                cursor.execute(sql, (user_id, self.get_recipe_id(), self.recipe_name, self.category, self.ingredients, self.details))
                connection.commit()
            connection.close()
        return 0

    def get_recipe_id(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """SELECT recipe_id FROM Recipe WHERE recipe_name = %s"""
                cursor.execute(sql, (self.recipe_name,))
                recipe_id = cursor.fetchone()
            connection.close()
        return recipe_id

    def create_recipe_ingredients(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """INSERT INTO Ingredients (recipe_id, indg_id) VALUES (%s, %s)"""
                cursor.execute(sql, (self.recipe_id, self.ingredient_id))
                connection.commit()