import json 
import pika

from django.core.mail import send_mail
from time import sleep

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost',
                            credentials=pika.PlainCredentials('guest', 'guest')
                            ))

channel = connection.channel()

channel.queue_declare(queue='mail_queue', durable=True)


def callback(ch, method, properties, body):
    task_message = json.loads(body)
    sleep(10)
    try:
        send_mail(
            'Suggestion',
            f'Name: {task_message["name"]}\nEmail: {task_message["email"]}\nSuggestion: {task_message["suggestion"]}',
            'your_email@example.com',  # Replace with the sender's email address
            [task_message["email"]],    # Replace with the recipient's email address
            fail_silently=False,
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        # Handle the exception as per your application's requirements
    
def run():
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='mail_queue', on_message_callback=callback)
    channel.start_consuming()
    
    
