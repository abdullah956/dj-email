from django.http import HttpResponse
from .utils import send_email

def send_test_email(request):
    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    recipient_list = ['abdullah.arshed.5421@gmail.com']
    
    send_email(subject, message, recipient_list)
    
    return HttpResponse('Email sent successfully!')