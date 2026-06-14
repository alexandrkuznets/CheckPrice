import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.config import settings
from app.celery_app import logger

smtp_server = settings.email_server
smtp_port = settings.email_port
email_address = settings.email_sender
email_password = settings.email_password


def send_email(product_name, price, send_to):
    message = MIMEMultipart()
    message["From"] = email_address
    message["To"] = send_to
    message["Subject"] = "Цена на ваш товар снизилась!!"
    body = f"Товар: {product_name}\n На данный момент его цена: {price} руб"
    message.attach(MIMEText(body, "plain"))

    try:
        logger.error(f"Отправка письма: пользователь {send_to}")
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(email_address, email_password)
        text = message.as_string()
        server.sendmail(email_address, send_to, text)
        server.quit()
    except Exception as ex:
        logger.error(f"Ошибка отправки письма: {ex}")