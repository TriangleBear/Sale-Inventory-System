from View import ProductRegisterView
from Utils import Functions
class ProductRegisterController:
    def __init__(self, managerController,recipe_id):
        self.recipe_id = recipe_id
        self.mC = managerController
        self.user_id = self.mC.user_id
        self.view = ProductRegisterView(self,recipe_id)     

    def main(self):
        self.view.main()

    def register_product(self,data:list):
        from Model import ProductRegisterModel
        product_model = ProductRegisterModel(data, self.user_id)
        return product_model.register_product()
    
    def manager_view(self,master):
        Functions.destroy_page(master)
        self.mC.view.register_page()
    
    def get_recipe_name_by_id(self, recipe_id):
        from Model import ProductRegisterModel
        return ProductRegisterModel.get_recipe_name_by_id(recipe_id)
    
    def get_recipe_id(self, recipe_name):
        from Model import ProductRegisterModel
        return ProductRegisterModel.get_recipe_id(self,recipe_name)
    
    def logUserActivity(self):
        Functions.logUserActivity(
            [self.user_id,
             "Product Registered",
             Functions.get_current_date("datetime")
            ])

    
    