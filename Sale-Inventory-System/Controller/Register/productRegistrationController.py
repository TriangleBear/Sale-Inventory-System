from View import ProductRegistrationView
class ProductRegistrationController:
    def __init__(self, managerController,recipe_id):
        self.recipe_id = recipe_id
        self.mC = managerController
        self.user_id = self.mC.user_id  # Extracting user_id from managerController
        self.view = ProductRegistrationView(self,recipe_id)

    def main(self):
        self.view.main()

    def register_Product(self):
        return self.productRegistrationController.register_product()
    
    def get_recipe_name_by_id(self, recipe_id):
        from Model import ProductRegistrationModel
        return ProductRegistrationModel.get_recipe_name_by_id(self,recipe_id)
    
    def get_recipe_id(self, recipe_name):
        from Model import ProductRegistrationModel
        return ProductRegistrationModel.get_recipe_id(self,recipe_name)

    
    