import request
from celery import shared_task
from django.core.mail import send_mail
from rapidfuzz import fuzz
from subscription.models import Address

@shared_task
def match_adderess_task(address):
    response = requests.get(
               'http://127.0.0.1:7000/api/v1/addresses/')
    addresses = [a_address['address'] for a_address in
                                         response.json()]
    top_score = 0



