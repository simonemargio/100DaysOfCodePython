import requests
from twilio.rest import Client

endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "openweathermap_api_key"
account_sid = 'twilio_sid'
auth_token = 'twilio_token'


params = {
    "lat": 0,
    "lon": 0,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(endpoint, params=params)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False

for hour in weather_slice:
    code_condition = hour["weather"][0]["id"]
    if int(code_condition) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Hey bro u need an umbrella! ☔️",
        from_='twilio_number',
        to='your_number',
    )
    print(message.status)