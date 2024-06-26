from View import ReportView
from Model import ReportModel
class ReportController():
    def __init__(self,master,managerController):
        self.master = master
        self.managerController = managerController
        self.view = ReportView(self, master)

    def main(self):
        self.view.main()

    def reportController(self):
        from Controller import ReportController
        report_page = ReportController(self.master)
        report_page.main()

    def fetch_data_from_user_activity(self):
        # code to fetch data from user_activity table
        pass