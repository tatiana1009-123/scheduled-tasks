import smtplib
import random
import datetime as dt
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

recipients = ["tfm606.606@gmail.com", "pjmozingo604@gmail.com", "julio.ferro2009@hotmail.com", "maritza_montaa@yahoo.es"]

with open("quotes.txt") as file:
    all_quotes = file.readlines()
    random_quote = random.choice(all_quotes).strip()

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=recipients,
        msg=f"Subject: Friendly Reminder\n\n{random_quote}"
    )
