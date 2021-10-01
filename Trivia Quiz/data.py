import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

quiz_response = requests.get(url="https://opentdb.com/api.php", params=parameters)
quiz_response.raise_for_status()
question_data = quiz_response.json()["results"]