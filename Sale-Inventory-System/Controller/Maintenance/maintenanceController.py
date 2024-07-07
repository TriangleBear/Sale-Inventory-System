from View import MaintenanceView
from Model import MaintenanceModel
class MaintenanceController:
    def __init__(self,controller, master):
        self.master = master
        self.controller = controller
        self.view = MaintenanceView(self, master)

    def main(self):
        self.view.main()

    # def UpdateInventory(self):
    #     from Controller import InventoryController
    #     controller = InventoryController
    #     controller.maintenance_page(self)