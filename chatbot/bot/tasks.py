from celery import shared_task
import logging
from .models import SupportTicket

@shared_task
def raise_support_ticket(user_query):
    print("Running celery")
    #Replace with your DB or email logic
    logging.warning(f"Support ticket raised for query: {user_query}")
    
    #create a model instance here to log the ticket
    SupportTicket.objects.create(support_ticket = user_query)