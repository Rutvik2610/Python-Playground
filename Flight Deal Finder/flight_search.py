import requests
import os
from flight_data import FlightData

API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:
    def __init__(self):
        self.tequila_headers = {
            "apikey": API_KEY
        }
        self.endpoint = TEQUILA_ENDPOINT

    def get_city_code(self, city_name):
        """Returns IATA Code of the city"""
        query = {
            "term": city_name,
            "location_types": "city"
        }
        search_response = requests.get(url=f"{self.endpoint}/locations/query", params=query, headers=self.tequila_headers)
        search_response.raise_for_status()
        return search_response.json()["locations"][0]["code"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=self.tequila_headers, params=query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
            stop_overs=1,
            via_city=data["route"][0]["cityTo"]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
