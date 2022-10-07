import pika
import sys
import time
import random
import json
import requests

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.90.90'))
channel = connection.channel()

# URL = "http://192.168.90.90:15672/api/queues/%2F/jobs"
MINS_INTERVAL = 0.004


channel.queue_declare(queue='task_queue', durable=True)
try:
    while True :
            with open('events.json', 'r') as f:
                events = f.read().strip().split('\n')
            i = 0
            for event in events[1:-1]:
                print(i)
                if event[-1] == ",": 
                    e = "{" + event[:-1] + "}"
                else:                    
                    e = "{" + event + "}"

            data = json.loads(e)
            # message = ' '.join(sys.argv[1:]) or "Hello World!"
            print(data)
            channel.basic_publish(
                exchange='jobs',
                routing_key='jobs',
                body=data,
                properties=pika.BasicProperties(
                    delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                ))
            print(" [x] Sent %r" % data)
#        sleep(1)


finally:
    connection.close()
