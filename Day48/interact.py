# Author: Deepak Kumar Singh
# Descr: Selenium Web Driver Automation an Interaction.
# Date Created: 27/02/2022
# Date Modified: 27/02/2022

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "/Users/deepaksingh/Documents/Softwares/ChromeDriver/chromedriver"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)
content = driver.find_element_by_css_selector("#articlecount a")
#content.click()

all_portals = driver.find_element_by_link_text("All portals")
#all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Ukraine")
search.send_keys(Keys.ENTER)


#driver.quit()