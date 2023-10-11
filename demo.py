# import app,time


# # On message
# # Celery supports catching all states changes by setting on_message callback.

# # For example for long-running tasks to send task progress you can do something like this:

# @app.task(bind=True)
# def hello(self, a, b):
#     time.sleep(1)
#     self.update_state(state="PROGRESS", meta={'progress': 50})
#     time.sleep(1)
#     self.update_state(state="PROGRESS", meta={'progress': 90})
#     time.sleep(1)
#     return 'hello world: %i' % (a+b)
# def on_raw_message(body):
#     print(body)

# a, b = 1, 1
# r = hello.apply_async(args=(a, b))
# print(r.get(on_message=on_raw_message, propagate=False))
# # Will generate output like this:

# {'task_id': '5660d3a3-92b8-40df-8ccc-33a5d1d680d7',
#  'result': {'progress': 50},
#  'children': [],
#  'status': 'PROGRESS',
#  'traceback': None}
# {'task_id': '5660d3a3-92b8-40df-8ccc-33a5d1d680d7',
#  'result': {'progress': 90},
#  'children': [],
#  'status': 'PROGRESS',
#  'traceback': None}
# {'task_id': '5660d3a3-92b8-40df-8ccc-33a5d1d680d7',
#  'result': 'hello world: 10',
#  'children': [],
#  'status': 'SUCCESS',
#  'traceback': None}
# # hello world: 10
# add = ''
# # The expires argument defines an optional expiry time, either as seconds after task publish, or a specific date and time using datetime:

# # Task expires after one minute from now.
# add.apply_async((10, 10), expires=60)

# # Also supports datetime
# from datetime import datetime, timedelta
# add.apply_async((10, 10), kwargs, expires=datetime.now() + timedelta(days=1))


# add.apply_async((2, 2), retry=True, retry_policy={
#     'max_retries': 3,
#     'interval_start': 0,
#     'interval_step': 0.2,
#     'interval_max': 0.2,
#     'retry_errors': None,
# })



