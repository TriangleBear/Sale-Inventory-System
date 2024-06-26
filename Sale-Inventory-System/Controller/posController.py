from View.posView import PosView
class PosController:
    def __init__(self,master,user_id):
        self.master = master
        super().__init__(self.master)
        self.user_id = user_id
        self.view = PosView(self.master,self.user_id)

    def main(self):
        self.view.main()

    def managerController(self):
        from Controller.managerController import ManagerController
        manager_page = ManagerController()
        manager_page.main()

    def posController(self):
        from Controller.posController import PosController
        pos_page = PosController()
        pos_page.main()


