from Model import IngredientRegisterModel
from View import IngredientRegisterView
from Utils import Functions

class IngredientRegisterController:
    def __init__(self, managerController,recipeDetails:list=None):
        self.mC = managerController
        if recipeDetails is not None:
            #recipeDetails = [recipe_id,recipe_name, user_id]
            self.recipe_id = recipeDetails[0]
            self.recipe_name = recipeDetails[1]
            self.user_id = recipeDetails[2]
        self.view = IngredientRegisterView(self,[self.recipe_id,self.recipe_name])

    def main(self):
        self.view.main()

    def checkInput(self, data: list):
        noItem = IngredientRegisterModel(data)
        return noItem.checkInput()

    def logUserActivity(self):
        Functions.logUserActivity([
            self.user_id,
            f"{self.recipe_id}|Ingredient Registered", 
            Functions.get_current_date("datetime")
            ]
        )

    def save_transaction(self, data: list): 
        #data = [recipe_id, [ingredient_name, quantity, unit],... ]
        print(data)
        item = IngredientRegisterModel(data=data, user_id=self.user_id)
        item.save_transaction()

    