import os
from twilio.rest import Client

TWILIO_SID = "YOUR TWILIO SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
     def notify_by_sms(self, message):
        account_sid = TWILIO_SID
        auth_token = TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_='+18594847785',
            to='+32495776549'
        )
        print(message.sid)

