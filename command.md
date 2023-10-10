from myapp.tasks import h,l,m
from celery import group
g = group(h.s(), l.s(), m.s())
g.apply_async()



print(r.get(on_message=on_raw_message, propagate=False))