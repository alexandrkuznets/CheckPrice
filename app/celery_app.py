from celery import Celery

from app.config import settings

app = Celery("tasks", broker=f"amqp://admin:{settings.rabbitmq_pass}@localhost:5672//")

app.autodiscover_tasks(["app.tasks"])