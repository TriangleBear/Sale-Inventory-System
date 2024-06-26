import tkinter as tk
from tkinter import *
from tkinter import ttk, font, messagebox
from Utils import Functions
class IngredientRegisterView(tk.Toplevel):
    def __init__(self,ingredientRegisterController,recipe_id):
        super().__init__(background="GhostWhite")
        self.recipe_id = recipe_id
        self.table = ['Ingredient Name', 'Quantity', 'Unit']
        self.ingredientRegisterController = ingredientRegisterController
        self._window_attributes()

        self.ingredient_labels_with_colspan = {
            "Ingredient Name":1,
            "Quantity":1,
            "Unit":1
        }
        self.ingredient_entry_boxes = []
        self.mainBg = "Gray89"

    def main(self):
        self._header_frame()
        self._header_label(f"{self.recipe_id}")
        self._base_frame()
        self.display_table()
        self._entry_frame()
        self._ingredient_entry_widgets()
        self._add_ing_btn()
        self._remove_ing_btn()
        self._cancel_btn()
        self._save_btn()
        self.mainloop()

    def _window_attributes(self):
        self.h = 520
        self.w = 680
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        self.title('Ingredients Registration')
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.quit())

    
    def _header_frame(self):
        self.headerFrame = tk.Frame(self,background=self.mainBg)
        self.headerFrame.place(x=0,y=0,width=self.w,height=30)
    
    def _header_label(self, text:str):
        self.headerLabel = tk.Label(self.headerFrame,background=self.mainBg,font=font.Font(family='Courier New',size=12,weight='bold'),
                                    text=f"Ingredients Registration | {text}")
        self.headerLabel.place(relx=0.05,rely=0.5,anchor='w')

    def _base_frame(self):
        self.baseFrame = tk.Frame(self, background=self.mainBg)
        self.baseFrame.place(x=15, y=43, width=self.w-30, height=460)
        
    def _entry_frame(self):
        self.entryFrame = tk.Frame(self.baseFrame, background=self.mainBg,width=50,height=50)
        self.entryFrame.place(relx=0.05, rely=0.5, anchor='w')

    def _ingredient_entry_widgets(self):
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=self.ingredient_labels_with_colspan,
            entryList=self.ingredient_entry_boxes,
            shortEntryWidth=23,
            side='e',
            borderW=1,
            bgColor=self.mainBg,
            max_columns=1,
            yPadding=15
        )

    def display_table(self):
        self.tree = ttk.Treeview(self.baseFrame, columns=self.table, show='headings')
        for col in self.table:
            self.tree.heading(col, text=col)    
            self.tree.column(col, anchor='e')
        # Assuming `self.tree` is your Treeview widget
        self.tree.bind("<Configure>", Functions.adjust_column_widths)
        self.tree.place(relx=0.975, rely=0.032,anchor='ne',width=330,height=380)

    def _add_ing_btn(self):
        add_btn = tk.Button(self.baseFrame, font=font.Font(family='Courier New', size=9, weight='bold'),
                            text="Add Ingredient", command=lambda: self._checkInput())
        add_btn.place(relx=0.13, rely=0.69, anchor='center')

    def _remove_ing_btn(self):
        remove_btn = tk.Button(self.baseFrame, font=font.Font(family='Courier New', size=9, weight='bold'),
                               text="Remove Ingredient", command=lambda: self.remove_ingredient())
        remove_btn.place(relx=0.33, rely=0.69, anchor='center')
    
    def _cancel_btn(self):
        cancel_btn = tk.Button(self.baseFrame, font=font.Font(family='Courier New', size=9, weight='bold'),
                               text="Cancel", command=lambda: self.destroy())
        cancel_btn.place(relx=0.6, rely=0.92, anchor='center')

    def _save_btn(self):
        save_btn = tk.Button(self.baseFrame, font=font.Font(family='Courier New', size=9, weight='bold'),
                             text="Save", command=lambda: self.save_transaction())
        save_btn.place(relx=0.9, rely=0.92, anchor='center')
        
        

    def _insert_data(self, data):
        self.tree.insert('', 0, values=data)

    def _checkInput(self):
        ingredients = [entry.get() for entry in self.ingredient_entry_boxes]
        for item in ingredients:
            if item == '':
                messagebox.showerror("Error", f"Please fill in {item}")
                return 
        self._insert_data(ingredients)

    def remove_ingredient(self):
        selected_item = self.tree.selection()
        if selected_item:
            for i in selected_item:
                self.tree.delete(i)
        else:
            messagebox.showerror("Error", "Please select an item to remove")

    def save_transaction(self):
        ingList = [self.recipe_id]
        for child in self.tree.get_children():
            ingList.append(self.tree.item(child)['values'])
        print(ingList)
        self.ingredientRegisterController.save_transaction(ingList)
        messagebox.showinfo("Success", "Transaction Saved")
        if not messagebox.askyesno("Continue?", "Add more Ingredients?"):
            self.destroy()
        else:
            return