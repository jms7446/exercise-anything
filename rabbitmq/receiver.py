import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(f" # 메세지 받음: {body.decode('utf8')}")


channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' # 메세지를 기다립니다')

channel.start_consuming()
