# Author: Deepak Kumar Singh
# Descr: Form fill up test using Selenium Web Driver.
# Date Created: 27/02/2022
# Date Modified: 27/02/2022

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

FIRST_NAME = "Deepak"
LAST_NAME ="Singh"
EMAIL = "dummyemail@example.com"

CHROME_DRIVER_PATH = "/Users/deepaksingh/Documents/Softwares/ChromeDriver/chromedriver"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url)

fname = driver.find_element_by_name("fName")
fname.send_keys(FIRST_NAME)

lname  = driver.find_element_by_name("lName")
lname.send_keys(LAST_NAME)

email = driver.find_element_by_name("email")
email.send_keys(EMAIL)

signup = driver.find_element_by_css_selector("form button")
signup.click()



