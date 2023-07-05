import smtplib
import datetime as dt
import random
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("EMAIL_PASSWORD")
receiver = "Email2_Test@Yahoo.Com"

# Getting current time
now = dt.datetime.now()
day_of_the_week = now.weekday()

print(day_of_the_week)

# Accessing Quotes
file_path = "quotes.txt"

if day_of_the_week == 2:
    with open(file_path, "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    # SMTP EMAIL
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver,
                            msg=f"SUBJECT:Today's Motivational Quote\n\n" + quote)
