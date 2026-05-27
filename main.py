import smtplib
import random
import datetime as dt
import os

my_email = os.environ.get("t.ferro1009@gmail.com")
password = os.environ.get("txyysrlqiywwgeoy")

with open ("quotes.txt") as file:
    all_quotes = file.readlines()
    random_quote = random.choice(all_quotes)

def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()       #Makes connection secure
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="tfm606.606@gmail.com",
                            msg=f"Subject: Friendly Reminder\n\n{random_quote}")
        connection.close()


now = dt.datetime.now()
day_of_the_week = now.weekday()
if day_of_the_week == 0:
    send_email()
