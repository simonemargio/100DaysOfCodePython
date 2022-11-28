from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import threading

item_prices = []
item_names = []


def get_cookies() -> str:
    return driver.find_element(By.ID, "money").text


def create_list_price_and_elements() -> None:
    all_upgrade = driver.find_element(By.ID, "store")

    for line in all_upgrade.text.splitlines():
        if "-" in line:
            single_line = line.split()

            name_upgrade = "buy" + single_line[0]
            if single_line[1] != "-":
                name_upgrade += " " + single_line[1]

            item_names.append(name_upgrade)

            price = single_line[-1]
            price = price.replace(",", "")
            item_prices.append(price)

    item_prices.reverse()
    item_names.reverse()


def check_upgrade():
    threading.Timer(5.0, check_upgrade).start()

    for upgrade in item_prices:
        if int(get_cookies()) >= int(upgrade):
            index_upgrade = item_prices.index(upgrade)
            name_upgrade = item_names[index_upgrade]
            button_upgrade = driver.find_element(By.ID, name_upgrade)
            print(f"Give my: {get_cookies()} cookies for the upgrade {name_upgrade} that costs {upgrade}")
            button_upgrade.click()


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://orteil.dashnet.org/experiments/cookie/")
create_list_price_and_elements()
check_upgrade()

while True:
    button = driver.find_element(By.ID, "cookie")
    button.click()
