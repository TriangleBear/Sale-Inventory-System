from tkinter import *
import tkinter as tk
from Utils import Functions
class RecipeRegisterView(tk.Toplevel):
    def __init__(self,recipeRegisterController):
        super().__init__(background="GhostWhite")
        self.recipeRegisterController = recipeRegisterController
        self._window_attributes()

        self.recipe_labels_with_colspan = {
            "Recipe Name":1,
            "Category":1,
            "Ingredients":1,
            "Details":3
        }
        self.recipe_entry_boxes = []
        self.recipe_inputs = []
        self.mainBg = "Gray89"

    def main(self):
        self._recipe_frame()  
        self._entry_frame()
        self._recipe_widgets()
        self._recipe_button()
        self._back_button()
        self.mainloop()

    def _window_attributes(self):
        self.h = 420
        self.w = 580
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        self.title('Recipe Registration')
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.quit())

    def _recipe_frame(self):
        self.recipeFrame = tk.Frame(self,background="GhostWhite")
        self.recipeFrame.pack(fill=tk.BOTH,expand=True)

    def _entry_frame(self):
        self.entryFrame = tk.Frame(self.recipeFrame,background=self.mainBg,padx=40,pady=80)
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)

    def _recipe_widgets(self):
        subset_one = {key:self.register_labels_with_colspan[key] for key in ["Recipe Name","Category","Ingredients"] if key in self.register_labels_with_colspan}
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=subset_one,
            bgColor=self.mainBg,
            entryList=self.recipe_entry_boxes,
            borderW=1,
            max_columns=2,
            current_r=2,
            current_c=0,
            longEntryWidth=54,
            side='e'
        )

    def _recipe_button(self):
        self.registerButton = tk.Button(self.entryFrame,text="Register",bg="SkyBlue1",command=self.recipeRegisterController.register_recipe)
        self.registerButton.grid(row=5,column=0,columnspan=2,pady=10)

    def _back_button(self):
        self.backButton = tk.Button(self.entryFrame,text="Back",bg="SkyBlue1",command=self.recipeRegisterController.back)
        self.backButton.grid(row=6,column=0,columnspan=2,pady=10)

    