import requests
from datetime import datetime

stock_name = "TSLA"
company_name = "tesla"
alpha_api_key = "your_alphavantage_api"

response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_name}&apikey={alpha_api_key}")
response.raise_for_status()

data = response.json()

prev_day = list(data["Time Series (Daily)"])[1]
prev_prev_day = list(data["Time Series (Daily)"])[2]
stock_prev_close = float(data["Time Series (Daily)"][prev_day]["1. open"])
stock_prev_prev_close = float(data["Time Series (Daily)"][prev_prev_day]["4. close"])

difference = abs(stock_prev_close - stock_prev_prev_close)
diff_percent = (difference / stock_prev_close) * 100

if diff_percent > 5:
    news_api_key = "your_newsapi_api"
    date_today = datetime.today().strftime('%Y-%m-%d')
    response = requests.get(f"https://newsapi.org/v2/everything?q={company_name}&from={date_today}&sortBy=publishedAt&apiKey={news_api_key}")
    response.raise_for_status()
    data_news = response.json()["articles"]

    for n_news in range(0, 3):
        print(
            f"News n.{n_news}\n{data_news[n_news]['title']}\n{data_news[n_news]['description']}\nMore info:{data_news[n_news]['url']}\n\n")
