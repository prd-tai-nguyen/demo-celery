
from celery import Celery
from time import sleep
import logging

broker_url = "amqp://rabbitmq:5672"
redis_url = "redis://redis:6379"
app = Celery('celery_worker', broker=broker_url, backend=redis_url)


logger = logging.getLogger(__name__)


@app.task(name="create_task")
def create_task(a, b):
    logger.info(a, b)
    return a + b


@app.task(name="test_task")
def test_task(a, b):
    return a * b


@app.task(name="create_error_task", autoretry_for=(Exception,),
          retry_kwargs={'max_retries': 5}, default_retry_delay=3)
def create_error_task(a, b):
    logger.info(a, b)
    raise Exception("Sorry, no numbers below zero")