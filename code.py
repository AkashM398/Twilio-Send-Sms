import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_num = os.environ['TWILIO_PHONE_NUMBER']
personal_num = os.environ['PERSONAL_PHONE_NUMBER']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello, World!",
                     from_= twilio_num,
                     to= personal_num
                 )

print(message.sid)