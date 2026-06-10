from time import sleep
from celery import Celery
from random import randint

from app.celery_app import app
from app.client.wb import get_wb_card_data
from app.services.products_sync import get_products, update_product


@app.task()
def request_on_wb():
    products = get_products()
    for product in products:
        sec = randint(1, 5)
        sleep(sec)
        price = get_wb_card_data(product.product_url)
        if price < product.last_price:
            print("ОТправили смс")
        elif price <= product.desired_price:
            print("ОТправили смс")

        update_product(article=product.product_url, new_price=price)



@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs):
    sender.add_periodic_task(30.0, request_on_wb.s(), name='add every 1 hour')
