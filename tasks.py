import os
from celery import Celery

BROKER=os.environ.get('CELERY_BROKER_URL', 'pyamqp://guest@localhost//')
BACKEND=os.environ.get('CELERY_RESULT_BACKEND', 'rpc://')

app = Celery('tasks', broker=BROKER, backend=BACKEND)
app.broker_connection_retry_on_startup = True

@app.task
def add(x, y):
    return x + y