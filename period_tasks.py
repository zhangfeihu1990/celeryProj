from celery import Celery
app = Celery('period_tasks')
app.config_from_object('celeryconfig')
@app.task()
def add(x,y):
  return 'hello',x + y


