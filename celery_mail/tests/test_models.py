from django.core.mail import send_mail
from django.test import TestCase, override_settings

from celery_mail import models


class ModelsTestCase(TestCase):

    @override_settings(
        EMAIL_BACKEND="celery_mail.backends.CeleryLocMemBackend"
    )
    def test_email_message(self):
        send_mail(
            "Subject here",
            "Here is the message.",
            "from@example.com",
            ["to@example.com"],
            fail_silently=False,
        )
        self.assertEqual(models.EmailMessage.objects.all().count(), 1)
