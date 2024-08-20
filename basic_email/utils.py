# utils.py (or any other Python file in your app)

from django.core.mail import send_mail
from django.conf import settings

def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,  # From email
        recipient_list,            # List of recipient emails
        fail_silently=False,
    )
