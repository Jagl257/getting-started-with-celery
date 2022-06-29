from celery_app_with_beat.beat_conf import beat_conf

broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/0'
task_serializer = 'json'
result_serializer = 'json'
enable_utc = True
imports = (
        "celery_app_with_beat.tasks",
)

beat_schedule = beat_conf
