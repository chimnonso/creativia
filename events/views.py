from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EventForm
from .models import Event
from django.conf import settings
import mimetypes
from django.http.response import HttpResponse
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


def download_file(request):
    events = Event.objects.all()
    BASE_DIR = settings.BASE_DIR
    file_name = 'email_list.txt'
    file_path = str(BASE_DIR) + f'/my_files/{file_name}'
    write_to_file(file_path, events)
    path = open(file_path, 'r')
    mime_type = mimetypes.guess_type(file_path)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = f"attachment; filename={file_name}"

    return response


def write_to_file(dir, events):
    with open(dir, 'w') as writer:
        for event in events:
            writer.write(event.email)
            writer.write(' ')

    return
