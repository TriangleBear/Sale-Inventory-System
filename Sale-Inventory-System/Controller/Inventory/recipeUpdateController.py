from View import RecipeUpdateView
from Model import RecipeRegisterModel
from Utils import Functions
class RecipeUpdateController:
    def __init__(self, managerController,inventoryController,recipe_data:list=None):
        self.inventoryController = inventoryController
        self.mC = managerController
        self.user_id = self.mC.user_id
        if recipe_data is not None:
            self.recipe_id,self.recipe_name = recipe_data[0:2]
            self.view = RecipeUpdateView(self.mC,self,self.recipe_id,self.recipe_name)

    def main(self):
        self.view.main()

    def update_recipe(self,id,name):
        recipe_regModel = RecipeRegisterModel(current_recipe_id=id,recipe_name=name,user_id=self.mC.user_id)
        return recipe_regModel.update_recipe_name()
    
    def manager_view(self,master):
        Functions.destroy_page(master)
        self.mC.view.register_page()
    
    def delete_recipe(self,recipe_id):
        recipeModel = RecipeRegisterModel(current_recipe_id=recipe_id)
        return recipeModel.delete_recipe()

    def logUserActivity(self):
        Functions.logUserActivity(
            [self.user_id,
             "Recipe Updated",
             Functions.get_current_date("datetime")
            ])
