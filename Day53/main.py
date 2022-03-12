# Author: Deepak Kumar Singh
# Descr: Capstone project - Search rental properties and document.
# Date Created: 05/03/2022
# Date Modified: 05/03/2022

from bs4 import BeautifulSoup
import requests
import lxml
from pprint import  pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from time import sleep

chrome_driver_path = "/Users/deepaksingh/Documents/Softwares/ChromeDriver/chromedriver"
PROPERTY_URL = "https://www.realo.be/en/search/flat/for-rent/ghent-9000?bedroomsMin=0&bedroomsMax=2"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLScmImHFg9S3Dp5fVN4ItwJo9Ehp7KNki0t8NBLRkPwL4C4nBA/viewform?usp=sf_link"
headers = {'Accept-Language' : "en-GB,en-US;q=0.9,en;q=0.8",
            'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"}
COMPANY = "https://www.realo.be/"

response = requests.get(PROPERTY_URL, headers=headers)
data = response.text

soup = BeautifulSoup(data, "lxml")
#pprint(soup.prettify())
val1 = soup.find(class_="list-unstyled grid component-estate-list-grid__list")
#val2 = val1.findAll(class_="col component-estate-list-grid-item ")
#val3 = val2[0].find('a')
#val4 = val3.get_text()
#print(val4)


all_link_elements = soup.select(".body a")
#print(all_link_elements)
all_links = []

for link in all_link_elements:
    href = link["href"][1:]
    #print(href)
    if "http" not in href:
        all_links.append(f"{COMPANY}{href}")
    else:
        all_links.append(href)

for i in all_links:
    #print(i)
    pass

all_address_elements = soup.find_all("div", {"class": "address truncate"})
#print(all_address_elements)

all_addresses = []
for address in all_address_elements:
    #print(address.get_text())
    all_addresses.append(address.get_text())

all_price_elements = soup.find_all("div", {"class": "col label label-price"})
#print(all_price_elements)

all_prices = []
for price in all_price_elements:
    #print(price.get_text())
    all_prices.append(price.get_text().split("/")[0].replace("€", "").strip())



# Create Spreadsheet using Google Form

driver = webdriver.Chrome(executable_path=chrome_driver_path)

for n in range(len(all_links)):

    driver.get(FORM)
    #driver.maximize_window()

    sleep(2)
    address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')

    price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    print(all_prices[n])
    submit_button.click()
    sleep(5)

sleep(5)
driver.quit()