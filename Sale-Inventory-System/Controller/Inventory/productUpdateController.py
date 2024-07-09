from View import ProductUpdateView
from Utils import Functions
class ProductUpdateController:
    def __init__(self, maintenanceController, current_product_data):
        self.maintenanceController = maintenanceController
        self.current_product_data = current_product_data
        self.user_id = maintenanceController.user_id
        self.view = ProductUpdateView(self, self.current_product_data)
    
    def main(self):
        self.view.main()

    def verify_product_inputs(self, data:list):
        print(f"prodcut inputs: {data}")
        from Model import ProductRegisterModel
        product_model = ProductRegisterModel(data)
        return product_model.checkInput()
    
    def added_subtracted_new_quantity(self,recipe_name, new_quantity,current_quantity):
        return float(current_quantity) - float(new_quantity)
    
    def subtract_item_stock_level(self, recipe_name, quantity):
        from Model import ItemRegisterModel, IngredientRegisterModel
        ingredient_model = IngredientRegisterModel()
        item_model = ItemRegisterModel()
        return item_model.subtract_item_stock(ingredient_model.get_total_quantity_for_update(recipe_name,quantity))

    def update_product(self,data:list,id,name):
        from Model import ProductRegisterModel
        product_model = ProductRegisterModel(data=data,product_id=id,product_name=name)
        return product_model.register_product()
        

    # def checkInput(self,data:list,status:str) -> int: 
    #     from Model import ProductRegisterModel
    #     noItem = ProductRegisterModel(data,status)
    #     return noItem.checkInput()
    
    # def update_product(self,data:list,status:str) -> None:
    #     from Model import ProductRegisterModel
    #     product = ProductRegisterModel(data,self.user_id,status)
    #     product.update_product()
    
    def logUserActivity(self):
        Functions.logUserActivity([self.user_id,
                                   "Product Updated",
                                   Functions.get_current_date("datetime")])