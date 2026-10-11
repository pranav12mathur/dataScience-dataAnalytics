import os
import smtplib
from email.mime.text import MIMEText

phone_number = "1234567890"
carrier_domain = "vtext.com"  
to_address = f"{phone_number}@{carrier_domain}"

msg = MIMEText("Server alert: Job #402 finished successfully.")
msg["From"] = os.environ["SENDER_EMAIL"]
msg["To"] = to_address

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(os.environ["SENDER_EMAIL"], os.environ["SMTP_APP_PASSWORD"])
    server.send_message(msg)