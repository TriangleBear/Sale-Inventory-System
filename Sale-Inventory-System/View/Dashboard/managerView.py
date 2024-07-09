from tkinter import *
import tkinter as tk
from tkinter import font,messagebox, simpledialog
from Utils import Functions, CustomDialog, CustomComboboxDialog
class ManagerDashboard(tk.Frame):
    def __init__(self,mC,master,user_id):
        self.master = master
        self._main_window_attributes()
        super().__init__(self.master, background="GhostWhite")
        self.mC = mC
        self.user_id = user_id
        self.pack(fill=tk.BOTH,expand=True)

        #frames attributes
        self.mainBg = 'Grey90'

        #buttons
        self.main_btn_lbls = ["Security", "Registration","Inventory", "Supplies", "Point of Sale", "Report", "Maintenance","Help & About"]
        self.registration_btn_lbls = ["User Registration","Item Registration","Product Registration","Recipe Registration"]
        self.reorder_receive_btn_lbls = ["Reorder", "Receive Order"]
        self.item_register_btn_lbls = ["Supply Item", "Raw Item"]
        self.maintenance_btn_lbls = ["Edit Data", "Backup/Restore"]
        self.help_about_btn_lbls = ["User Manual","About Us"]
        self.btns = []
        self.item_btns = []
    
    def main(self):
        self._header_frame()
        self._body_frame()
        self.body()

    def body(self):
        self._center_frame()
        self._body_buttons()

    def register_page(self):
        self._center_frame()
        self._main_register_buttons() # load buttons
        self._back_button("register_page")

    def _item_register_page(self):
        self._center_frame()
        self._item_register_buttons()
        self._back_button("item_register_page")

    def supplies_page(self):
        self._center_frame()
        self._reorder_receive_buttons()
        self._back_button("supplies_page")

    def maintenance_page(self):
        self._center_frame()
        self._maintenance_buttons()
        self._back_button("maintenance_page")

    def _help_and_about(self):
        self._center_frame()
        self._help_and_about_buttons()
        self._back_button("maintenance_page")

    def _main_window_attributes(self):
        # main window
        self.h = 720
        self.w = 900
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        self.master.title('S.I.M.S')
        self.master.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.master.resizable(False, False)

    def _header_frame(self):
        self.headerFrame = tk.Frame(self,background=self.mainBg)
        self.headerFrame.place(x=0,y=0, width=900,height=45)

        self._user_label()
        self._home_button()
        self._logout_button()

    def _user_label(self):
        user_label = tk.Label(self.headerFrame,font=font.Font(family='Courier New',size=14,weight='bold'),
                              text=f"manager dashboard | user ID: {self.user_id}",background=self.mainBg)
        user_label.place(x=9,y=9)

    def _home_button(self):
        home_btn = tk.Button(self.headerFrame,font=font.Font(family='Courier New',size=9,weight='bold'),
                               text="Home", command=lambda:self._check_back_command("home page"))
        home_btn.place(relx=0.88,rely=0.5,anchor='e')

    def _logout_button(self):
        logout_btn = tk.Button(self.headerFrame,font=font.Font(family='Courier New',size=9,weight='bold'),
                               text="Logout", command=lambda:self._check_back_command("logout"))
        logout_btn.place(relx=0.95,rely=0.5,anchor='e')

    def _body_frame(self):
        self.bodyFrame = tk.Frame(self, background=self.mainBg)
        self.bodyFrame.place(x=30,y=75,width=(self.w-60),height=self.h-120)

    def _center_frame(self):
        self.btn_frame = tk.Frame(self.bodyFrame,background=self.mainBg)
        self.btn_frame.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _body_buttons(self):
        Functions.create_buttons_using_grid(self.btn_frame,
                                            labels=self.main_btn_lbls,
                                            entryList=self.btns,
                                            max_columns=2,
                                            w=16,
                                            h=1,
                                            fontSize=13,
                                            gridxPadding=15,
                                            gridyPadding=10,
                                            btnyPadding=2,
                                            btnxPadding=10,
                                            cmd=self._check_buttons_command)

    def _main_register_buttons(self):
        Functions.create_buttons_using_grid(self.btn_frame,
                                            labels=self.registration_btn_lbls,
                                            entryList=self.btns,
                                            max_columns=2,
                                            w=21,
                                            h=1,
                                            fontSize=12,
                                            gridxPadding=10,
                                            gridyPadding=10,
                                            btnyPadding=2,
                                            btnxPadding=5,
                                            cmd=self._check_buttons_command)
        
    def _item_register_buttons(self):
        Functions.create_buttons_using_grid(self.btn_frame,
                                            labels=self.item_register_btn_lbls,
                                            entryList=self.item_btns,
                                            max_columns=2,
                                            w=21,
                                            fontSize=12,
                                            gridxPadding=10,
                                            gridyPadding=10,
                                            btnyPadding=2,
                                            btnxPadding=5,
                                            cmd=self._check_buttons_command)
        
    def _reorder_receive_buttons(self):
        Functions.create_buttons_using_grid(self.btn_frame,
                                            labels=self.reorder_receive_btn_lbls,
                                            entryList=self.btns,
                                            max_columns=2,
                                            w=21,
                                            h=1,
                                            fontSize=12,
                                            gridxPadding=10,
                                            gridyPadding=10,
                                            btnyPadding=2,
                                            btnxPadding=5,
                                            cmd=self._check_buttons_command)

    def _maintenance_buttons(self):
        Functions.create_buttons_using_grid(self.btn_frame,
                                            labels=self.maintenance_btn_lbls,
                                            entryList=self.btns,
                                            max_columns=2,
                                            w=21,
                                            h=1,
                                            fontSize=12,
                                            gridxPadding=10,
                                            gridyPadding=10,
                                            btnyPadding=2,
                                            btnxPadding=5,
                                            cmd=self._check_buttons_command)

    def _help_and_about_buttons(self):
        Functions.create_buttons_using_grid(self.btn_frame,
                                            labels=self.help_about_btn_lbls,
                                            entryList=self.btns,
                                            max_columns=2,
                                            w=21,
                                            h=1,
                                            fontSize=12,
                                            gridxPadding=10,
                                            gridyPadding=10,
                                            btnyPadding=2,
                                            btnxPadding=5,
                                            cmd=self._check_buttons_command)

    def _back_button(self,state:str):
        self.back_btn = tk.Button(self.bodyFrame,font=font.Font(family='Courier New',size=9,weight='bold'), 
                                  text="Back", background="Grey89",command=lambda:self._check_back_command(f"{state}"))
        self.back_btn.place(relx=0.5,rely=0.9,anchor='s')

    def _check_back_command(self,button:str):
        if button == "logout":
            if messagebox.askyesno('Confirm Logout','Proceed with logout?'):
                self.mC.mainController()
        if button == "home page":
            Functions.destroy_page(self.bodyFrame)
            self.body()
        if button == "register_page":
            Functions.destroy_page(self.bodyFrame)
            self.body()
        if button == "item_register_page":
            Functions.destroy_page(self.bodyFrame)
            self.register_page()
        if button == "supplies_page":
            Functions.destroy_page(self.bodyFrame)
            self.body()
        if button == "maintenance_page":
            Functions.destroy_page(self.bodyFrame)
            self.body()
        if button == "Manual":
            Functions.destroy_page(self.bodyFrame)
            self._help_and_about()

    def _check_buttons_command(self,button:str):
        if button == "Security": 
            self.mC.securityController(self.bodyFrame)
        if button == "Registration":
            Functions.destroy_page(self.bodyFrame)
            self.register_page()
        if button == "User Registration":
            self.mC.userRegisterController()
        if button == "Item Registration":
            Functions.destroy_page(self.bodyFrame)
            self._item_register_page()
        if button == "Recipe Registration":
            self.mC.recipeRegisterController(self.bodyFrame)
        if button == "Product Registration":
            self.show_hm_or_pm()
        if button == "Supply Item":
            self.mC.itemRegisterController("Supply Item")
        if button == "Raw Item":
            self.mC.itemRegisterController("Raw Item")
        if button == "Inventory":
            self.mC.inventoryController(self.bodyFrame)
        if button == "Report":
            self.mC.reportController(self.bodyFrame)
        if button == "Supplies":
            Functions.destroy_page(self.bodyFrame)
            self.supplies_page()
        if button == "Reorder":
            self.mC.suppliesController(self.bodyFrame)
        if button == "Receive Order":
            self.mC.receiveSuppliesController(self.bodyFrame)
        if button == "Point of Sale":
            self.mC.posController(self.bodyFrame)
        if button == "Maintenance":
            Functions.destroy_page(self.bodyFrame)
            self.maintenance_page()
        if button == "Edit Data":
            self.mC.maintenanceController(self.bodyFrame)
        if button == "Backup/Restore":
            self.mC.backupDatabaseController(self.bodyFrame)
        if button == "Help & About":
            Functions.destroy_page(self.bodyFrame)
            self._help_and_about()
        if button == "User Manual":
            Functions.destroy_page(self.bodyFrame)
            self.mC.userManualController(self.bodyFrame)

    def show_hm_or_pm(self):
        user_choice = CustomDialog(self.master, title="Home Made or Pre Made", buttons=["Home Made", "Pre Made"]).result
        if user_choice == "Home Made":
            rid_rname = Functions.convert_dicc_data(self.mC.get_rid_rname())
            formatted_values = [f"{rid} | {rname}" for rid, rname in rid_rname]
            CustomComboboxDialog(values=formatted_values, title="Recipe ID | Recipe Name", prompt="Choose Recipe Name",controller=self.mC,state=user_choice).main()
            return
        if user_choice == "Pre Made":
            sid_sname = Functions.convert_dicc_data(self.mC.get_sid_sname())
            formatted_values = [f"{sid} | {sname}" for sid,sname in sid_sname]
            CustomComboboxDialog(values=formatted_values, title="Recipe ID | Recipe Name", prompt="Choose Recipe Name",controller=self.mC,state=user_choice).main()
            

            