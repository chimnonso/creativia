from django.forms import ModelForm
from .models import Event
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class EventForm(ModelForm):
    
    def clean_email(self):
        data = self.cleaned_data['email']
        mail = Event.objects.filter(email__iexact=data).first()

        if mail:
            raise ValidationError(_(f'{mail} has already been used'))
        return data
    
    class Meta:
        model = Event
        exclude = ['contact_date']
