from View import ProductRegisterView
from Utils import Functions
class ProductRegisterController:
    def __init__(self, managerController,id,name):
        self.id = id
        self.name = name
        self.mC = managerController
        self.user_id = self.mC.user_id
        self.view = ProductRegisterView(self,self.id,self.name)     

    def main(self):
        self.view.main()

    def register_product(self,data:list,id,name):
        from Model import ProductRegisterModel
        product_model = ProductRegisterModel(data, self.mC.user_id,id,name)
        return product_model.register_product()
    
    def check_existing_product(self, product_name):
        from Model import ProductRegisterModel
        product_model = ProductRegisterModel(product_name=product_name)
        return product_model.product_existence_check()
    
    def manager_view(self,master):
        Functions.destroy_page(master)
        self.mC.view.register_page()
    
    def subtract_item_stock_level(self, recipe_id, quantity):
        from Model import ItemRegisterModel, IngredientRegisterModel
        ingredient_model = IngredientRegisterModel([recipe_id,quantity])
        item_model = ItemRegisterModel()
        return item_model.subtract_item_stock(ingredient_model.get_total_quantity())
    
    def subtract_supply_stock_level(self, supply_id, quantity):
        from Model import ItemRegisterModel
        item_model = ItemRegisterModel()
        return item_model.subtract_stock(ingredient_model.get_total_quantity())
        
    def verify_product_inputs(self, data:list):
        print(f"prodcut inputs: {data}")
        from Model import ProductRegisterModel
        product_model = ProductRegisterModel(data)
        return product_model.checkInput()
    
    def get_product_id(self):
        from Model import ProductRegisterModel
        product = ProductRegisterModel()
        return product.set_product_id()
    
    def logUserActivity(self):
        Functions.logUserActivity(
            [self.user_id,
             "Product Registered",
             Functions.get_current_date("datetime")
            ])

    
    