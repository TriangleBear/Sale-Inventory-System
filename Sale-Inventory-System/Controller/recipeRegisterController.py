from View import RecipeRegisterView
from Model import RecipeRegisterModel
from Utils import Functions
class RecipeRegisterController:
    def __init__(self, managerController,master):
        self.master = master
        self.managerController = managerController
        self.view = RecipeRegisterView(self,self.master)

    def main(self):
        self.view.main()

    def register(self,name):
        recipereg_model = RecipeRegisterModel(name,self.managerController.user_id)
        return recipereg_model.create_recipe()
    
    def manager_view(self,master):
        Functions.destroy_page(master)
        self.managerController.view.register_page()