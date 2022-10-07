import pika
import sys
from time import sleep
import random
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
try:
    while True :
        if ( random.randint(0,30) > 0 ):
            message = ' '.join(sys.argv[1:]) or "Hello World!"
            channel.basic_publish(
                exchange='',
                routing_key='task_queue',
                body=message,
                properties=pika.BasicProperties(
                    delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                ))
            print(" [x] Sent %r" % message)
        sleep(1)


finally:
    connection.close()