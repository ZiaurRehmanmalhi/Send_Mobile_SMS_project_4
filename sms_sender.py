import os
from twilio.rest import Client

os.environ['TWILIO_ACCOUNT_SID'] = 'ACd0b87ed276c99e871e7fd12b49ecbe21'
os.environ['TWILIO_AUTH_TOKEN'] = '1e71598b78b44bd441c82fa6277e2d5f'

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

body = input("Please enter the SMS content: ")
to_number = input("Please enter the recipient phone number: ")

message = client.messages.create(
    body=body,
    from_='+16073502900',
    to=to_number
)
print(message.sid)
