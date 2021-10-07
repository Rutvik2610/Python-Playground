
import os
import requests

USERNAME = os.environ.get("SHEETY_USERNAME")
TOKEN = os.environ.get("SHEETY_TOKEN")
PROJECT_NAME = ""
SHEET_NAME = ""

print("Welcome to Rutvik's Flight Club!\nWe find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
confirm_email = input("Type your email again.\n")

if email == confirm_email:
    users_headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    sheety_endpoint = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

    users = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": confirm_email
        }
    }
    enter_response = requests.post(url=sheety_endpoint, json=users, headers=users_headers)
    enter_response.raise_for_status()

print("emails don't match")
