import smtplib
import datetime as dt
import random
import pandas

# --------------Set Email and Password---------------
my_email = "@gmail.com"
password = ""

# --------------Check Date---------------------------
now = dt.datetime.now()
today = (now.month, now.day)

# ----------------CSV Data Handling------------------
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row.to_list() for (index, data_row) in data.iterrows()}

# ----------------Send Mail--------------------------
if today in birthdays_dict:
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as mail_letter:
        birthday_letter = mail_letter.read()
        birthday_letter = birthday_letter.replace("[NAME]", f"{birthdays_dict[today][0]}")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=f"{birthdays_dict[today][1]}",
                                msg=f"Subject:Happy Birthday\n\n{birthday_letter}")
