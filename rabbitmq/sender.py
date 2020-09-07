import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(10):
    channel.basic_publish(exchange='', routing_key='hello', body=f'안녕하세요 {i}')

print('# 메세지를 보냄')

connection.close()
