from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

FB_EMAIL = YOUR FACEBOOK LOGIN EMAIL
FB_PASSWORD = YOUR FACEBOOK PASSWORD

chrome_driver_path = "/Users/deepaksingh/Documents/Softwares/ChromeDriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maxmize_window()

driver.get("http://www.tinder.com")
main_page = driver.current_window_handle

sleep(2)
login_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
#login_button  = driver.find_element_by_xpath(("//*[text()='Log in']"))
login_button.click()

sleep(2)
fb_login = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

# Accept Cookies
accept_cookies = driver.find_element_by_xpath('//*[@id="u-648818393"]/div/div[2]/div/div/div[1]/button')
accept_cookies.click()

# Avoid mobile mode !
driver.maximize_window()
base_window = driver.window_handles[0]
print(driver.title)
accept_in = driver.find_element_by_xpath('//*[@id="u1917767827"]/div/div/div[1]/div/div[3]/span/div[2]/button')
accept_in.click()

# Enter to Facebook Dialog !
time.sleep(5)
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Waiting for Cookies!
time.sleep(5)
accept_cookies_facebook = driver.find_elements_by_css_selector("button")
accept_cookies_facebook[1].click()

for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle
driver.switch_to.window(login_page)

# Start to log in :
email_field = driver.find_element_by_id("email")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("pass")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)