from time import sleep
from celery import Celery
from random import randint

from app.celery_app import app
from app.client.wb import get_wb_product_data
from app.services.products_sync import get_products, update_product
from app.services.email import send_email
from app.celery_app import logger


@app.task()
def request_on_wb():
    products = get_products()
    logger.info("Запуск задачи: request_on_wb")
    for product in products:
        sec = randint(1, 5)
        sleep(sec)
        price, product_name = get_wb_product_data(product.product_url)
        if price == 0:
            continue
        if price != product.last_price:
            if price <= product.desired_price or price < product.last_price:
                send_email(product_name=product_name, price=price, send_to=product.email)

            update_product(article=product.product_url, new_price=price)


@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs):
    sender.add_periodic_task(3600.0, request_on_wb.s(), name='add every 1 hour')
