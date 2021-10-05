from datetime import datetime
from datetime import timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "BOM"

sheet1 = DataManager("flightDeals", "prices")
flight_search = FlightSearch()

sheet_data = sheet1.get_data()
# for row in sheet_data["prices"]:
#     if row["iataCode"] == "":
#         sheet1.edit_data(flight_search.get_city_code(row["city"]), row["id"])

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
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
            notification = NotificationManager(flight)
            notification.send_mail()
