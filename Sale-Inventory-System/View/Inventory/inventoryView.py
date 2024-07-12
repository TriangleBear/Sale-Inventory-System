from tkinter import *
import tkinter as tk
from tkinter import ttk
from Utils import Functions,  CustomDialog
from tkinter import font, messagebox
from tkcalendar import DateEntry
from icecream import ic
class InventoryView(tk.Frame):
    def __init__(self,inventoryController,master):
        self.inventoryController = inventoryController
        self.master = master
        self.mainBg = "Gray89"
        self.navBarBg = "Gray84"
        super().__init__(self.master, background=self.mainBg)

        self.inventory_labels_with_colspan = {
            "Product ID":1,
            "Product Name":1,
            "Quantity":1,
            "Supplier":1,
            "Expirartion Date":1,
            "Menu":1,
            "Cost":1,
            "Category":1
        }
        self.inventory_entry_boxes = []
        self.inventory_inputs = []
        self.menus = ["Items","Supplies","Products","Recipes"]
        self.pack(fill=tk.BOTH,expand=True)

    def main(self):
        self._nav_bar_frame()
        self._display_table()
        self._back_button()
        self._refresh_button()
        # self._update_button()

    def _nav_bar_frame(self):
        w = self.master.winfo_width()
        h = 50
        self.navBarFrame = tk.Frame(self,background=self.navBarBg)
        self.navBarFrame.place(relx=0,rely=0,width=w,height=h)
        self._nav_bar_label()
        self._tree_dropdown()
        self._search_button()
        self._search_entry()

    def _tree_dropdown(self):
        Functions.treeview_style(self.mainBg)
        self.selectTable = ttk.Combobox(self.navBarFrame,values=self.menus)
        self.selectTable.place(relx=0.355,rely=0.5,anchor=CENTER)
        self.selectTable.set(self.menus[0])
        self.selectTable.bind('<<ComboboxSelected>>', lambda event: self._change_column_labels(self.tree,self.selectTable.get(),self.selectTable.get()[0]))
        #self._update_table(self.selectTable.get())

    def _insert_table_columns(self,labels):
        for col in self.table:
            self.tree.heading(col, text=col)    
            self.tree.column(col, anchor='center')
    

    def _display_table(self):
        # Functions.treeview_style(self.mainBg)
        self.tree = ttk.Treeview(
            self,
            show='headings',
            selectmode='browse',
            style="Custom.Treeview"
        )
        Functions.change_column(self.tree,self.inventoryController.get_items_column_names())
        self.tree.bind('<Configure>',Functions.adjust_column_widths)
        self.tree.place(relx=0.49999,rely=0.5,anchor='center',width=839.9,height=355)
        self._insert_data(self.inventoryController.get_items_on_database())

    def _insert_data(self,data):
        self.tree.delete(*self.tree.get_children())
        converted_data = Functions.convert_dicc_data(data)
        for item in converted_data:
            self.tree.insert('', 'end', values=item)

    def _destroy_recipe_view_ingd(self):
        if hasattr(self, 'recipe_view_ingd') and self.recipe_view_ingd is not None:
            self.recipe_view_ingd.destroy()
            self.recipe_view_ingd = None

    def _change_column_labels(self, tree: ttk.Treeview, table_name: str, data=None):
        # Always destroy the button at the start
        self._destroy_recipe_view_ingd()
        
        self.navBarLabel.config(text=f"{table_name} Inventory")
        
        if table_name == "Items":
            Functions.change_column(tree, self.inventoryController.get_items_column_names())
        elif table_name == "Products":
            product_labels = self.inventoryController.get_product_column_names()
            Functions.change_column(tree, product_labels)
        elif table_name == "Supplies":
            Functions.change_column(tree, self.inventoryController.get_supply_column_names())
        elif table_name == "Recipes":
            Functions.change_column(tree, self.inventoryController.get_recipe_column_names())
            self._create_recipe_view_ingd()
        
        self._insert_data(self.inventoryController.search_data(table_name, data))
        return

    def _create_recipe_view_ingd(self):
        self.recipe_view_ingd = tk.Button(
            self,
            font=font.Font(family='Courier New', size=9, weight='bold'),
            text="View Ingredients",
            background=self.mainBg,
            command=lambda: self._view_recipe_ingredients()
        )
        self.recipe_view_ingd.place(relx=0.9, rely=0.9, anchor='se')

    def _nav_bar_label(self):
        self.navBarLabel =tk.Label(self.navBarFrame,font=font.Font(family='Courier New',size=14,weight='bold'),text=f"{self.menus[0]} Inventory",background=self.navBarBg)
        self.navBarLabel.place(relx=0.14,rely=0.5,anchor=CENTER)

    def _search_entry(self):
        self.search_entry = tk.Entry(self.navBarFrame, borderwidth=0, width=23,font=font.Font(size=12))
        self.search_entry.place(relx=0.9, rely=0.5,anchor='e')  # Place the entry at the top with some paddin

    def _search_button(self):
        search_button = tk.Button(self.navBarFrame, font=font.Font(family='Courier New', size=9, weight='bold'), text="Search",
                                    command=lambda: self._change_column_labels(self.tree,self.selectTable.get(),self.search_entry.get()), padx=7, pady=2)
        search_button.place(relx=0.64,rely=0.5, anchor='e')  # Place the button at the bottom with some padding
            
    def _back_button(self):
        self.back_btn = tk.Button(self,font=font.Font(family='Courier New',size=9,weight='bold'), 
                                  text="Back", background="Grey89",command=lambda:self.inventoryController.manager_view())
        self.back_btn.place(relx=0.09,rely=0.9,anchor='s')

    def _refresh_button(self):
        refresh_button = tk.Button(self, font=font.Font(family='Courier New',size=9,weight='bold'),text="Refresh", 
                                   command=lambda:self._change_column_labels(self.tree,self.selectTable.get(),self.selectTable.get()[0]))
        refresh_button.place(relx=0.9,rely=0.9,anchor='se')

    def _update_item_data(self):
        self.inventoryController.itemUpdate(list(self.tree.item(self.tree.selection()[0],'values')))
        self._change_column_labels(self.tree,self.selectTable.get(),self.selectTable.get()[0])

    def _update_supply_data(self) -> None:
        self.inventoryController.supplyUpdate(list(self.tree.item(self.tree.selection()[0],'values')))
        self._change_column_labels(self.tree,self.selectTable.get(),self.selectTable.get()[0])

    def _update_row_data(self,table_name):
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

    def _delete_or_update_recipe_name(self):
        user_choice = CustomDialog(self.master,title="Recipe or Ingredient",buttons=["Update Name", "Delete Recipe"]).result
        if user_choice == "Update Name":
            self.inventoryController.recipeUpdate(list(self.tree.item(self.tree.selection()[0],'values')))
        if user_choice == "Delete Recipe":
            self.inventoryController.recipeIngredientDelete(list(self.tree.item(self.tree.selection()[0],'values')))
            messagebox.showinfo('Deletion', 'Deletion Successful! Please Refresh')
            return

    def _update_product_data(self):
        user_choice = CustomDialog(self.master,title="Product or Supply",buttons=["Update Product", "Delete Product"]).result
        if user_choice == "Update Product":
            self.inventoryController.productUpdate(list(self.tree.item(self.tree.selection()[0],'values')))
        if user_choice == "Delete Product":
            self.inventoryController.productDelete(list(self.tree.item(self.tree.selection()[0],'values')))
            messagebox.showinfo('Deletion', 'Deletion Successful! Please Refresh')
            return

    def _view_recipe_ingredients(self):
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("No Selection", "Please select a recipe first.")
            return

        recipe_values = Functions.convert_dicc_data(self.tree.item(selected_items[0], 'values'))
        ic(recipe_values)
        recipe_id = recipe_values[0]  # Assuming the recipe ID is the first column
        ic(recipe_id)
        ingredients = Functions.convert_dicc_data(self.inventoryController.get_recipe_ingredients(recipe_id))
        ic(ingredients)
        
        if not ingredients:
            messagebox.showinfo("No Ingredients", f"No ingredients found for recipe: {recipe_id}")
            return

        # Create a new window to display ingredients
        ingredients_window = tk.Toplevel(self)
        ingredients_window.title(f"Ingredients for {recipe_id}")
        self.h = 300
        self.w = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40
        ingredients_window.geometry(f"{self.w}x{self.h}+{x}+{y}")
        
        # Create a treeview to display ingredients
        ingredients_tree = ttk.Treeview(ingredients_window, columns=("Ingredient", "Description", "Quantity", "Unit"), show="headings")
        ingredients_tree.heading("Ingredient", text="Ingredient")
        ingredients_tree.heading("Description", text="Description")
        ingredients_tree.heading("Quantity", text="Quantity")
        ingredients_tree.heading("Unit", text="Unit")
        
        for ingredient, description, quantity, unit in ingredients:
            ingredients_tree.insert("", "end", values=(ingredient, description, quantity, unit))
        
        ingredients_tree.pack(expand=True, fill="both")


    def _update_button(self):
        update_button = tk.Button(self, font=font.Font(family='Courier New',size=9,weight='bold'),text="Update", 
                                   command=lambda:self._update_row_data(self.selectTable.get()))
        update_button.place(relx=0.9,rely=0.9,anchor='se')