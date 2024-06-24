from View import RegisterView
from Model import RegisterModel

class RegisterController():
    def __init__(self,master):
        self.master = master
        self.view = RegisterView(self, self.master)
        self.model = RegisterModel()

    def main(self):
        self.view.main()
    

    