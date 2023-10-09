from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

celery = Celery('myproject')
celery.config_from_object('django.conf:settings', namespace='CELERY')

celery.conf.task_default_rate_limit = '1/m'

celery.autodiscover_tasks()