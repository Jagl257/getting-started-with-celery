import logging
import time
from celery_app_with_routing.tasks import notify_hello_world, say_hello_world

logger = logging.getLogger(__name__)

if __name__ == "__main__":

    while True:
        say_hello_world.delay()
        time.sleep(1)
