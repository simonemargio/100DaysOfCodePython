import requests
import smtplib
from bs4 import BeautifulSoup
import lxml

URL = "amazon_url_product_you_want_to_track"
PARAMETERS = {
    # See (http://myhttpheader.com/) for those informations
    "User-Agent": "your_user_agent",
    "Accept-Language": "your_language",
}
EMAIL = "your_email"
PASSWORD = "your_password"
your_price = "float_value_price_for_the_product"


def send_email(letter):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Hey :)\n\n{letter}")


response = requests.get(url=URL, headers=PARAMETERS)
response.raise_for_status()

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(name='span', class_="a-offscreen").getText().replace("€", "").replace(",", ".")
product = soup.find(name='span', id="productTitle").getText().strip()


if float(price) <= float(your_price):
    send_email(f"The price of the {product} product now costs {price}.\n\nIt's time now, buy it!")
