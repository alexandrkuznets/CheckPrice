import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.config import settings

smtp_server = settings.email_server
smtp_port = settings.email_port
email_address = settings.email_sender
email_password = settings.email_password


def send_email(body, send_to):
    message = MIMEMultipart()
    message["From"] = email_address
    message["To"] = send_to
    message["Subject"] = "Тестовое письмо"
    # body = "Привет! Это тестовое письмо, отправленное с помощью Python."
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(email_address, email_password)

        text = message.as_string()
        server.sendmail(email_address, send_to, text)
        server.quit()
    except Exception as e:
        print(f"Произошла ошибка: {e}")