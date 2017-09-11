from smtplib import SMTP

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailClient:
    def __init__(self, host=None, port=None, username=None, password=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def send(self, message, recipients=None, sender=None, subject=None):
        conn = SMTP(host=self.host, port=self.port)
        conn.starttls()
        conn.login(self.username, self.password)

        email_message = MIMEMultipart()
        email_message['From'] = sender
        email_message['Subject'] = subject
        email_message.attach(MIMEText(message))

        for recipient in recipients:
            email_message['To'] = recipient
            conn.send_message(email_message)

        conn.quit()
