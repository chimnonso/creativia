from django.forms import ModelForm
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['contact_date']
