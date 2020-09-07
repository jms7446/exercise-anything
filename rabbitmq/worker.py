import time
from datetime import datetime

from pika import BlockingConnection, ConnectionParameters


def main():
    connection = BlockingConnection(ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    print(' # 메세제를 기다림')

    def callback(ch, method, properties, body):
        msg = str(body, 'utf8').split(':')
        print(f' # {datetime.now()} {msg[0]} 메시지 받음\n {body}')
        time.sleep(int(msg[1]) / 10)
        print(f' # {datetime.now} 완료.')

        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume('task_queue', callback)

    channel.start_consuming()


if __name__ == '__main__':
    main()
