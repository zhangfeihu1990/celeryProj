from celery import Celery
from pymongo import MongoClient
app = Celery('tasks',backend='rpc://', broker='pyamqp://')

client = MongoClient('localhost',27017)
db = client['celerydb']

@app.task()
def add(x, y):
  r = x + y
  content = {"result":r}
  re = db.result
  re.insert_one(content)
  
  return x + y

@app.task
def multiply(x, y):
  return x*y
