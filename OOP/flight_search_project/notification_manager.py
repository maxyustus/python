import smtplib
from twilio.rest import Client

TWILIO_SID = "AC0c2f213a430f976bf64b5867faa5d3f9"
TWILIO_AUTH_TOKEN = "3eff95dbc1ad704a82e1e36dd9a60187"
TWILIO_VIRTUAL_NUMBER = "+14077535057"
TWILIO_VERIFIED_NUMBER = "+79227536239"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "your_email"
MY_PASSWORD = "your_password"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )