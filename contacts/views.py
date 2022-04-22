from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm, EventForm, TechRequestForm

import os
# Create your views here.


# def contact(request):

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         print(request.POST)
#         if form.is_valid():
#             # print(request.POST['message'])
#             form.save()
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             email_subject = f"New Contact {email}: {form.cleaned_data['subject']}"
#             email_message = form.cleaned_data['message']
#             # send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)
#             messages.add_message(request, messages.SUCCESS, 'Request sent successfully. We will get back to you soon :)')
#             return redirect('index')
    
#         else:
#             return HttpResponse('None')

def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        
        if contact_form.is_valid():
            print('I am valid')
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, 'Request sent successfully. We will get back to you soon :)')
            return redirect('contact:contact')
        else:
            print("NOt valid form")
    context = {
        'contact_form': contact_form
    }
    return render(request, 'contacts/contact.html', context)

def event(request):

    event_form = EventForm()

    if request.method=='POST':

        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            messages.add_message(request, messages.SUCCESS, 'Event Registration Completed Successfully')
            return redirect('index')

        else:
            print(event_form.errors)
            # messages.add_message(request, messages.ERROR, 'Form not properly filled. Scroll down for error messages')
            # # return redirect(reverse('contact:event'))
            

    context = {
        'event_form': event_form
    }

    return render(request, 'contacts/event.html', context)


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