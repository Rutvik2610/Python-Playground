import os
import requests


USERNAME = os.environ.get("SHEETY_USERNAME")
TOKEN = os.environ.get("SHEETY_TOKEN")


class DataManager:

    def __init__(self, project_name, sheet_name):
        self.username = USERNAME
        self.token = TOKEN
        self.header = {
            "Authorization": f"Bearer {self.token}"
        }
        self.project_name = project_name
        self.sheet_name = sheet_name
        self.endpoint = f"https://api.sheety.co/{self.username}/{self.project_name}/{self.sheet_name}"
        self.sheet_data = {}

    def get_data(self):
        response = requests.get(url=self.endpoint, headers=self.header)
        response.raise_for_status()
        self.sheet_data = response.json()[f"{self.sheet_name}"]
        return self.sheet_data

    def enter_data(self, city_name, lowest_price):
        prices = {
            "price": {
                "city": city_name,
                "iataCode": "",
                "lowestPrice": lowest_price
            }
        }
        enter_response = requests.post(url=self.endpoint, json=prices, headers=self.header)
        enter_response.raise_for_status()

    def edit_data(self, iata_code, row_id):
        prices = {
            "price": {
                "iataCode": iata_code,
            }
        }
        edit_response = requests.put(url=f"{self.endpoint}/{row_id}", json=prices, headers=self.header)
        edit_response.raise_for_status()
