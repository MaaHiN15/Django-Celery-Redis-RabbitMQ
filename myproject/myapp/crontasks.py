import json
from datetime import datetime, timedelta
from django_celery_beat.models import PeriodicTask, IntervalSchedule

# executes every 10 seconds.
schedule, created = IntervalSchedule.objects.get_or_create(
    every=10,
    period=IntervalSchedule.SECONDS,
)

PeriodicTask.objects.create(
    interval=schedule,                  # we created this above.
    name='Importing contacts',          # simply describes this periodic task.
    task='myapp.tasks.test',                # name of task.
    args=json.dumps(['HelloBoy!']),
    kwargs=json.dumps({
       'be_careful': True,
    }),
    expires=datetime.utcnow() + timedelta(seconds=30)
)