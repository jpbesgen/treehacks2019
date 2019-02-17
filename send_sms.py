# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from passwords import *
import datetime


# Your Account Sid and Auth Token from twilio.com/console
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_TOKEN
client = Client(account_sid, auth_token)

currentDT = datetime.datetime.now()
STOP_TIME = str(currentDT.strftime("%I:%M:%S %p"))

message = client.messages \
                .create(
                     body= "You are designated as " + USER_NAME + "'s emergency contact. \
                     They were stopped at " + STOP_TIME + " in " + STOP_LOCATION + ".",
                     from_='+18059792058',
                     to=EMERGENCY_CONTACT
                 )

print(message.sid)
