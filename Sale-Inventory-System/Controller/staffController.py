from View import StaffDashboard
from Model import ManagerModel

class ManagerController:
    def __init__(self, master,user_id):
        self.master = master
        self.id =user_id
        self.view = StaffDashboard(self,self.master,self.id)
    
    def main(self):
        self.view.main()