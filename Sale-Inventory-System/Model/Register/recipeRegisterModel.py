from Utils import Database, Functions
class RecipeRegisterModel:
    def __init__(self,current_recipe_id=None,recipe_name=None,user_id=None):
        self.recipe_id = Functions.generate_unique_id("Recipe")
        self.recipe_name = recipe_name
        self.current_recipe_id = current_recipe_id
        self.user_id = user_id

    def delete_recipe(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                print(f"recipe deletion ID: {self.current_recipe_id}")
                delete_sql = """DELETE FROM Recipes WHERE recipe_id = %s"""
                cursor.execute(delete_sql, (self.current_recipe_id,))
                connection.commit() 
            connection.close()
        return

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
    
    def register_recipe_name(self):
        if self.recipe_name == '':
            return ValueError("Recipe Name cannot be empty")
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                # user_id should be inside the database for tracking
                sql = """INSERT INTO Recipes (recipe_id, recipe_name, user_id) VALUES (%s, %s, %s)"""
                cursor.execute(sql, (self.recipe_id, self.recipe_name, self.user_id))
                connection.commit()
            connection.close()
        return [self.recipe_id, self.recipe_name, self.user_id]
    
    def update_recipe_name(self):
        if self.recipe_name == '':
            return ValueError("Recipe Name cannot be empty")
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                # user_id should be inside the database for tracking
                sql = """UPDATE Recipes SET recipe_name = %s WHERE recipe_id = %s"""
                cursor.execute(sql, (self.recipe_name, self.current_recipe_id,))
                connection.commit()
            connection.close()
        return [self.current_recipe_id, self.recipe_name, self.user_id]

    def create_recipe_ingredients(self):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = """INSERT INTO Ingredients (recipe_id, indg_id) VALUES (%s, %s)"""
                cursor.execute(sql, (self.recipe_id, self.ingredient_id))
                connection.commit()