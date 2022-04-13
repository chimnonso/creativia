from django.shortcuts import render
from technologies.models import Technology
from contacts.forms import ContactForm

# Create your views here.

def index(request):
    techs = Technology.objects.all()[:3]

    context = {
        'techs': techs
    }

    return render(request, 'core/index.html', context)

