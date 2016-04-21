# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACdc5f132a3c49700934481addd5ce1659"
auth_token  = "{{ auth_token }}"
client = TwilioRestClient(account_sid, auth_token)

# A list of short_code objects with the properties described above
short_codes = client.sms.short_codes.list()