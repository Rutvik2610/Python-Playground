import requests
import smtplib
import time
from datetime import datetime

my_email = "@gmail.com"
password = ""

MY_LAT = 19.075983  # Your latitude
MY_LONG = 72.877655  # Your longitude


# Your position is within +5 or -5 degrees of the ISS position.
def check_position():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if abs(MY_LAT - iss_latitude) <= 5:
        if abs(MY_LONG - iss_longitude) <= 5:
            return True
        else:
            return False
    else:
        return False


# Check if it is still dark outside
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.utcnow()

    if sunset <= time_now.hour <= sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if check_position() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:ISS Overhead Notification\n\n"
                                    f"Hey look up!The ISS is above you.".encode("utf8")
                                )
