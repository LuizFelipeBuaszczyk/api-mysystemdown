from celery import shared_task
from infra.email.email import Email, EmailType

@shared_task
def send_email(subject, to_email, email_type_value: EmailType, context: dict):
    Email.send_email(subject, to_email, email_type_value, context)