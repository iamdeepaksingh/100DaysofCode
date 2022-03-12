# Author: Deepak Kumar Singh
# Descr: Selenium Web Driver basics.
# Date Created: 27/02/2022
# Date Modified: 27/02/2022

# Good read https://selenium-python.readthedocs.io/locating-elements.html

from selenium import webdriver

CHROME_DRIVER_PATH = "/Users/deepaksingh/Documents/Softwares/ChromeDriver/chromedriver"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://www.python.org/")
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

for time in event_times:
    print(time.text)

for name in event_names:
    print(name.text)

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time" : event_times[n].text,
        "name" : event_names[n].text
    }

print(events)
#driver.close()
driver.quit()

