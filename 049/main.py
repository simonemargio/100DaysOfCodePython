import tweepy
import requests
from datetime import datetime

api_key = "twitter_api_key"
api_secret = "twitter_secret"
access_token = "twitter_app_token"
access_token_secret = "twitter_app_secret_token"

client = tweepy.Client(consumer_key=api_key,
                       consumer_secret=api_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret
                       )


stock_name = "AAPL"
company_name = "apple"
alpha_api_key = "api_key" # from www.alphavantage.co
news_api_key = "new_api_key" # from newsapi.org

response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_name}&apikey={alpha_api_key}")
response.raise_for_status()

data = response.json()

prev_day = list(data["Time Series (Daily)"])[1]
prev_prev_day = list(data["Time Series (Daily)"])[2]
stock_prev_close = float(data["Time Series (Daily)"][prev_day]["1. open"])
stock_prev_prev_close = float(data["Time Series (Daily)"][prev_prev_day]["4. close"])

difference = abs(stock_prev_close - stock_prev_prev_close)
diff_percent = (difference / stock_prev_close) * 100

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if diff_percent > 5:
    date_today = datetime.today().strftime('%Y-%m-%d')
    response = requests.get(f"https://newsapi.org/v2/everything?q={company_name}&from={date_today}&sortBy=publishedAt&apiKey={news_api_key}")
    response.raise_for_status()
    data_news = response.json()["articles"]
    three_articles = data_news[:1]

    formatted_articles = f"{stock_name}: {up_down}{diff_percent}%\n{three_articles[0]['title']}."

    response = client.create_tweet(text=formatted_articles)
    print(response)

