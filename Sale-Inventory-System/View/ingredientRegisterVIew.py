import tkinter as tk
from tkinter import *
from tkinter import font, messagebox
class IngredientRegisterView(tk.Toplevel):
    def __init__(self,ingredientRegisterController,recipe_id):
        super().__init__(background="GhostWhite")
        self.recipe_id = recipe_id
        self.recipeRegisterController = ingredientRegisterController
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
        self.headerFrame.place(x=0,y=0,width=self.w,height=20)
    
    def _base_frame(self):
        self.baseFrame = tk.Frame(self,background=self.mainBg)
        self.baseFrame.pack(fill=tk.BOTH,expand=True)

    def _entry_frame(self):
        self.entryFrame = tk.Frame(self.registerFrame,background=self.mainBg,padx=40,pady=80)
        self.entryFrame.grid(row=0,column=0,sticky='nsew')

    def _table_frame(self):
        self.registerFrame = tk.Frame(self.baseFrame,background=self.mainBg)
        self.registerFrame.grid(row=0,column=1,sticky='nsew')

    def _ingredient_label(self):
        ingredient_label = tk.Label(self.entryFrame,font=font.Font(family='Courier New',size=14,weight='bold'),
                                  text=f"Ingredient Name: ",background=self.mainBg)
        ingredient_label.grid(row=0,column=0)