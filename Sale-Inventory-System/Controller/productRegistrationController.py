class ProductRegistrationController:
    def __init__(self,ProductRegistrationService):
        self.productRegistrationService = ProductRegistrationService()

    def registerProduct(self, product):
        return self.productRegistrationService.registerProduct(product)

    def updateProduct(self, product):
        return self.productRegistrationService.updateProduct(product)

    def deleteProduct(self, product):
        return self.productRegistrationService.deleteProduct(product)

    def getAllProducts(self):
        return self.productRegistrationService.getAllProducts()

    def getProduct(self, product):
        return self.productRegistrationService.getProduct(product)