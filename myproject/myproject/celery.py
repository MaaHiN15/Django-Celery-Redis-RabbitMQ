from celery import Celery
import os
from kombu import Queue, Exchange

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

celery = Celery('myproject')
celery.config_from_object('django.conf:settings', namespace='CELERY')

# celery.conf.task_default_rate_limit = '1/m'

celery.conf.task_queues = [
    Queue('task', Exchange('task'), routing_key = 'task', queue_arguments = { 'x-max-priority' : 10 }),
]

celery.conf.task_acts_late = True
celery.conf.worker_prefetch_multiplier = 1
celery.conf.worker_concurrency = 1
celery.conf.task_default_priority = 1

celery.autodiscover_tasks()