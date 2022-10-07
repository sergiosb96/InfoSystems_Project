import pika
import json
import sys
import time
import random
import requests

# Connect to RabbitMQ and create channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.90.90'))
channel = connection.channel()

# Declare and listen queue
channel.queue_declare(queue="jobs", durable=True)
URL = "http://192.168.90.90:15672/api/queues/%2f/jobs"
MINS_INTERVAL = 0.004

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    # read all simulation data
    print("Simulation completed.")
    with open('events.json', 'r') as f:
        events = f.read().strip().split('\n')
        print("Simulation completed.")

    # for every event
    for event in events[1:-1]:
        # set it to the right format in order to be able to convert it to json
        if event[-1] == ',': 
            e = '{' + event[:-1] + '}'
        else:                    
            e = '{' + event + '}'
        # json.loads creates a dict if string is valid
        data = json.loads(e)
        # get the response and print it
        r = requests.post(url = URL, json = data)
        print("Response text is:", r.text)
        
        time.sleep(60 * MINS_INTERVAL)
    
    print("Simulation completed.")

# Listen and receive data from queue
channel.basic_consume(queue='jobs', on_message_callback=callback)
channel.start_consuming()