import smtplib
import datetime as dt
import random
import pandas

my_email = ""
password = ""

letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row.to_list() for (index, data_row) in data.iterrows()}
print(birthdays_dict)

if today in birthdays_dict:
    with open(f"letter_templates/{random.choice(letter_list)}") as mail_letter:
        birthday_letter = mail_letter.read()
        birthday_letter = birthday_letter.replace("[NAME]", f"{birthdays_dict[today][0]}")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=f"{birthdays_dict[today][1]}",
                                msg=f"Subject:Happy Birthday\n\n{birthday_letter}")
