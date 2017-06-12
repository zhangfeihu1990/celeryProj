broker_url = 'pyamqp://'
backend = 'rpc://'
timezone = 'Europe/London'
enable_utc = True
beat_schedule = {
    'add-every-5-seconds':{
         'task':'tasks.add',
         'schedule':5.0,
         'args':(16,16)
     },
}

