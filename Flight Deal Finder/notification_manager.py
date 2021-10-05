import smtplib
import os

EMAIL_ID = os.environ.get("email_id")
PASSWORD = os.environ.get("password")


class NotificationManager:
    def __init__(self, flight_details):
        self.flight_details = flight_details

    def send_mail(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL_ID, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL_ID,
                                to_addrs=EMAIL_ID,
                                msg=f"Low Price Alert!✈\n\n"
                                    f"Only {self.flight_details.price} to fly from"
                                    f"{self.flight_details.origin_city}-{self.flight_details.origin_airport} to"
                                    f"{self.flight_details.destination_city}-{self.flight_details.destination_airport},"
                                    f"from {self.flight_details.out_date} - "
                                    f"{self.flight_details.return_date}.".encode("utf8"))
