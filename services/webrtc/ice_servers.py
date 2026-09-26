import os
from twilio.rest import Client

def get_ice_servers():
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    token = client.tokens.create()
    return token.ice_servers