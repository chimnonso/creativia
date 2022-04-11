from django.shortcuts import render, get_object_or_404
from .models import Technology

# Create your views here.


def get_technologies(request):

    techs = Technology.objects.all()
    context = {
        'techs': techs
    }
    return render(request, 'technologies/technologies.html', context)


def details(request, tech_id):

    tech = get_object_or_404(Technology, pk=tech_id)
    related_techs = Technology.objects.exclude(pk=tech_id)

    context = {
        'tech': tech,
        'related_techs': related_techs
    }

    return render(request, 'technologies/details.html', context)