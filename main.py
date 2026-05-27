import smtplib
import random
import datetime as dt
import os

with open ("quotes.txt") as file:
    all_quotes = file.readlines()
    random_quote = random.choice(all_quotes)

def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()       #Makes connection secure
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="tfm606.606@gmail.com",
                            msg=f"Subject: Friendly Reminder\n\n{random_quote}")
        connection.close()

send_email()
