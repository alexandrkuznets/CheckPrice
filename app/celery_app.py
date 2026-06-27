import logging
from celery import Celery
from celery.utils.log import get_task_logger

from app.config import settings

logger = get_task_logger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler("celery.log")
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)


app = Celery("tasks", broker=f"amqp://{settings.rabbitmq_default_user}:{settings.rabbitmq_default_pass.get_secret_value()}@localhost:5672//")


app.autodiscover_tasks(["app.tasks"])