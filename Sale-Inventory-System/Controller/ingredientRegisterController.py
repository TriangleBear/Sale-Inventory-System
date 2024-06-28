from Model import IngredientRegisterModel
from View import IngredientRegisterView
from Utils import Functions

class IngredientRegisterController:
    def __init__(self, managerController,recipe_id=None):
        self.mC = managerController
        self.recipe_id = recipe_id
        self.view = IngredientRegisterView(self)

    def main(self):
        self.view.main()

    def checkInput(self, data: list):
        noItem = IngredientRegisterModel(data)
        return noItem.checkInput()

    def register(self, data: list):
        item = IngredientRegisterModel(data, self.user_id)
        item.registerItemData()

    def logUserActivity(self):
        Functions.logUserActivity([
            self.user_id, 
            "Ingredient Registered", 
            Functions.get_current_date("datetime")
            ]
        )
    