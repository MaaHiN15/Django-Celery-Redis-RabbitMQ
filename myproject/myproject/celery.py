from celery import Celery
import os
from kombu import Queue, Exchange
from myapp.tasks import test

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


# from celery.schedules import crontab
# @celery.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(4.0, test.s('hello'), name='add every 10')

#     # Calls test('hello') every 30 seconds.
#     # It uses the same signature of previous task, an explicit name is
#     # defined to avoid this task replacing the previous one defined.
#     sender.add_periodic_task(30.0, test.s('hello'), name='add every 30')

#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)

#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         test.s('Happy Mondays!'),
#     )
