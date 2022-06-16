from celery import Celery

celery = Celery('celery_app', broker='redis://localhost:6379/0')
