# Djangio Celery Mail

A dead simple method to send and keep track of mails from Django. Mails are automatically
retried should the mail server be unavailable.

## Installation

1. Install or add `django-celery-mail` to your Python path.

2. Add `celery_mail` to your `INSTALLED_APPS` setting.

3. Set `EMAIL_BACKEND` setting to `celery_mail.backens.CeleryFileBackend`.

4. Set `EMAIL_FILE_PATH` setting to `/tmp/app-messages`.

5. Optionally configure Celery to run periodic tasks `celery_mail.tasks.send_unsent_mails`
   and `celery_mail.tasks.vacuum`.

## Running

In development mode set the environment variable `CELERY_ALWAYS_EAGER=True`
to immediately execute the mail tasks.

In production start one or more separate Celery workers. Refer to the Celery documentation.

## Tests

Install:

    virtualenv ve
    ./ve/bin/pip install -r test_requirements.txt

Run:

    ./ve/bin/tox

## Settings

Django Celery Mail introduces no settings. The standard Django mail related settings are
respected.
