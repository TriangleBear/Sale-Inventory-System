from tkinter import font, messagebox
from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry
from Utils import Functions
class RecipeRegisterView(tk.Frame):
    def __init__(self,recipeRegisterController,master):
        self.master = master
        self.recipeRegisterController = recipeRegisterController
        super().__init__(self.master,background="Gray89")
        self.pack(fill=tk.BOTH,expand=True)
        self.mainBg = "Gray89"
        # self.recipe_labels_with_colspan = {
        #     "Recipe Name":1,
        #     "Category":1,
        #     "Ingredients":1,
        #     "Details":3
        # }
        # self.recipe_entry_boxes = []
        # self.recipe_inputs = []

    def main(self):
        self._entry_frame()
        self._recipe_label()
        self._recipe_name_entry()
        self._confirm_button()
        self._back_button()


    def _entry_frame(self):
        self.entryFrame = tk.Frame(self,background=self.mainBg,padx=40,pady=80)
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)
    
    def _recipe_label(self):
        recipe_label = tk.Label(self.entryFrame,font=font.Font(family='Courier New',size=14,weight='bold'),
                              text=f"Recipe Name: ",background=self.mainBg)
        recipe_label.grid(row=0,column=0)

    def _recipe_name_entry(self):
        self.recipe_name_entry = tk.Entry(self.entryFrame, borderwidth=0, width=23,font=font.Font(size=12))
        self.recipe_name_entry.grid(row=0,column=1)  

    def _register_recipe_ingredients(self,recipeDetails):
        print(recipeDetails)
        if messagebox.askyesno("Ingredients Registration","Do you want to register the ingredients for this recipe?"):
            self.recipeRegisterController.mC.ingredientRegisterController(recipeDetails)
        return

    def _commit_recipe_name(self,recipe_name):
        recipeDetails = self.recipeRegisterController.register_recipe(recipe_name)
        #recipeDetails = [recipe_id,recipe_name, user_id]
        if type(recipeDetails) == list:
            if messagebox.askyesno("Recipe Registration","Are you sure you want to register this recipe?"):
                self.recipeRegisterController.logUserActivity()
                messagebox.showinfo("Recipe Registration","Recipe Registered Successfully!")
                self._register_recipe_ingredients(recipeDetails)
        else:
            messagebox.showerror("Recipe Registration",recipeDetails)
        return

    def _confirm_button(self):
        confirm_button = tk.Button(self.entryFrame, font=font.Font(family='Courier New',size=9,weight='bold'),text="Confirm", 
                                   command=lambda:self._commit_recipe_name(Functions.format_str(self.recipe_name_entry.get())))
        confirm_button.grid(row=1,column=1,sticky='e')
    
    def _back_button(self):
        back_button = tk.Button(self, font=font.Font(family='Courier New',size=9,weight='bold'),text="Back", 
                                command=lambda:self.recipeRegisterController.manager_view(self.master))
        back_button.place(relx=0.1,rely=0.9,anchor='sw')  # Place the button at the bottom with some padding