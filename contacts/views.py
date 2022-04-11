from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm, EventForm, TechRequestForm

import os
# Create your views here.


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(request.POST)
        if form.is_valid():
            # print(request.POST['message'])
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            email_subject = f"New Contact {email}: {form.cleaned_data['subject']}"
            email_message = form.cleaned_data['message']
            # send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)
            messages.add_message(request, messages.SUCCESS, 'Request sent successfully. We will get back to you soon :)')
            return redirect('index')
    
        else:
            return HttpResponse('None')

def event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            email_subject = f"{email}: {form.cleaned_data['subject']}"
            message = f"{first_name} registerd for an event"
            # send_mail(email_subject, message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)
            messages.add_message(request, messages.SUCCESS, 'Event Registration Completed Successfully')
            return redirect('index')

        else:
            return HttpResponse('not Valid')
    return HttpResponse('Hello Worlfd')


def tech_request(request):

    if request.method == 'POST':
        form = TechRequestForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            tech = form.cleaned_data['tech_title']
            # tech_id = form.cleaned_data['tech_id']
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            email_subject = f"Technology Request for {tech}: {email}"
            message = f"{first_name}: {email}"
            # send_mail(email_subject, message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)
            messages.add_message(request, messages.SUCCESS, 'Request sent successfully. We will get back to you soon :)')
            return redirect('technology:technologies')

        else:
            return HttpResponse('not Valid')
    return HttpResponse('Hello Worlfd')