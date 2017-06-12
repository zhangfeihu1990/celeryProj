broker_url = 'pyamqp://'
backend = 'redis://localhost'
timezone = 'Europe/London'
enable_utc = True
beat_schedule = {
    'add-every-5-seconds':{
         'task':'task.add',
         'schedule':5.0,
         'args':(16,16)
     },
}

