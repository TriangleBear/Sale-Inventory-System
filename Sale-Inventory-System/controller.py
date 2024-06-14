import sys
sys.path.append("..")
from Model.model import Model
from View.view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()
    
    def register(self):
        self.model.registerUser()
        return 0

    def checkInput(self,username, password)->str:
        value = self.model.levelOfAccess(username,password)
        return value

if __name__ == '__main__':
    controller = Controller()
    controller.main()