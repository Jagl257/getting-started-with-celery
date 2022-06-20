from celery import Celery
from celery_app_with_routing import celeryconfig

celery = Celery('celery_app')

celery.config_from_object('celery_app_with_beat.celeryconfig')
