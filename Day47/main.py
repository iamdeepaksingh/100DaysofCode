# Author: Deepak Kumar Singh
# Descr: Price checker using Beautiful Soup. Use http://myhttpheader.com/ for header information.
# Date Created: 26/02/2022
# Date Modified: 26/02/2022

#Gmail: smtp.gmail.com
#Hotmail: smtp.live.com
#Outlook: outlook.office365.com
#Yahoo: smtp.mail.yahoo.com

from pprint import pprint
from bs4 import BeautifulSoup
import lxml
import requests
import smtplib
YOUR_SMTP_ADDRESS ="smtp.gmail.com"
YOUR_EMAIL = "youramail@gmail.com"
YOUR_PASSWORD = "yourpassword"

BUY_PRICE = 3000.00
headers = {'Accept-Language' : "en-GB,en-US;q=0.9,en;q=0.8",
            'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"}

url = "https://www.amazon.com/dp/B09JQMW44C/ref=fs_a_mbt2_us4"
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "lxml")
#pprint(soup.prettify())

title = soup.find(id="productTitle").get_text().strip()
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
remove_price_comma = price_without_currency.replace(",", "")
#print(remove_price_comma)
price_as_float = float(remove_price_comma)
print(price_as_float)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"
    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        print(message)
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        print("chk")
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
        print(message)