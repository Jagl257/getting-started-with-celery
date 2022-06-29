from celery import Celery

celery = Celery('celery_app')

celery.conf.update(
    broker_url='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/0',
    imports = (
        "simple_celery_app.tasks",
    ) 
)

