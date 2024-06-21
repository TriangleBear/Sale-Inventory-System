from View import ManagerDashboard
from Model import ManagerModel

class ManagerController:
    def __init__(self, parentFrame,user_id):
        self.frame = parentFrame
        self.id =user_id
        self.view = ManagerDashboard(self,self.frame)
    
    def main(self):
        self.view.main()