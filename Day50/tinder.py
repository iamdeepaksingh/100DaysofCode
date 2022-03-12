import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

# https://this-person-does-not-exist.com/en

FB_EMAIL = YOUR FACEBOOK LOGIN EMAIL
FB_PASSWORD = YOUR FACEBOOK PASSWORD

chrome_driver_path = "/Users/deepaksingh/Documents/Softwares/ChromeDriver/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)



# url of main page.
URL = "https://tinder.com/app/recs"
EMAIL_ID = 'YOUR EMAIL'
PASSWORD = 'YOUR PASSWORD'

# driver path (driver location in folders)
driver_path = Service(chrome_driver_path)
# set driver object to drive browser
driver = webdriver.Chrome(service=driver_path)
driver.maximize_window()


# make driver to go to preferred url
driver.get(URL)
time.sleep(5)
# save main window id, will tell you later on about its usage.
main_window = driver.current_window_handle

# click accept to terms on first page of tinder.
allow_cookies = driver.find_element(By.XPATH, '//*[@id="c-1420294622"]/div/div[2]/div/div/div[1]/button').click()
# click on log in button
click_log_in = driver.find_element(By.LINK_TEXT, 'Log in').click()
time.sleep(3)
try:
    # sometimes it shows facebook log in only after clicking on more options, that's why i used exception handling.
    click_more_options = driver.find_element(By.XPATH, '//*[@id="c1146291598"]/div/div/div[1]/div/div[3]/'
                                                       'span/button').click()
except NoSuchElementException:
    pass
time.sleep(5)
try:
    # normally click on log in with facebook
    log_in_facebook = driver.find_element(By.XPATH, '//*[@id="c1146291598"]/div/div/div[1]/div/div[3]/span/div'
                                                    '[2]/button/span[2]').click()

except NoSuchElementException:
    # sometimes before clicking on log in with facebook, it shows account recovery pop up. so we need to tackle that.
    recovery_cancel = driver.find_element(By.XPATH, '//*[@id="c1146291598"]/div/div/div[2]/button').click()
    time.sleep(2)
    # again click on log in
    click_log_in = driver.find_element(By.LINK_TEXT, 'Log in').click()
    time.sleep(2)
    log_in_facebook = driver.find_element(By.XPATH, '//*[@id="c1146291598"]/div/div/div[1]/div/div[3]/span/div'
                                                    '[2]/button/span[2]').click()

time.sleep(5)
# when we click on Facebook log in, our browser automatically opens new tab, but our driver is still on first tab
# so if we want to perform any operation in new window  it will give us error, so we need to change driver from
# main window to current window.
for tab in driver.window_handles:
    if tab != main_window:
        driver.switch_to.window(tab)
        # to verify that driver has switched to new window
        print(driver.title)
time.sleep(3)
add_email = driver.find_element(By.XPATH, '//*[@id="email"]')
add_email.send_keys(EMAIL_ID)
add_password = driver.find_element(By.XPATH, '//*[@id="pass"]')
add_password.send_keys(PASSWORD)
add_password.send_keys(Keys.ENTER)
time.sleep(20)
# make driver to return to its original window (main tab of browser), so that it can perform functions over there.
driver.switch_to.window(main_window)
time.sleep(2)
# to verify that the driver has switched back to main window
print(driver.title)
# allow location
allow_location = driver.find_element(By.XPATH, '//*[@id="c1146291598"]/div/div/div/div/div[3]/button[1]/span').click()
time.sleep(2)
# disallow notification
disallow_notification = driver.find_element(By.XPATH, '//*[@id="c1146291598"]/div/div/div/div/div[3]/button'
                                                      '[2]/span').click()
time.sleep(20)
# create like button object
click_like_button = driver.find_element(By.XPATH,
                                        '//*[@id="c-1420294622"]/div/div[1]/div/main/div[1]/div/div/div[1]'
                                        '/div[1]/div/div[4]/div/div[4]/button')

for i in range(20):
    try:
        # like a profile only if it is loaded
        click_like_button.click()

    except ElementClickInterceptedException:
        try:
            # hide pop up (it's a match)
            hide_its_a_match = driver.find_element(By.XPATH, '//*[@id="c-1089923421"]/div/div/div[1]/div/div'
                                                             '[4]/button').click()
        except:
            # sometimes tinder shows (add to home screen pop up) so we need to click cancel
            add_tinder_home_screen = driver.find_element(By.XPATH,
                                                         '//*[@id="c1146291598"]/div/div/div[2]/button[2]/span').click()
        # wait for two seconds for any of the above two exceptions and then click like button
        time.sleep(2)
        click_like_button.click()

    except NoSuchElementException:
        # if profile is not loaded yet, then wait for 2 more sec
        time.sleep(3)
        click_like_button.click()

    time.sleep(7)
