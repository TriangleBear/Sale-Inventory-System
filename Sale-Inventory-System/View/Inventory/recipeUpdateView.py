from tkinter import font, messagebox
from tkinter import *
import tkinter as tk
from Utils import Functions
from PIL import Image,ImageTk

class RecipeUpdateView(tk.Toplevel):
    def __init__(self,managerController,recipeUpdateController,recipe_id,recipe_name):
        self.mC = managerController
        self.recipeUpdateController = recipeUpdateController
        self.recipe_id = recipe_id
        self.recipe_name = recipe_name
        super().__init__(background="Gray89")
        self._window_attributes()
        self.mainBg = "Gray89"

    def main(self):
        self._entry_frame()
        self._recipe_id_label()
        self._recipe_entry_label()
        self._recipe_name_entry()
        self._confirm_button()
        self._back_button()
        self.mainloop()

    def _window_attributes(self):
        self.h = 420
        self.w = 580
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        # image = Image.open('Assets\\icon.jpg')
        # photo_image = ImageTk.PhotoImage(image)
        # self.iconphoto(False, photo_image)
        self.title('Update Recipe')
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()

    def _entry_frame(self):
        self.entryFrame = tk.Frame(self,background=self.mainBg,padx=40,pady=80)
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)
    
    def _recipe_id_label(self):
        recipe_label = tk.Label(self,font=font.Font(family='Courier New',size=14,weight='bold'),
                              text=f"Recipe ID: {self.recipe_id} ",background=self.mainBg)
        recipe_label.place(relx=0.5,rely=0.38,anchor=CENTER)


    def _recipe_entry_label(self):
        recipe_label = tk.Label(self.entryFrame,font=font.Font(family='Courier New',size=14,weight='bold'),
                              text=f"Recipe Name: ",background=self.mainBg)
        recipe_label.grid(row=0,column=0)

    def _recipe_name_entry(self):
        self.recipe_name_entry = tk.Entry(self.entryFrame, borderwidth=0, width=23,font=font.Font(size=12))
        self.recipe_name_entry.insert(0,self.recipe_name)
        self.recipe_name_entry.grid(row=0,column=1)  

    def _confirm_button(self):
        confirm_button = tk.Button(self.entryFrame, font=font.Font(family='Courier New',size=9,weight='bold'),text="Confirm", 
                                   command=lambda:self._commit_recipe_name(recipe_id=self.recipe_id,recipe_name=Functions.format_str(self.recipe_name_entry.get())))
        confirm_button.grid(row=1,column=1,sticky='e')
    
    def _back_button(self):
        back_button = tk.Button(self, font=font.Font(family='Courier New',size=9,weight='bold'),text="Back", 
                                command=lambda:self.destroy())
        back_button.place(relx=0.1,rely=0.9,anchor='sw')  # Place the button at the bottom with some padding

    def _update_recipe_ingredients(self,recipeDetails):
        if messagebox.askyesno("Ingredient Management","Do you want to update the ingredients for this recipe?"):
            self.destroy()
            self.recipeUpdateController.inventoryController.recipeIngredientUpdate(recipeDetails)
        self.destroy()
        return

    def _commit_recipe_name(self,recipe_id,recipe_name):
        recipeDetails = self.recipeUpdateController.update_recipe(recipe_id,recipe_name)
        #recipeDetails = [recipe_id,recipe_name, user_id]
        if type(recipeDetails) == list:
            if messagebox.askyesno("Recipe Registration","Are you sure you want to update this recipe?"):
                self.recipeUpdateController.logUserActivity()
                messagebox.showinfo("Recipe Update","Recipe Updated Successfully!")
                self._update_recipe_ingredients(recipeDetails)
        else:
            messagebox.showerror("Recipe Registration",recipeDetails)
        return