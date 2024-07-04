from time import sleep
from django.core.mail import send_mail
from celery import shared_task

@shared_task()
def send_email_task(name, email, suggestion):
    sleep(10)
    send_mail(
        'Suggestion',
        f'Name: {name}\nEmail: {email}\nSuggestion: {suggestion}',
        'your_email@example.com',  # Replace with the sender's email address
        [email],    # Replace with the recipient's email address
        fail_silently=False,
    )