from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EventForm
# Create your views here.

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
            messages.add_message(request, messages.ERROR, 'Form not properly filled. Scroll down for error messages')
            # # return redirect(reverse('contact:event'))
            

    context = {
        'event_form': event_form
    }

    return render(request, 'events/event.html', context)
