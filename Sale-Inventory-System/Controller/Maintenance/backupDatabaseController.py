from View import BackupDatabaseView
from Model import BackupDatabaseModel
class BackupDatabaseController:
    def __init__(self, managerController, master):
        self.master = master
        self.mC = managerController
        self.view = BackupDatabaseView(self,master)

    def main(self):
        self.view.main()

    def backupDatabase(self):
        backupModel = BackupDatabaseModel()
        backupModel.backupDatabase()

    def restoreDatabase(self):
        backupModel = BackupDatabaseModel()
        backupModel.restoreDatabase()