from View import UserManualView
import os
class UserManualController:
    def __init__(self,managerController,master):
        self.mC = managerController
        self.master = master
        self.file_path = ("\\Group-6-User-Manual.pdf")
        self.view = UserManualView(self,self.master,self.file_path)

    def main(self):
        self.view.main()