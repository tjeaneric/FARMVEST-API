web: gunicorn FARMVESTNG_API.wsgi --log-level debug

celeryworker: celery worker -A celeryconfig --loglevel INFO


celerybeatworker: celery -A celeryconfig beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
