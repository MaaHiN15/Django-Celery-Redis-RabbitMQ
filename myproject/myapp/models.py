from django.db import models

# Several kinds of events trigger signals, you can connect to these signals to perform actions as they trigger.

# Example connecting to the after_task_publish signal:

from celery.signals import after_task_publish

@after_task_publish.connect
def task_sent_handler(sender=None, headers=None, body=None, **kwargs):
    # information about task are located in headers for task messages
    # using the task protocol version 2.
    info = headers if 'task' in headers else body
    print('after_task_publish for task id {info[id]}'.format(
        info=info,
    ))
# Some signals also have a sender you can filter by. For example the after_task_publish signal uses the task name as a sender, so by providing the sender argument to connect you can connect your handler to be called every time a task with name “proj.tasks.add” is published:

@after_task_publish.connect(sender='proj.tasks.add')
def task_sent_handler(sender=None, headers=None, body=None, **kwargs):
    # information about task are located in headers for task messages
    # using the task protocol version 2.
    info = headers if 'task' in headers else body
    print('after_task_publish for task id {info[id]}'.format(
        info=info,
    ))
