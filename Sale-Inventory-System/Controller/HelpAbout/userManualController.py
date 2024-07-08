from View import UserManualView
class UserManualController:
    def __init__(self,managerController,master):
        self.mC = managerController
        self.master = master
        self.file_path = r"Sale-Inventory-System\Controller\HelpAbout\User-manual-pero-di-pa-tapos-pero-pwede-na-muna.pdf"
        self.view = UserManualView(self,self.master,self.file_path)

    def main(self):
        self.view.main()