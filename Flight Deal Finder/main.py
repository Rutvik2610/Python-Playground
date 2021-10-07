from datetime import datetime
from datetime import timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "BOM"

sheet1 = DataManager("flightDeals", "prices")
sheet2 = DataManager("flightDeals", "users")
flight_search = FlightSearch()

price_sheet_data = sheet1.get_data()
user_sheet_data = sheet2.get_data()
user_email_list = [user["email"] for user in user_sheet_data]
# for row in price_sheet_data["prices"]:
#     if row["iataCode"] == "":
#         sheet1.edit_data(flight_search.get_city_code(row["city"]), row["id"])

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in price_sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    try:
        price = flight.price
    except AttributeError:
        continue
    else:
        if flight.price <= destination["lowestPrice"]:
            notification = NotificationManager(flight, user_email_list)
            notification.send_mail()
