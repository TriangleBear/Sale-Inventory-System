from View import ProductRegistrationView
class ProductRegistrationController:
    def __init__(self, managerController):
        self.mC = managerController
        self.user_id = self.mC.user_id  # Extracting user_id from managerController
        self.view = ProductRegistrationView(self)

    def main(self):
        self.view.main()

    def register_Product(self):
        return self.productRegistrationController.register_product()

    
    