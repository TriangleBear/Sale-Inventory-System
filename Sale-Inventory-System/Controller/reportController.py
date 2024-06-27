from View import ReportView
from Model import ReportModel
class ReportController():
    def __init__(self,master,managerController):
        self.master = master
        self.managerController = managerController
        self.search_entry = self.reportView.search_entry()
        self.view = ReportView(self, master)

    def main(self):
        self.view.main()

    def reportController(self):
        from Controller import ReportController
        report_page = ReportController(self.master)
        report_page.main()

    def fetch_data_from_user_activity(self):
        model = ReportModel(self.master, self.managerController)
        return model.fetch_data_from_user_activity()
    
    def search_data(self):
        model = ReportModel(self.master, self.managerController, self.search_entry.get())
        return model.search_data()
    
    def back_to_manager_view(self):
        self.view.destroy()
        self.managerController.main()