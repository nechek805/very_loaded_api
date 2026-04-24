from src.celery_app.celery_main import celery_app
from email.message import EmailMessage


@celery_app.task(name="tasks.send_task_created_message")
def send_task_created_message(task_id: int, title: str) -> str:
    return f"Task {task_id}, {title} processed"
