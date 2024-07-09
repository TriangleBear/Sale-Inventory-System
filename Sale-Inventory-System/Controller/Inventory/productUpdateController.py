from View import ProductUpdateView
from Utils import Functions
class ProductUpdateController:
    def __init__(self, managerController, current_product_data):
        self.mC = managerController
        self.current_product_data = current_product_data
        self.view = ProductUpdateView(self, self.current_product_data)
    
    def main(self):
        self.view.main()

    def checkInput(self,data:list,status:str) -> int: 
        from Model import ProductRegisterModel
        noItem = ProductRegisterModel(data,status)
        return noItem.checkInput()
    
    def update_product(self,data:list,status:str) -> None:
        from Model import ProductRegisterModel
        product = ProductRegisterModel(data,self.user_id,status)
        product.update_product()
    
    def logUserActivity(self):
        Functions.logUserActivity([self.user_id,
                                   "Product Updated",
                                   Functions.get_current_date("datetime")])