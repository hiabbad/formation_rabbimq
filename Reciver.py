import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

def consume_messages_from_queue(queue='my_queue'):
    # Connexion au serveur RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    # S'assurer que la queue existe
    channel.queue_declare(queue=queue, durable=True)
    
    # Consommer les messages de la queue
    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
    
    print(f' [*] Waiting for messages in {queue}. To exit press CTRL+C')
    
    # Commencer à consommer
    channel.start_consuming()

if __name__ == "__main__":
    consume_messages_from_queue()
