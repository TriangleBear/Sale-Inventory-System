import tkinter as tk
from View import *
from tkinter import *
from tkinter import font, ttk, messagebox

class Functions:
    def create_entry_box_using_grid(frame, labels:dict, entryList:list, max_columns:int, max_rows:int=None, bgColor:str="Grey82",borderW:int=0,xPadding=5, yPadding=5, entryWidth=None):
        current_row = 0 
        current_column = 0 
        refName = [label for label in labels.keys()]
        print(refName)
        for string in refName:
            l = tk.Label(frame,borderwidth=borderW,background=bgColor,text=f"{string}:")
            l.grid(row=current_row,column=current_column,padx=xPadding,pady=yPadding)

            current_column += 1

            entry = tk.Entry(frame,borderwidth=borderW)
            entry.grid(row=current_row,column=current_column,columnspan=labels.get(f"{string}"),padx=xPadding,pady=yPadding)
            entryList.append(entry)

            if labels.get(f"{string}") > 1:
                entry.config(width=entryWidth)
                current_column += (labels.get(f"{string}"))
            
            if (current_column >= max_columns):
                current_column =0
                current_row +=1
            else:
                current_column +=1 

    # def register(register_inputs:list):

    #     register_var = [val.get() for val in register_inputs]

    #     controller.register(register_var)

    #     messagebox.showinfo('Registrion', 'Registraion Successful!')
    #     switch_page(login_page)

    # def checkInput(self, username, password):
    #     user = LoginModel.check_username(username)
    #     stored_password = LoginModel.get_password(username)
    #     if stored_password is not None:  # Assuming 'password' is the column name in the database
    #         if LoginModel.check_password(stored_password, password):
    #             return user['user_type']  # Assuming 'user_type' is the column name in the database
    #         else:
    #             return "Incorrect password"
    #     else:
    #         return "No such user was found"

    def clear_frame(page_to_destroy):
        for child in page_to_destroy.winfo_children():
            child.destroy()

    def destroy_page(page_to_destroy):
        for child in page_to_destroy.winfo_children():
            child.destroy()