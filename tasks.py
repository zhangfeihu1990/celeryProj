from celery import Celery
from pymongo import MongoClient
#app = Celery('tasks',backend='rpc://', broker='pyamqp://')
app = Celery('tasks')
app.config_from_object('celeryconfig')
client = MongoClient('localhost',27017)
db = client['celerydb']

@app.task()
def add(x, y):
  print "starting add ..."
  r = x + y
  content = {"result":r}
  re = db.result
  re.insert_one(content)
  
  return x + y

@app.task
def multiply(x, y):
  return x*y
