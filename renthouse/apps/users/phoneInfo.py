#短信模块
from twilio.rest import Client

account_sid = 'AC911b2fe3b08e3dc682df65851bde1b0a'
auth_token ='fc311f7ef2de07ceeb12422935ebf95d'
client = Client(account_sid,auth_token)

message = client.messages.create(
    from_='+12109780784',
    body='hello world',
    to='+8613824464121'
)
print(message.sid)
