#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
         host = 'localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue')

message = ' '.join(sys.argv[1:]) or "hello world!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2,#make messege persistent
                      ))
print(" [x] Sent %r" % message)
connection.close()

