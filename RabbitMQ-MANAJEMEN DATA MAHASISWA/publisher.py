import pika

def send_message(message):
    # Konfigurasi RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Deklarasi pertukaran (exchange) dengan parameter durable=True
    channel.exchange_declare(exchange='logs_exchange', exchange_type='fanout', durable=True)

    # Kirim pesan
    channel.basic_publish(exchange='logs_exchange', routing_key='', body=message, properties=pika.BasicProperties(delivery_mode=2))
    print(" [x] Sent %r" % message)

    # Tutup koneksi
    connection.close()

# Kirim pesan
send_message('Hello, RabbitMQ!')
