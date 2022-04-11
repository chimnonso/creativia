from django.forms import ModelForm
from .models import Contact, Event, TechRequest

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class TechRequestForm(ModelForm):
    class Meta:
        model = TechRequest
        fields = '__all__'