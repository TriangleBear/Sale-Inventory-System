from View import *
from tkinter import *
from tkinter import font, ttk, messagebox
from Utils import *
from email.message import EmailMessage
import smtplib
import tkinter as tk
import random


class Functions:
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
    


    def create_entry_box_using_grid(frame, labels:dict, entryList:list, max_columns:int, max_rows:int=None,current_r=0,current_c=0, bgColor:str="Grey82",borderW:int=0,xPadding=5, yPadding=5, entryWidth=None):
        current_row = current_r
        current_column = current_c
        refName = [label for label in labels.keys()]
        print(refName)
        for string in refName:
            l = tk.Label(frame,borderwidth=borderW,background=bgColor,text=f"{string}:")
            l.grid(row=current_r,column=current_c,padx=xPadding,pady=yPadding)

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

    def destroy_page(page_to_destroy):
        for child in page_to_destroy.winfo_children():
            child.destroy()
