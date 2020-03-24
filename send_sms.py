# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import pandas as pd 

import env
import message

# Your Account Sid and Auth Token from twilio.com/console
client = Client(env.ACCOUNT_SID, env.AUTH_TOKEN)

# df = pd.read_csv("data.csv") 

# def twilio_message(number):
#     message2send = client.messages \
#     .create(
#          body=message.PUBLIC_HEALTH_ALERT,
#          messaging_service_sid=env.MESSAGING_SERVICE_SID,
#         # to='+18492124834'
#         to=number
#      )

#     print(message2send.sid)



# df['telephoneNumber'] = '1' + df['telephoneNumber'].astype(str)

# df['telephoneNumber'].apply(twilio_message)

message2send = client.messages \
    .create(
        body=message.PUBLIC_HEALTH_ALERT,
        messaging_service_sid=env.MESSAGING_SERVICE_SID,
        to='18097897452'
    )

print(message2send.sid)