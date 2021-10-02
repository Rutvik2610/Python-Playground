import requests
import smtplib


# Login Credentials
my_email = "@gmail.com"
password = ""

# Parameters to be passed
parameters = {
    "lat": 19.075983,
    "lon": 72.877655,
    "appid": "",
    "exclude": "current,minutely,daily"
}

# Getting the data using Open Weather Map API
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

# Slicing the weather data for next 12 hours
hour_data = data["hourly"][:12]

will_rain = False

# Check if it will rain in next 12 hours
for hour in hour_data:
    condition_code = hour["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Rain Alert☔\n\n"
                                f"It's going to rain today. Remember to bring an umbrella with you.".encode("utf8")
                            )
