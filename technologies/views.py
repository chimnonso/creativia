from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Technology
from contacts.forms import TechRequestForm

# Create your views here.


def get_technologies(request):

    techs = Technology.objects.all()
    context = {
        'techs': techs
    }
    return render(request, 'technologies/technologies.html', context)


def details(request, tech_id):

    tech = get_object_or_404(Technology, pk=tech_id)
    related_techs = Technology.objects.exclude(pk=tech_id)[:2]
    tech_request_form = TechRequestForm()

    if request.method == 'POST':
        
        tech_request_form = TechRequestForm(request.POST)
        print(tech_request_form.errors)
        tech_request_form.save()
        messages.add_message(request, messages.SUCCESS, 'Request Sent Successfully.')
        return redirect('technology:technologies')

    context = {
        'tech': tech,
        'related_techs': related_techs,
        'tech_request_form': tech_request_form
    }

    return render(request, 'technologies/details.html', context)


