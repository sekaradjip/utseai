import pika

def receive_messages():
    # Konfigurasi RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Deklarasi pertukaran (exchange) dengan parameter durable=True
    channel.exchange_declare(exchange='logs_exchange', exchange_type='fanout', durable=True)

    # Deklarasi antrean (queue)
    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue

    # Ikatan antrean ke pertukaran
    channel.queue_bind(exchange='logs_exchange', queue=queue_name)

    # Callback function untuk meng-handle pesan
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    # Mulai mengonsumsi pesan
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    # Mulai mengonsumsi pesan
    channel.start_consuming()

# Terima dan proses pesan
receive_messages()
