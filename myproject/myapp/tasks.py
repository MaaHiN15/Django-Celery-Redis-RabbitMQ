from celery import shared_task
import time


@shared_task
def first_task():
    time.sleep(3)
    return

@shared_task
def second_task():
    return


@shared_task(priority=0, queue='high_priority')
def h():
    return


@shared_task(priority=5, queue='medium_priority')
def m():
    return

@shared_task(priority=10, queue='low_priority')
def l():
    return