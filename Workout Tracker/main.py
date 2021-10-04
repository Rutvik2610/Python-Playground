import requests
import os
import datetime as dt

# Environment variables and Constants
APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
NUTRITIONIX_API_ENDPOINT = " https://trackapi.nutritionix.com/v2"

# Headers for Nutritionix API
nutrix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Headers for Sheety API
sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}


def exercise_info(query):
    """Get Calorie information by passing workout details"""
    gender = ""
    weight = None
    height = None
    age = None
    exercise_endpoint = f"{NUTRITIONIX_API_ENDPOINT}/natural/exercise"
    exercise_parameters = {
        "query": query,
        "gender": gender,
        "weight_kg": weight,
        "height_cm": height,
        "age": age
    }
    exercise_response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=nutrix_headers)
    exercise_response.raise_for_status()
    return exercise_response.json()["exercises"]


# Enter data into sheet
project_name = ""
sheet_name = ""


def enter_sheet_data(exercise_details):
    """Pass exercise info to enter the data in Google Sheets"""
    sheety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/{project_name}/{sheet_name}"

    now = dt.datetime.now()
    today = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    for exercise in exercise_details:

        workouts = {
            "workout": {
                "date": today,
                "time": time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
        sheety_response = requests.post(url=sheety_endpoint, json=workouts, headers=sheety_headers)
        sheety_response.raise_for_status()


user_input = input("Tell me which exercises you did:\n")
exercise_data = exercise_info(user_input)
enter_sheet_data(exercise_data)
