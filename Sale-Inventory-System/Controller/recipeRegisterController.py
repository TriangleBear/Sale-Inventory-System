from View import RecipeRegisterView
from Model import RecipeRegisterModel
class RecipeRegisterController:
    def __init__(self,recipeRegisterView):
        self.recipeRegisterView = recipeRegisterView()
        self.view = RecipeRegisterView(self)

    def main(self):
        self.view.main()

    def register(self, data:list):
        recipereg_model = RecipeRegisterModel(data)
        return recipereg_model.create_recipe()