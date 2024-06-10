#Decrepted for time being

import json
import os
import random
import smtplib
from email.message import EmailMessage
import pymysql

creds = ".creds/credentials.json"

with open(creds, "r") as f:
    credentials = json.load(f)


# Function to generate a 6-digit OTP
def generate_otp():
    otp = random.randint(100000, 999999)
    return otp


# Function to store the OTP in the database
def store_otp(email, otp):
    try:
        connection = pymysql.connect(
            host=credentials["host"],
            user=credentials["username"],
            password=credentials["password"],
            db="viviandb",
            port=22577,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO OTP (otp, email) VALUES (%s, %s)", (otp, email))
            connection.commit()
    finally:
        connection.close()


# Function to send the OTP via email
def send_otp(email, otp):
    msg = EmailMessage()
    msg['Subject'] = "OTP Verification"
    msg['From'] = credentials["sender_email"]
    msg['To'] = email
    msg.set_content(f"Your OTP is {otp}")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(credentials["sender_email"], credentials["sender_password"])
            server.send_message(msg)
        print("OTP sent successfully!")
    except Exception as e:
        print(f"Failed to send OTP: {e}")


# Function to validate the OTP by checking the database
def validate_otp_db(otp, email):
    try:
        connection = pymysql.connect(
            host=credentials["host"],
            user=credentials["username"],
            password=credentials["password"],
            db="viviandb",
            port=22577,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM OTP WHERE otp = %s AND email = %s", (otp, email))
            result = cursor.fetchone()
            if result:
                return True
            else:
                return False
    finally:
        connection.close()


# Example usage
email = input("Enter your Email: ")
otp = generate_otp()
store_otp(email, otp)
send_otp(email, otp)

user_input = input("Enter the OTP: ")
if validate_otp_db(user_input, email):
    print("OTP is valid!")
else:
    print("OTP is invalid!")
