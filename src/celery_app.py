from celery import Celery
import os

app = Celery(
    "very_loaded_api",
    broker=os.environ["CELERY_BROKER_URL"],
    backend=os.environ["CELERY_RESULT_BACKEND"],
)

app.autodiscover_tasks(["src"])