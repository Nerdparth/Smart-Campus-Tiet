from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Twilio Client
client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))

# Send a test SMS
message = client.messages.create(
    body="This is a test message from Twilio.",
    from_=os.getenv('TWILIO_PHONE_NUMBER'),
    to=os.getenv('AUTHORITY_PHONE_NUMBER')
)

print(f"Message sent with SID: {message.sid}")
