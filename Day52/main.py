# Author: Deepak Kumar Singh
# Descr: Instagram bot to auto follow users.
# Date Created: 05/03/2022
# Date Modified: 05/03/2022

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

INSTA_USERID = "YourUserID"
INSTA_PASSWORD = "YourInstaPassword"
INSTA_URL = "https://www.instagram.com/accounts/login/"
INSTA_ACCOUNT = "codemonkeystu"
chrome_driver_path = "/Users/deepaksingh/Documents/Softwares/ChromeDriver/chromedriver"

class InstaFollower():
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)


    def login(self):
        self.driver.get(INSTA_URL)
        self.driver.maximize_window()
        # Wait for the site to finish loading
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))

        close_popup = self.driver.find_element_by_css_selector('.mt3GC .HoLwm')
        close_popup.click()
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        sleep(10)
        username.send_keys(INSTA_USERID)
        password.send_keys(INSTA_PASSWORD)

        sleep(5)
        password.send_keys(Keys.ENTER)


    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{INSTA_ACCOUNT}")
        self.driver.maximize_window()

        sleep(2)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


ig_bot = InstaFollower(chrome_driver_path)
ig_bot.login()
ig_bot.find_followers()
ig_bot.follow()