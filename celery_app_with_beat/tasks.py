import logging

from celery_app_with_beat.celery_app import celery

logger = logging.getLogger(__name__)

@celery.task
def scheduled_task_1():
    logger.info("This is task #1")

@celery.task
def scheduled_task_2():
    logger.info("This is task #2")

@celery.task
def scheduled_task_3():
    logger.info("This is task #3")
