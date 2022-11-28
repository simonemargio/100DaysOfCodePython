import requests
import smtplib
import time
from datetime import datetime

MY_LAT = float("your_latitude")
MY_LNG = float("your_longitude")
email = "your_email_here"
password = "your_password_email_here"


def send_email(receiver, letter):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=receiver,
            msg=f"Subject:Hey :)\n\n{letter}")


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()

    if iss_latitude - 5 <= MY_LAT <= iss_latitude + 5 and iss_longitude - 5 <= MY_LNG <= iss_longitude + 5 and time_now.hour <= sunset:
        send_email(email, "Yo bro, look up, the ISS is above you in the sky 😄!")

    time.sleep(360000)