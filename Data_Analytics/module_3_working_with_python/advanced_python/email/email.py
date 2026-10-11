import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.environ["pranav12mathur@gmail.com"]
SENDER_PASSWORD = os.environ["SMTP_APP_PASSWORD"]
RECIPIENT_EMAIL = "pranav04mathur@gmail.com"
msg = MIMEMultipart("alternative")
msg["Subject"] = "System Notification"
msg["From"] = SENDER_EMAIL
msg["To"] = RECIPIENT_EMAIL

text_content = "Have you recieved my email"

msg.attach(MIMEText(text_content, "plain"))
msg.attach(MIMEText(html_content, "html"))

try:
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10) as server:
        server.ehlo()
        server.starttls()  # Encrypt session
        server.ehlo()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
except smtplib.SMTPException as exc:
    raise SystemExit(f"Email delivery failed: {exc}")