import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from settings import sender_address
from settings import sender_password
from settings import smtp_host
from settings import smtp_port


class Emailing:
    def __init__(self, to_email):
        self._to_email = to_email
        self._sender_address = sender_address
        self._host = smtp_host
        self._port = smtp_port

    def send_email(self, event_url):
        context = ssl.create_default_context()
        message = self._create_message(event_url)
        with smtplib.SMTP_SSL(self._host, self._port,
                              context=context) as server:
            server.login(sender_address, sender_password)
            server.sendmail(sender_address, self._to_email,
                            message.as_string())

    def _create_message(self, event_url):
        """
        docstring
        """
        message = MIMEMultipart("alternative")
        message["Subject"] = "Запись на мероприятие Adidas"
        message["From"] = sender_address
        message["To"] = self._to_email
        text = f"""Привет. Ты был успешно записаны на мероприятие Adidas Runners!"""
        html = f"""\
                <html>
                <body>
                    <p>Привет.<br>
                    Ты был успешно записаны на мероприятие Adidas Runners!<br>
                    <a href="{event_url}">Ссылка на мероприятие</a>
                    </p>
                </body>
                </html>
                """
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)
        return message