import pika

def send_message_to_exchange(message, exchange='my_exchange', routing_key='my_routing_key'):
    # Connexion au serveur RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    # Déclarer l'exchange
    channel.exchange_declare(exchange=exchange, exchange_type='direct', durable=True)
    
    # Publier le message à l'exchange
    channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message,
                          properties=pika.BasicProperties(delivery_mode=2))  # rendre le message persistant
    
    print(f" [x] Sent '{message}' to exchange '{exchange}' with routing key '{routing_key}'")
    
    # Fermer la connexion
    connection.close()

if __name__ == "__main__":
    message = 'Hello, RabbitMQ!'
    send_message_to_exchange(message)