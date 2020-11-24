import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

host = "smtp.gmail.com"
port = 465
password = ""


class Emailing:
    @staticmethod
    def send_test(email, url):
        context = ssl.create_default_context()
        message = MIMEMultipart("alternative")
        message["Subject"] = "Запись на мероприятие Adidas"
        message["From"] = "vvkovyazin@miem.hse.ru"
        message["To"] = email
        text = f"""Привет. Ты был успешно записаны на мероприятие Adidas Runners!"""
        html = f"""\
                <html>
                <body>
                    <p>Привет,<br>
                    Ты был успешно записаны на мероприятие Adidas Runners!<br>
                    <a href="{url}">Ссылка на мероприятие</a>
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
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login("vvkovyazin@miem.hse.ru", password)
            server.sendmail("vvkovyazin@miem.hse.ru", email,
                            message.as_string())


if __name__ == "__main__":
    Emailing.send_test("adidasscript@yandex.ru", "https://www.adidas.ru/adidasrunners/community/moscow/event/ar-atrium-142?cm_sp=RUNNING_HUB-_-LOGGEDIN-_-AR-ATRIUM-142")