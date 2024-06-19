from View import RegisterPage
from Model import RegisterModel

class RegisterController:
    def __init__(self,parentFrame):
        self.frame = parentFrame
        self.view = RegisterPage(self, self.frame)
        self.model = RegisterModel()

    def main(self):
        self.view.main()
    

    