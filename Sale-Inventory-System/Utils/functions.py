from View import *
from tkinter import *
from tkinter import font, ttk, messagebox
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
            labels:list,
            entryList:list,
            max_columns:int,
            max_rows:int=None,
            fontSize=9,
            current_r=0,
            current_c=0,
            bgColor:str=None,
            borderW:int=1,
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
            b = tk.Button(frame,
                        font=font.Font(family='Courier New',size=fontSize,weight='bold'),
                        borderwidth=borderW,
                        background=bgColor,
                        text=f"{string}", width=w,height=h,
                        padx=btnxPadding,pady=btnyPadding,
                        command=lambda var=string:cmd(f"{var}"))
            current_column +=1
            b.grid(row=current_row,column=current_column,columnspan=columnSpan,padx=gridxPadding,pady=gridyPadding,sticky=side)
            entryList.append(b)



            if (current_column >= max_columns):
                current_column =0
                current_row +=1
            else:
                current_column +=1 
        

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
                        letter = "S"
                    elif access_level == "Manager":
                        letter = "M"
                    elif access_level == "Item":
                        letter = "I"
                    unique_id = letter + digits
                    sql = 'SELECT user_id FROM User WHERE user_id = %s'
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

    def create_entry_box_using_grid(frame,
                                    labels:dict,
                                    entryList:list,
                                    max_columns:int,
                                    max_rows:int=None,
                                    current_r=0,
                                    current_c=0,
                                    bgColor:str="Grey82",
                                    borderW:int=0,
                                    xPadding=5,
                                    yPadding=5,
                                    longEntryWidth=None,
                                    shortEntryWidth=None,
                                    labelWidth=None,
                                    side=None):
        current_row = current_r
        current_column = current_c
        refName = [label for label in labels.keys()]
        # print(refName)
        for string in refName:
            l = tk.Label(frame,borderwidth=borderW,background=bgColor,text=f"{string}:",width=labelWidth)
            l.grid(row=current_row,column=current_column,padx=xPadding,pady=yPadding,sticky=side)

            current_column += 1

            entry = tk.Entry(frame,borderwidth=borderW,width=shortEntryWidth)
            entry.grid(row=current_row,column=current_column,columnspan=labels.get(f"{string}"),padx=xPadding,pady=yPadding)
            entryList.append(entry)

            if labels.get(f"{string}") > 1:
                entry.config(width=longEntryWidth)
                current_column += (labels.get(f"{string}"))
            
            if (current_column >= max_columns):
                current_column =0
                current_row +=1
            else:
                current_column +=1 

    def destroy_page(page_to_destroy):
        for child in page_to_destroy.winfo_children():
            child.destroy()
