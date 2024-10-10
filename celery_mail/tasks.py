from datetime import timedelta

from celery import shared_task
from django.core.mail import get_connection
from django.utils import timezone

from celery_mail.models import EmailMessage


@shared_task(bind=True)
def send_mail(context, email_message_id):
    email_message = EmailMessage.objects.get(id=email_message_id)
    if email_message.sent:
        return
    success = get_connection().send_messages([email_message.unpickled], immediate=True)
    if success:
        email_message.sent = True
        email_message.save(update_fields=["sent"])


@shared_task
def send_unsent_mails():
    """Periodically send unsent mails."""
    for email_message in EmailMessage.objects.filter(sent=False):
        send_mail.delay(email_message.id)


@shared_task
def vacuum():
    """Delete old mails."""
    start = timezone.now() - timedelta(days=14)
    EmailMessage.objects.filter(created__lte=start).delete()
