from View import RecipeRegisterView
from Model import RecipeRegisterModel
from Utils import Functions
class RecipeRegisterController:
    def __init__(self, managerController,master):
        self.master = master
        self.mC = managerController
        self.user_id = self.mC.user_id
        self.view = RecipeRegisterView(self,master)

    def main(self):
        self.view.main()

    def register_recipe(self,name):
        recipe_regModel = RecipeRegisterModel(recipe_name=name,user_id=self.mC.user_id)
        return recipe_regModel.register_recipe_name()
    
    def manager_view(self,master):
        Functions.destroy_page(master)
        self.mC.view.register_page()

    def logUserActivity(self):
        Functions.logUserActivity(
            [self.user_id,
             "Recipe Registered",
             Functions.get_current_date("datetime")
            ])
