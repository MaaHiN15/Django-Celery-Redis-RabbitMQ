from celery import shared_task
import time


@shared_task
def first_task():
    time.sleep(3)
    return

@shared_task
def second_task(task_defualt_rate_limit='1/m'):
    return


@shared_task(priority=0, queue='high_priority')
def h():
    time.sleep(3)
    return


@shared_task(priority=5, queue='medium_priority')
def m():
    time.sleep(3)
    return

@shared_task(priority=10, queue='low_priority')
def l():
    time.sleep(3)
    return




from celery import group

# Here s() method stats signature of the task function
task_group = group(h.s(), m.s(), l.s()) 

# Here apply_async function runs the task function in async order
task_group.apply_async()




from celery import chain

# Here s() method stats signature of the task function
task_group = chain(h.s(), m.s(), l.s()) 

# Here apply_async function runs the task function in async order
task_group.apply_async()
