# Author: Deepak Kumar Singh
# Description: API calls to get stock prices of Tesla.
# Date Created: 02/02/2022
# Date Modified: 03/02/2022

import requests
import os
import pandas as pd

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API = os.environ.get ("ALPHA_ADVANTAGE_API")
NEWS_API = os.environ.get("NEWS_API")
count = 0

Stock_Params ={
    "function": "TIME_SERIES_DAILY",
     "symbol": STOCK,
     "outputsize": "compact",
     "apikey": STOCK_API

}


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

response = requests.get(url=STOCK_ENDPOINT, params=Stock_Params)
response.raise_for_status()

data = response.json()

df = pd.DataFrame.from_dict(data)
#print(df)

data_daily = data["Time Series (Daily)"]
data_list = [v for (k,v) in data_daily.items()]
print(data_list[0])
new_dict = {}
for (k,v) in data_daily.items():
    if count < 2:
        new_dict[k] = v
        count += 1
#print(new_dict)

new_dict2 = {}
t = []
for (m,n) in new_dict.items():
    new_dict2[m] = n["4. close"]
    t.append(float(n["4. close"]))

print(new_dict2)

diff = [t[i+1]-t[i] for i in range(len(t)-1)]
print(diff)

val_5percent = (t[0] * 5)/100
print(val_5percent)


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

NEWS_PARAM = {
    "q": "COMPANY_NAME",
    "from": "2022-02-03",
    "sortBy": "popularity",
    "apiKey": "NEWS_API"


}

#response1 = requests.get(url="https://newsapi.org/v2/everything", params=NEWS_PARAM)
#response1.raise_for_status()

#data1 = response1.json()
#print(data)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

url = ('https://newsapi.org/v2/everything?'
       'q=Tesla&'
       'from=2022-02-03&'
       'sortBy=popularity&'
       'apiKey=NEWS_API')


response1 = requests.get(url)


data1 = response1.json()

news_data = data1["articles"][0:3]
#print(news_data)

for i in news_data:
    print(i["title"])
    print(i["description"])
    print("\n")

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

