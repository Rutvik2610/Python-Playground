import requests

TOKEN = ""
USER_NAME = ""
GRAPH_ID = ""
headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"

# To create an account
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
pixela_respone = requests.post(url=pixela_endpoint, json=user_params)


# To create a graph
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Jogging Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


# To add pixel
pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

pixel_config = {
    "date": "20211003",
    "quantity": "2.1"
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)

