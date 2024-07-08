import tkinter as tk
from tkinter import CENTER, font, ttk, messagebox
from Utils import Functions
from Utils import CustomDialog
class MaintenanceView(tk.Frame):
    def __init__(self, maintenanceController, master):
        self.master = master
        self.mainBg = "Gray89"
        self.navBarBg = "Gray84"
        super().__init__(self.master, background=self.mainBg)
        self.maintenanceController = maintenanceController
        self.menu = ["Items","Supplies","Products","Recipes","User"]
        self.pack(fill=tk.BOTH, expand=True)

    def main(self):
        self._nav_bar_frame()
        self._display_table()
        self._back_button()
        self._refresh_button()
        self._update_button()
        
    def _nav_bar_frame(self):
        w = self.master.winfo_width()
        h = 50
        self.navBarFrame = tk.Frame(self, background="Grey84")
        self.navBarFrame.place(relx=0, rely=0, width=w, height=h)
        self._nav_bar_label()
        self._tree_dropdown()
        self._search_button()
        self._search_entry()

    def _nav_bar_label(self):
        self.navBarLabel =tk.Label(self.navBarFrame,font=font.Font(family='Courier New',size=14,weight='bold'),text=f"{self.menu[0]} Maintenance",background=self.navBarBg)
        self.navBarLabel.place(relx=0.14,rely=0.5,anchor=CENTER)

    def _tree_dropdown(self):
        self.selectTable = ttk.Combobox(self.navBarFrame,values=self.menu)
        self.selectTable.place(relx=0.355,rely=0.5,anchor=CENTER)
        self.selectTable.set(self.menu[0])
        self.selectTable.bind('<<ComboboxSelected>>', lambda event: self._change_column_labels(self.tree,self.selectTable.get(),self.selectTable.get()[0]))

    def _insert_table_columns(self,labels):
        for col in self.table:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor='center')

    def _display_table(self):
        self.tree = ttk.Treeview(
            self,
            show="headings",
            selectmode="browse",
            style="Custom.Treeview"
        )
        Functions.change_column(self.tree,self.maintenanceController.get_items_column_names())
        self.tree.bind('<Configure>', Functions.adjust_column_widths)
        self.tree.place(relx=0.49999,rely=0.5,anchor='center',width=839.9,height=355)
        self._insert_data(self.maintenanceController.get_items_on_database())

    def _insert_data(self,data):
        self.tree.delete(*self.tree.get_children())
        converted_data = Functions.convert_dicc_data(data)
        for item in converted_data:
            self.tree.insert("","end",values=item)

    def _change_column_labels(self,tree:ttk.Treeview, table_name:str, data=None):
        if table_name == "Items":
            self.navBarLabel.config(text=f"{table_name}")
            Functions.change_column(tree,self.maintenanceController.get_items_column_names())
            self._insert_data(self.maintenanceController.search_data(table_name,data))
        if table_name == "Products":
            self.navBarLabel.config(text=f"{table_name}")
            product_labels = self.maintenanceController.get_product_column_names()
            Functions.change_column(tree,product_labels)
            self._insert_data(self.maintenanceController.search_data(table_name,data))
        if table_name == "Supplies":
            self.navBarLabel.config(text=f"{table_name}")
            Functions.change_column(tree,self.maintenanceController.get_supply_column_names())
            self._insert_data(self.maintenanceController.search_data(table_name,data))
        if table_name == "Recipes":
            self.navBarLabel.config(text=f"{table_name}")
            Functions.change_column(tree,self.maintenanceController.get_recipe_column_names())
            self._insert_data(self.maintenanceController.search_data(table_name,data))
        if table_name == "User":
            self.navBarLabel.config(text=f"{table_name}")   
            Functions.change_column(tree,self.maintenanceController.get_users_column_names())
            self._insert_data(self.maintenanceController.search_data(table_name,data))
        return
    
    def _search_entry(self):
        self.searchEntry = tk.Entry(self.navBarFrame, borderwidth=0, width=23,font=font.Font(size=12))
        self.searchEntry.place(relx=0.9,rely=0.5,anchor='e')

    def _search_button(self):
        self.searchButton = tk.Button(self.navBarFrame, text="Search",font=font.Font(size=12),background=self.navBarBg,command=lambda: self._change_column_labels(self.tree,self.selectTable.get(),self.searchEntry.get()))
        self.searchButton.place(relx=0.64,rely=0.5,anchor='e')

    def _update_item_data(self):
        self.maintenanceController.itemUpdate(list(self.tree.item(self.tree.selection()[0],'values')))
        self._change_column_labels(self.tree,self.selectTable.get(),self.selectedTable.get()[0])

    def _update_supply_data(self) -> None:
        self.maintenanceController.supplyUpdate(list(self.tree.item(self.tree.selection()[0],'values')))
        self._change_column_labels(self.tree,self.selectTable.get(),self.selectTable.get()[0])

    def _update_row_data(self,table_name):
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("No selection", "Please select a row to update.")
            return
        if table_name == "Items":
            print(list(self.tree.item(self.tree.selection()[0],'values')))
            self._update_item_data()
        if table_name == "Supplies":
            print(self.tree.item(self.tree.selection()[0],'values'))
            self._update_supply_data()
        if table_name == "Products":
            print(self.tree.item(self.tree.selection()[0],'values'))
        if table_name == "Recipes":
            print(list(self.tree.item(self.tree.selection()[0],'values')))
            self._update_reg_ingd()
            self._change_column_labels(self.tree,self.selectTable.get(),self.selectTable.get()[0])
        if table_name == "User":
            print(self.tree.item(self.tree.selection()[0],'values'))
            self._update_user_data()
            self._change_column_labels(self.tree,self.selectTable.get(),self.selectTable.get()[0])

    def _delete_or_update_recipe_name(self):
        user_choice = CustomDialog(self.master,title="Recipe or Ingredient",buttons=["Update Name", "Delete Recipe"]).result
        if user_choice == "Update Name":
            self.maintenanceController.recipeUpdate(list(self.tree.item(self.tree.selection()[0],'values')))
        if user_choice == "Delete Recipe":
            self.maintenanceController.recipeIngredientDelete(list(self.tree.item(self.tree.selection()[0],'values')))
            messagebox.showinfo('Deletion', 'Deletion Successful! Please Refresh')
            return

    def _update_product_data(self):
        user_choice = CustomDialog(self.master,title="Product or Supply",buttons=["Update Product", "Delete Product"]).result
        if user_choice == "Update Product":
            self.maintenanceController.productUpdate(list(self.tree.item(self.tree.selection()[0],'values')))
        if user_choice == "Delete Product":
            self.maintenanceController.productDelete(list(self.tree.item(self.tree.selection()[0],'values')))
            messagebox.showinfo('Deletion', 'Deletion Successful! Please Refresh')
            return

    def _update_user_data(self):
        user_choice = CustomDialog(self.master,title="User",buttons=["Update User", "Delete User"]).result
        if user_choice == "Update User":
            self.maintenanceController.userUpdate(list(self.tree.item(self.tree.selection()[0],'values')))
            messagebox.showinfo('Update', 'Update Successful! Please Refresh')
        if user_choice == "Delete User":
            self.maintenanceController.userDelete(list(self.tree.item(self.tree.selection()[0],'values')))
            messagebox.showinfo('Deletion', 'Deletion Successful! Please Refresh')
            return
        
    def userUpdate(self):
        self.maintenanceController.userUpdate(list(self.tree.item(self.tree.selection()[0],'values')))
        self._change_column_labels(self.tree,self.selectTable.get(),self.selectTable.get()[0])
        

    def _update_reg_ingd(self):
        user_choice = CustomDialog(self.master,title="Recipe or Ingredient",buttons=["Recipe Name", "Recipe Ingredients"]).result
        if user_choice == "Recipe Name":
            self._delete_or_update_recipe_name()
        if user_choice == "Recipe Ingredients":
            self.maintenanceController.recipeIngredientUpdate(list(self.tree.item(self.tree.selection()[0],'values')))

    def _refresh_button(self):
        refresh_button = tk.Button(self, font=font.Font(family='Courier New',size=9,weight='bold'),text="Refresh", 
                                   command=lambda:self._change_column_labels(self.tree,self.selectTable.get(),self.selectTable.get()[0]))
        refresh_button.place(relx=0.8,rely=0.9,anchor='se')


    def _update_button(self):
        update_button = tk.Button(self, font=font.Font(family='Courier New',size=9,weight='bold'),text="Update", 
                                   command=lambda:self._update_row_data(self.selectTable.get()))
        update_button.place(relx=0.9,rely=0.9,anchor='se')

    def _back_button(self):
        back_button = tk.Button(self, font=font.Font(family='Courier New',size=9,weight='bold'),text="Back", 
                                command=lambda:self.maintenanceController.manager_view())
        back_button.place(relx=0.09,rely=0.9,anchor='sw')
