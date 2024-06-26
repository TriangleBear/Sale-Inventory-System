from View import ReportView
from Model import ReportModel
class ReportController():
    def __init__(self,managerController,master):
        self.master = master
        self.managerController = managerController
        self.view = ReportView(self,master)


    def fetch_data_from_user_activity(self):
        # code to fetch data from user_activity table
        pass