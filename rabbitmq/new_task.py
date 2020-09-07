import random

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

msgs = [str(i) + ':' + str(random.randrange(1, 11)) for i in range(100)]

for msg in msgs:
    channel.basic_publish(exchange='', routing_key='task_queue', body=str(msg),
                          properties=pika.BasicProperties(delivery_mode=2, ))
    print(f' # 메세지 보냄: {msg}')

connection.close()
