from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.mail import send_mail, send_mass_mail

def home(request):
    subject ="Test_Mail from Django Server"
    message = "This is a Demo-test mail"
    from_email ="priyapardeshi610@gmail.com"
    recipient_list =[ "priyapardeshi610@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)

    return HttpResponse("pls check ur mail.....")    