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
    
    def register(self, data:list):
        self.model.registerUser(data)
        return 0

    def checkInput(self,username, password)->str:
        value = self.model.getLevelOfAccess(username,password)
        return value

if __name__ == '__main__':
    controller = Controller()
    controller.main()