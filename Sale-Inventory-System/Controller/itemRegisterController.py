from View import ItemRegisterView
from Model import ItemRegisterModel
from Utils import Functions
class ItemRegisterController:
    def __init__(self,master,managerController):
        self.master = master
        self.managerController = managerController
        self.view = ItemRegisterView(self)

    def main(self):
        self.view.main()

    def manager_body(self,master):
        Functions.destroy_page(master)
        self.managerController.view.register_page()