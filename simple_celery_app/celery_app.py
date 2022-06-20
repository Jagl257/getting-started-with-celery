from celery import Celery

celery = Celery('celery_app')

celery.conf.update(
    broker_url='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/0',
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
    imports = (
        "simple_celery_app.tasks",
    ) 
)

