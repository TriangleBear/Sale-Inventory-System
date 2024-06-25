from View import ManagerDashboard
from Model import ManagerModel
from Utils import Functions

class ManagerController:
    def __init__(self, master,user_id):
        self.master = master
        self.id =user_id
        self.view = ManagerDashboard(self,self.master,self.id)
    
    def main(self):
        self.view.main()
    
    def managerPage(self,master,user_id):
        Functions.destroy_page(master)
        from Controller import ManagerController
        manager_dashboard = ManagerController(master,user_id)
        manager_dashboard.main()