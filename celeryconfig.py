import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FARMVESTNG_API.settings")

app = Celery("FARMVESTNG_API")
app.config_from_object("django.conf:settings")

app.autodiscover_tasks()
