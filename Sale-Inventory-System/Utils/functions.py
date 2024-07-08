from View import *
from tkinter import *
from tkinter import font, ttk, messagebox
import customtkinter as ctk
from tkcalendar import DateEntry
from Utils import *
from email.message import EmailMessage
import smtplib
import tkinter as tk
import random, string
from datetime import datetime
from hashlib import sha256


class Functions:
    def logUserActivity(userActivityData:list):
        #[userID,activity,logDate]
        from Model import SecurityModel
        model = SecurityModel(activityData=userActivityData)
        model.log_user_activity()

    def get_current_date(data:str=None):
        if data=="date":
            return datetime.now().date()
        if data=="datetime":
            return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def create_buttons_using_grid(
            frame,
            labels: list,
            entryList: list,
            max_columns: int,
            max_rows: int = None,
            fontSize=9,
            current_r=0,
            current_c=0,
            bgColor: str = None,
            borderW: int = 1,
            w=None,
            h=None,
            columnSpan=None,
            gridxPadding=10,
            gridyPadding=5,
            btnxPadding=None,
            btnyPadding=None,
            activeBg=None,
            side=None,
            relf=None,
            cmd=None
    ):
        current_row = current_r
        current_column = current_c
        for string in labels:
            b = ctk.CTkButton(
                    frame,
                    font=ctk.CTkFont(family='Courier New', size=fontSize, weight='bold'),
                    text=f"{string}",
                    width=w,
                    height=h,
                    fg_color=bgColor,
                    corner_radius=borderW,
                    command=lambda var=string: cmd(f"{var}")
                )
            current_column += 1
            b.grid(row=current_row, column=current_column, columnspan=columnSpan, padx=gridxPadding, pady=gridyPadding, sticky=side)
            entryList.append(b)

            if current_column >= max_columns:
                current_column = 0
                current_row += 1
            else:
                current_column += 1

    def create_table_using_grid(
            frame,
            labels: list,
            entryList: list,
            max_columns: int,
            max_rows: int = None,
            fontSize=9,
            current_r=0,
            current_c=0,
            bgColor: str = None,
            borderW: int = 1,
            w=None,
            h=None,
            columnSpan=None,
            gridxPadding=10,
            gridyPadding=5,
            btnxPadding=None,
            btnyPadding=None,
            side=None,
            cmd=None
    ):
        current_row = current_r
        current_column = current_c
        for string in labels:
            b = ctk.CTkLabel(
                    frame,
                    font=ctk.CTkFont(family='Courier New', size=fontSize, weight='bold'),
                    text=f"{string}",
                    width=w,
                    height=h,
                    fg_color=bgColor,
                    corner_radius=borderW,
                )
            current_column += 1
            b.grid(row=current_row, column=current_column, columnspan=columnSpan, padx=gridxPadding, pady=gridyPadding, sticky=side)
            entryList.append(b)

            if current_column >= max_columns:
                current_column = 0
                current_row += 1
            else:
                current_column += 1


    def create_entry_box_using_grid(
            frame,
            labels: dict,
            entryList: list,
            max_columns: int,
            max_rows: int = None,
            current_r=0,
            current_c=0,
            bgColor: str = "Grey89",
            borderW: int = 0,
            xPadding=5,
            yPadding=5,
            longEntryWidth=None,
            shortEntryWidth=None,
            labelWidth=None,
            side=None
    ):
        current_row = current_r
        current_column = current_c
        refName = [label for label in labels.keys()]

        for string in refName:
            l = ctk.CTkLabel(
                frame,
                text=f"{string}:",
                width=labelWidth,
                fg_color=bgColor,
                corner_radius=borderW
            )
            l.grid(row=current_row, column=current_column, padx=xPadding, pady=yPadding, sticky=side)

            current_column += 1

            entry = ctk.CTkEntry(
                frame,
                width=shortEntryWidth,
                fg_color=bgColor,
                corner_radius=borderW
            )
            entry.grid(row=current_row, column=current_column, columnspan=labels.get(f"{string}"), padx=xPadding, pady=yPadding)
            entryList.append(entry)

            if labels.get(f"{string}") > 1:
                entry.config(width=longEntryWidth)
                current_column += labels.get(f"{string}")

            if current_column >= max_columns:
                current_column = 0
                current_row += 1
            else:
                current_column += 1

    def check_password_criteria(password,username,email,fname,lname,old_password=None):
        #fname, lname, user_type, birthdate, contact_num, email,address, username, password
        if password == '':
            return ValueError("Password cannot be empty")
        if len(password) < 8 or len(username) > 15:
            return ValueError("Password must be at least 8-15 characters long")
        if not any(char.isdigit() for char in password):
            return ValueError("Password must have at least one numeral")
        if not any(char.isupper() for char in password):
            return ValueError("Password must have at least one uppercase letter")
        if not any(char.islower() for char in password):
            return ValueError("Password must have at least one lowercase letter")
        if not any(char in ['$', '@', '#', '%', '!', '&', '*'] for char in password):
            return ValueError("Password must have at least one special character")
        if old_password != None and old_password == sha256(password.encode()).hexdigest():
            return ValueError("New password cannot be the same as the old password")
        if username in password:
            return ValueError("Username and password cannot be the same")
        if email in username:
            return ValueError("Email and username cannot be the same")
        if (fname in password) or (lname in password):
            return ValueError("First and last name cannot be part of the Password")
        return 0

    def generate_unique_id(access_level:str):
        with Database.get_db_connection() as vivdb:
            with vivdb.cursor() as cursor:
                while TRUE:
                    digits = ''.join(random.choices(string.digits, k=4))
                    if access_level == "Staff":
                        sql = 'SELECT user_id FROM User WHERE user_id = %s'
                        letter = "S"
                    elif access_level == "Manager":
                        sql = 'SELECT user_id FROM User WHERE user_id = %s'
                        letter = "M"
                    elif access_level == "Item":
                        sql = 'SELECT item_id FROM Items WHERE item_id = %s'
                        letter = "I"
                    elif access_level == "Recipe":
                        sql = 'SELECT recipe_id FROM Recipes WHERE recipe_id = %s'
                        letter = "R"
                    elif access_level == "Ingredient":
                        sql = 'SELECT ingd_id FROM Ingredients WHERE ingd_id = %s'
                        letter = "C"
                    elif access_level == "Product":
                        sql = 'SELECT product_id FROM Product WHERE product_id = %s'
                        letter = "P"
                    elif access_level == "Sales":
                        sql = 'SELECT sales_id FROM Sales WHERE sales_id = %s'
                        letter = "SL"
                    elif access_level == "Invoice":
                        sql = 'SELECT invoice_id FROM Invoice WHERE invoice_id = %s'
                        letter = "INV"
                    unique_id = letter + digits
                    cursor.execute(sql, (unique_id,))
                    if not cursor.fetchone():
                        vivdb.close()
                        return unique_id
                vivdb.close()

    def send_otp_email(email, otp):
        sender_email = Credentials.appemail
        sender_password = Credentials.apppass

        msg = EmailMessage()
        msg['Subject'] = "OTP Verification"
        msg['From'] = sender_email
        msg['To'] = email
        msg.set_content(f"Your OTP is {otp}")

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                print(f"From send_otp_email (sender_email): {sender_email}")
                server.send_message(msg)
            print("OTP sent successfully!")
        except Exception as e:
            print(f"Failed to send OTP: {e}")

    def generate_otp():
        otp = random.randint(100000, 999999)
        return otp

    def treeview_style(background):
        style = ttk.Style()
        style.configure("Custom.Treeview.Heading",background=background, foreground="black",borderwidth=0,relief="sunken")
        style.configure("Custom.Treeview",background=background, foreground="black",borderwidth=0,relief="sunken")
        style.layout("Custom.Treeview",[('Treeview.treearea',{'sticky':'nswe'})])

    def change_column(tree, column_lables:list):
        tree["columns"] = column_lables
        for col in column_lables:
            tree.column(col, anchor=tree.column(col)['anchor'], width=tree.column(col)['width'])
            tree.heading(col, text=col, anchor=tree.heading(col)['anchor'])

    def format_float_list(data:list):
        temp = []
        for _ in data:
            temp.append(float(_))
        return temp
    
    def format_float(data:str):
        return float(data)

    def format_str_list(data:list):
        temp = []
        for _ in data:
            temp.append(str(_).strip().title())
        return temp
    
    def format_str(data:str):
        return str(data).strip().title()

    def format_ingredient_data(data:list,str_list_func=format_str_list, float_func=format_float):
        return [*str_list_func(data[0:2]),
                float_func(data[2]),
                data[3]]
    
    def format_user_data(data:list,str_func=format_str,str_list_func=format_str_list):
        return [*str_list_func(data[0:5]),
                data[5],
                str_func(data[6]),
                data[7],
                data[8]]

    def format_item_data(data:list,str_func=format_str,float_func=format_float,str_list_func=format_str_list):
        return [str_func(data[0]),
                float_func(data[1]),
                *str_list_func(data[2:6]),
                float_func(data[6]),
                float_func(data[7])]
    
    def format_product_data(data:list,str_func=format_str,float_func=format_float,str_list_func=format_str_list):
        return [float_func(data[0]),
                float_func(data[1]),
                *str_list_func(data[2:4]),
                float_func(data[4]),
                float_func(data[5])]
    
    def filter_item_data(data:list):
        temp = []
        for _ in data:
            temp.append(_)
        return temp
    
    def format_float(data:str):
        return float(data)

    def format_cart_item(product, quantity, price):
        return [product, int(quantity), float(price)]

    
    def check_existing_data(insertData,insertedData):
        name,descript,quantity,unit = insertData
        exisiting_name,existing_descript,exisiting_quantity,exisiting_unit = insertedData
        print
        if name == exisiting_name and descript == existing_descript and unit == exisiting_unit :
            updated_quantity = exisiting_quantity + quantity
            return [name,descript,updated_quantity,unit]
        elif name == exisiting_name and descript == existing_descript and unit != exisiting_unit:
            return ValueError("Quantity unit must be the same to update the item.")
        else:
            return

    def check_existing_cart_item(insertData,insertedData,quantity_available):
        product_name,quantity,price = insertData
        existing_name,existing_quantity = insertedData[0:2]
        if product_name != existing_name:
            return
        new_quantity = int(existing_quantity) + quantity
        if new_quantity <= int(quantity_available):
            return [product_name,new_quantity,float(price*new_quantity)]
        else:
            return ValueError("Quantity is greater than available stock.")
        
        # if product_name == self.tree_cart.item(iid, 'values')[0]:
        #         current_quantity = int(self.tree_cart.item(iid, 'values')[1])
        #         new_quantity = current_quantity + quantity
        #         new_total_price = new_quantity * price
        #         if new_quantity > int(quantity_available):
        #             return messagebox.showerror("Error", "Quantity is Greater than available stock.")
        #         self.tree_cart.item(iid, values=(product_name, new_quantity, new_total_price))
        #         self.calculate_total_amount()
        #         self.update_total_amount_label(self.total_amount)
        #         return
    
        
    #Convert dictionary row to a list in the order of self.table columns
    def convert_dicc_data(data=None):
        current_index = 0
        if data is None:
            data = []
        for row in data:
            if isinstance(row, dict):
                try:
                    temp_row = []
                    for value in row.values():
                        temp_row.append(value)
                except KeyError as e:
                    print(f"Missing key in row data: {e}")
                    continue
            elif not isinstance(row, (list, tuple)):
                print(f"Row format error: {row}")
                continue
            row = temp_row
            data[current_index] = row
            current_index += 1
        return data
    
    
    def adjust_column_widths(_):
        tree_width = _.width  # Get the current width of the Treeview
        num_columns = len(_.widget['columns'])
        # Subtract vertical scrollbar width if present, assuming a width of about 20 pixels
        scrollbar_width = 20
        usable_width = tree_width - scrollbar_width
        column_width = usable_width // num_columns  # Divide the usable width by the number of columns
        for col in _.widget['columns']:
            _.widget.column(col, width=column_width)  # Set each column to the calculated width

    def filter_ingredient_columns(data:list):
        temp = []
        for inner_dict in data:
            del inner_dict['recipe_id']
            del inner_dict['ingd_id']
            del inner_dict['user_id']

            temp.append(inner_dict)
        return temp

    def filter_product_columns(data:list[dict]):
        temp = []
        for inner_dict in data:
            del inner_dict['product_id']
            del inner_dict['user_id']
            del inner_dict['exp_date']
            del inner_dict['category']
            del inner_dict['flooring']
            del inner_dict['ceiling']
            del inner_dict['stock_level']

            temp.append(inner_dict)
        return temp

    def destroy_page(page_to_destroy):
        for child in page_to_destroy.winfo_children():
            child.destroy()

    def check_stock_amount(existing:float,input:float):
        if input == existing:
            return input
        if input > existing:
            return existing + (input - existing)
        if input < existing:
            return existing - (existing - input)
        
    def filter_breakfast_products(data:list[dict]) -> list[dict]:
        temp = []
        for dict in data:
            if dict['category'] == "Breakfast":
                temp.append(dict)
        return temp
    
    def filter_lunch_products(data:list[dict]) -> list[dict]:
        temp = []
        for dict in data:
            if dict['category'] == "Lunch":
                temp.append(dict)
        return temp
    
    def filter_dinner_products(data:list[dict]) -> list[dict]:
        temp = []
        for dict in data:
            if dict['category'] == "Dinner":
                temp.append(dict)
    
        return temp
    
    def filter_desert_products(data:list[dict]) -> list[dict]:
        temp = []
        for dict in data:
            if dict['category'] == "Desert":
                temp.append(dict)
        return temp
    
    def filter_drinks_products(data:list[dict]) -> list[dict]:
        temp = []
        for dict in data:
            if dict['category'] == "Drinks":
                temp.append(dict)
        return temp
    
    def filter_snacks_products(data:list[dict]) -> list[dict]:
        temp = []
        for dict in data:
            if dict['category'] == "Snacks":
                temp.append(dict)
        return temp

class CustomShowInfo(tk.Toplevel):
    def __init__(self,master, title=None):
        pass


class CustomDialog(tk.Toplevel):
    def __init__(self, master, title=None, buttons=None):
        super().__init__(master)
        self.result = None

        if title:
            self.title(title)

        self.update_idletasks()  # Update the dialog to set its dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        # Set the window's position to the center of the screen
        self.geometry(f'+{center_x}+{center_y}')
        self.grab_set()
        self.resizable(False,False)
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=10)

        if buttons:
            for button_name in buttons:
                button = tk.Button(self.button_frame, text=button_name, command=lambda name=button_name: self.set_result(name))
                button.pack(side=tk.LEFT, padx=5)

        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.grab_set()
        self.wait_window(self)
        

    def set_result(self, result):
        self.result = result
        self.destroy()

    def on_close(self):
        self.result = None
        self.destroy()

class CustomComboboxDialog(tk.Toplevel):
    def __init__(self, values:list,title=None, prompt=None, controller=None,state=None):
        super().__init__()
        self._window_attributes()
        self.controller = controller
        self.state = state
        self.title = title
        self.result = None
        self.prompt = prompt
        self.values = values
        self.btn_lbl = ["ok","cancel"]
        self.btn_vals = []

    def main(self):
        self._base_frame()
        self._prompt()
        self._recipe_combobox()
        self._btn_frame()
        self._btn_widgets()
        self.mainloop()

    def _window_attributes(self):
        self.h = 100
        self.w = 150
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        self.title('combobox')
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.quit())

    def _base_frame(self):
        self.baseFrame = tk.Frame(self)
        self.baseFrame.pack(fill='both',expand=True)

    def _prompt(self):
        self.prompt = tk.Label(self.baseFrame, text=self.prompt)
        self.prompt.place(relx=0.5,rely=0.15, anchor=CENTER)

    def _recipe_combobox(self):
        self.combobox = ttk.Combobox(self.baseFrame, values=self.values)
        self.combobox.place(relx=0.5,rely=0.45, anchor=CENTER)

    def _btn_frame(self):
        self.btn_frame = tk.Frame(self)
        self.btn_frame.place(relx=0.5,rely=0.76, anchor=CENTER)

    def _btn_widgets(self):
        Functions.create_buttons_using_grid(frame=self.btn_frame,labels=self.btn_lbl,entryList=self.btn_vals,max_columns=2,cmd=self._check_command,btnxPadding=5)

    def _check_command(self,string):
        if string == "ok" and self.combobox.get() == "":
            messagebox.showerror('no input',"Please select a value from the combobox")
        if string == "ok" and self.combobox.get() != "" and self.state == "Home Made":
            recipe_id = self.combobox.get()[:5]
            recipe_name = self.combobox.get()[8:]
            self.destroy()
            self.controller.productRegisterController(recipe_id,recipe_name)
        if string == "ok" and self.combobox.get() != "" and self.state == "Pre Made":
            supply_id = self.combobox.get()[:5]
            supply_name = self.combobox.get()[8:]
            self.destroy()
            self.controller.productRegisterController(supply_id,supply_name)
        if string == "cancel":
            self.destroy()
            return
        

class CustomCalendar(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.date_entry = DateEntry(self)
        self.date_entry.pack(fill='both', expand=True)
        
        # Add a confirm button to handle date selection
        confirm_btn = tk.Button(self, text="Confirm", command=self._on_date_confirm)
        confirm_btn.pack(pady=10)
        
        self.grab_set()
        self.wait_window(self)

    def _on_date_confirm(self):
        # Fetch the date from DateEntry
        selected_date = self.date_entry.get()
        self.controller.set_date(selected_date)
        self.destroy()