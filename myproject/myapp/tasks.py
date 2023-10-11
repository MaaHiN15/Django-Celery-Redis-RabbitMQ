from celery import shared_task

# @shared_task(priority=0, queue='task')
# def h():
#     time.sleep(3)
#     return


# @shared_task(priority=5, queue='task')
# def m():
#     time.sleep(3)
#     return

# @shared_task(priority=10, queue='task')
# def l():
#     time.sleep(3)
#     return



# from celery import group

# # Here s() method stats signature of the task function
# task_group = group(h.s(), m.s(), l.s()) 

# # Here apply_async function runs the task function in async order
# task_group.apply_async()




# from celery import chain

# # Here s() method stats signature of the task function
# task_group = chain(h.s(), m.s(), l.s()) 

# # Here apply_async function runs the task function in async order
# task_group.apply_async()

# import time
# import logging
# @shared_task(queue='task')
# def f_func():
#     time.sleep(2)
#     logging.critical('Demo error')
#     return 'HELLO'


# @shared_task(queue='task')
# def s_func():
#     res = f_func.apply_async(args=[1,2],kwargs={'msg':'The sum is'})
#     if res.ready():
#         print('Task has completed')
#     else:
#         print('Task encountered error')

#     if res.successful():
#         print('Success')
#     else:
#         print('failed')
#     try:
#         task_result = res.get()
#         print('The result is ', task_result)
#     except Exception as e:
#         print('Exception: ', e)
    
# @shared_task(queue='task')
# def t_func():
#     result = f_func.apply_async()
#     print(result.task_id)
#     print(result.get())
#     return


# import time
# @shared_task(bind=True)
# def hello(self, a, b):
#     time.sleep(3)
#     self.update_state(state="PROGRESS", meta={'progress': 50})
#     time.sleep(3)
#     self.update_state(state="PROGRESS", meta={'progress': 90})
#     time.sleep(4)
#     return 'hello world: %i' % (a+b)

# @shared_task
# def on_raw_message(body):
#     print(body)




import time
@shared_task(queue='task')
def delay_task(d_sec):
    time.sleep(d_sec)
    return 'Hello'


@shared_task(queue='task')
def test(arg):
    print(arg)