from View import ReportView
from Model import ReportModel
class ReportController():
    def __init__(self,master):
        self.master = master
        self.view = ReportView(self,self.master)

    def main(self):
        self.view.main()

    def managerController(self):
        from Controller import ManagerController
        manager_page = ManagerController(self.master)
        manager_page.main()
    
    def display_stock_level(self):
        model = ReportModel()
        model.display_items_stock_level()