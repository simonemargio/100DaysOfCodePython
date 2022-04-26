from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "your_twitter_email"
TWITTER_PASSWORD = "your_twitter_password"


class Speed:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        button_go = self.driver.find_element(By.CLASS_NAME, "start-text")
        button_go.click()
        sleep(50)
        self.up = self.driver.find_element(By.CLASS_NAME,
                                           "result-data-large.number.result-data-value.download-speed").text
        self.down = self.driver.find_element(By.CLASS_NAME,
                                             "result-data-large.number.result-data-value.upload-speed").text
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        enter_email = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        enter_email.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div')
        next_button.click()
        sleep(10)
        enter_password = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        enter_password.send_keys(TWITTER_PASSWORD)
        login_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]')
        login_button.click()
        sleep(5)
        click_tweet = self.driver.find_element(By.XPATH,
                                               '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        click_tweet.click()
        sleep(3)
        enter_tweet = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        enter_tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        sleep(3)
        post_tweet = self.driver.find_element(By.XPATH,
                                              '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        post_tweet.click()
        sleep(10)
        self.driver.quit()
