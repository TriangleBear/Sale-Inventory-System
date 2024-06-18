from View import RegisterPage
from Model import register

class RegisterController:
    def __init__(self,parentFrame):
        self.parentFrame = parentFrame
        self.view = RegisterPage(self, self.parentFrame)
        self.model = 