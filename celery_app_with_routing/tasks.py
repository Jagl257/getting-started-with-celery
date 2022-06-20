import logging
import time
from celery_app_with_routing.celery_app import celery

logger = logging.getLogger(__name__)

@celery.task(queue="priority")
def notify_hello_world():
    logger.info("NOTIFYING HELLO WORLD")

@celery.task
def say_hello_world():
    time.sleep(5)
    logger.info("Just saying Hello World")
