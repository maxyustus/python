import smtplib
import datetime as dt
import random

MY_EMAIL = "lakersdollarbill@gmail.com"
MY_PASSWORD = "your_password"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    with open("quotes.txt", "r") as data_file:
        all_quotes = data_file.readlines()
        random_quote = random.choice(all_quotes)

    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{random_quote}"
        )
