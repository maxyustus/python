import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "54CQXTOHDOSZQO4U"
NEWS_API_KEY = "b0661467613546b1911310c027c0d7e5"
TWILIO_SID = "AC0c2f213a430f976bf64b5867faa5d3f9"
TWILIO_AUTH_TOKEN = "3eff95dbc1ad704a82e1e36dd9a60187"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

stock_price_difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = round(stock_price_difference / float(yesterday_closing_price)) * 100
if diff_percent > 5:
    news_parameters = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"{STOCK_NAME}: {diff_percent}%\nHeadline: {article['title']}. \nBrief:" \
                          f" {article['description']}"
                          for article in
                          three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+14077535057",
            to="+79227536239",
        )
