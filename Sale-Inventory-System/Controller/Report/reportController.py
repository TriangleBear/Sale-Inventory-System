from View import ReportView
from Model import ReportModel
class ReportController():
    def __init__(self,managerController,master):
        self.master = master
        self.mC = managerController
        self.view = ReportView(self,master)

    def main(self):
        self.view.main()

    def manager_view(self):
        self.mC.view.main()
    
    def display_stock_level(self):
        model = ReportModel()
        fig = model.display_items_stock_level()
        self.view.embed_graph(fig)

    def display_sales_report(self,date):
        print(f'Date controller: {date}')
        model = ReportModel()
        fig = model.display_sales_report(date)
        self.view.embed_graph(fig)