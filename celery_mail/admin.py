from django.contrib import admin

from celery_mail import models


class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ("id", "created", "sent")


admin.site.register(models.EmailMessage, EmailMessageAdmin)
