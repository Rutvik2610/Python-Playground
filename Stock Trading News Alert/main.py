import requests
import smtplib
import os
from datetime import date
from datetime import timedelta


today = date.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

my_email = os.environ.get("my_email")
password = os.environ.get("password")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

AVS_API = os.environ.get("AVS_API")
NEWS_API = os.environ.get("NEWS_API")

avs_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "60min",
    "outputsize": "compact",
    "apikey": AVS_API
}

news_parameters = {
    "q": "tesla",
    "from": f"{today - timedelta(days=30)}",
    "sortBy": "publishedA",
    "apiKey": NEWS_API
}

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
avs_response = requests.get(url=STOCK_ENDPOINT, params=avs_parameters)
avs_response.raise_for_status()
trading_data = avs_response.json()

stock_information = trading_data["Time Series (Daily)"]
yesterday_closing = float(stock_information[f"{yesterday}"]["4. close"])
db_yesterday_closing = float(stock_information[f"{day_before_yesterday}"]["4. close"])
diff_in_closing = abs(yesterday_closing - db_yesterday_closing) / yesterday_closing * 100

if diff_in_closing >= 5:
    print("Get News")

# Get the first 3 news pieces for the COMPANY_NAME.
news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
top_articles = news_data["articles"][:3]

# Send a seperate mail with the percentage change and each article's title and description to your mail id. 
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg=f"Subject:Stock Alert: TSLA %\n\n"
                            f"Headline: {top_articles[0]['title']}.\nBrief: {top_articles[0]['description']}\n\n"
                            f"Headline: {top_articles[1]['title']}.\nBrief: {top_articles[1]['description']}\n\n"
                            f"Headline: {top_articles[2]['title']}.\nBrief: {top_articles[2]['description']}\n\n".encode("utf8")
                        )
