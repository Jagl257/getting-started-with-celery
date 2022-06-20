import time
from simple_celery_app.celery_app import celery


@celery.task
def add(x: int,y: int) -> int:
    time.sleep(5)
    return x + y

@celery.task
def multiply(x: int, y: int) -> int:
    time.sleep(5)
    return x * y
