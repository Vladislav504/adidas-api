import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from settings import sender_password
from settings import sender_address
from settings import smtp_host
from settings import smtp_port
from settings import ssl as is_ssl
from settings import tls
from settings import auth_required


class Emailing:
    def __init__(self, reciever_address):
        self._reciever_address = reciever_address
        self._sender_address = sender_address
        self._sender_password = sender_password
        self._host = smtp_host
        self._port = smtp_port
        self._server = smtplib.SMTP_SSL if is_ssl else smtplib.SMTP

    def send_email(self, event_url):
        if  self._reciever_address is None or \
            self._sender_address is None or \
            self._sender_password is None or \
            self._host is None or \
            self._port is None:
            return
        message = self._create_message(event_url)
        self._send_with_ssl(message) if is_ssl else self._send_unsafe(message)

    def _send_with_ssl(self, message):
        context = ssl.create_default_context()
        with self._server(self._host, self._port, context=context) as server:
            self._send(server, message)

    def _send_unsafe(self, message):
        with self._server(self._host, self._port) as server:
            self._send(server, message)

    def _send(self, server, message):
        self._starttls(server)
        self._login(server)
        server.sendmail(self._sender_address, self._reciever_address,
                        message.as_string())

    def _starttls(self, server):
        if tls:
            server.starttls()

    def _login(self, server):
        if auth_required:
            server.login(self._sender_address, self._sender_password)

    def _create_message(self, event_url):
        """
        docstring
        """
        message = MIMEMultipart("alternative")
        message["Subject"] = "Запись на мероприятие Adidas"
        message["From"] = sender_address
        message["To"] = self._reciever_address
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