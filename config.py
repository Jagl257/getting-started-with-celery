class Config():

    SECRET_KEY = "JUSTANOTHERSECRETKEY"

    #Celery

    broker_url = 'redis://localhost:6379/0'
    result_backend = 'redis://localhost:6379/0'
    task_serializer = 'json'
    result_serializer = 'json'
    accept_content = ['json']
    timezone = 'Europe/Oslo'
    enable_utc = True
    # imports = (
    #        "celery_app_with_routing.tasks",
    #
