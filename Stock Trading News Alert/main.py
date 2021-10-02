import requests
import smtplib
import os


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

my_email = os.environ.get("my_email")
password = os.environ.get("password")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

AVS_API_KEY = os.environ.get("AVS_API")
NEWS_API_KEY = os.environ.get("NEWS_API")

avs_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "60min",
    "outputsize": "compact",
    "apikey": AVS_API_KEY
}

news_parameters = {
    "qInTitle": COMPANY_NAME,
    "sortBy": "publishedA",
    "apiKey": NEWS_API_KEY
}


# Check the stocks.
avs_response = requests.get(url=STOCK_ENDPOINT, params=avs_parameters)
avs_response.raise_for_status()
trading_data = avs_response.json()["Time Series (Daily)"]

trading_data_list = [value for (key, value) in trading_data.items()]
yesterday_closing = float(trading_data_list[0]["4. close"])
db_yesterday_closing = float(trading_data_list[1]["4. close"])
diff_in_closing = (yesterday_closing - db_yesterday_closing) / yesterday_closing * 100
up_down = None
if diff_in_closing > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then sen mail.
if abs(diff_in_closing) > 5:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    top_articles = news_data["articles"][:3]
    formatted_top_articles = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in
                              top_articles]

    # Send a separate mail with the percentage change and each article's title and description to your mail id.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        for article in formatted_top_articles:
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:Stock Alert: TSLA {up_down}{round(abs(diff_in_closing), 3)}%\n\n"
                                    f"{article}".encode("utf8")
                                )
