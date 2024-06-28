from View import SuppliesView
class SuppliesController:
    def __init__(self,master,user_id):
        self.master = master
        self.user_id = user_id
        self.view = SuppliesView(self.master,self.user_id)

    def main(self):
        self.view.main()

    def managerController(self):
        from Controller import ManagerController
        manager_page = ManagerController()
        manager_page.main()

    def suppliesController(self):
        from Controller import SuppliesController
        supplies_page = SuppliesController()
        supplies_page.main()
    