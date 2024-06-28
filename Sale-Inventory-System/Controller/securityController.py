from View import SecurityView
from Model import SecurityModel
from Utils import Functions
class SecurityController():
    def __init__(self,master,managerController):
        self.master = master
        self.mC = managerController
        self.view = SecurityView(self, master)

    def main(self):
        self.view.main()

    def fetch_data_from_user_activity(self):
        model = SecurityModel()
        return model.fetch_data_from_user_activity()
    
    def search_data(self,search_entry):
        model = SecurityModel(search_entry)
        return model.search_data()
    
    def manager_view(self):
        Functions.destroy_page(self.master)
        self.mC.view.body()
    

    
