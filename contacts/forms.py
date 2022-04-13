from django.forms import ModelForm, ValidationError, CharField, EmailField, Textarea
from .models import Contact, Event, TechRequest

class ContactForm(ModelForm):
    # first_name = CharField(label='')
    # last_name = CharField(label='')
    # company_name = CharField(label='')
    # message = CharField(label='')
    # email = EmailField(label='')

    class Meta:
        model = Contact
        exclude = ['contact_date']
        widgets = {
            'message': Textarea(attrs={'rows':4})
        }

    # def clean(self):
    #     super().clean()
    #     name = self.cleaned_data.get("name")

    #     if not name:
    #         msg = "Please give us a name"
    #         self.add_error('name', msg)
    #         raise ValidationError(msg)


class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['contact_date']

class TechRequestForm(ModelForm):
    class Meta:
        model = TechRequest
        exclude = ['request_date']
        widgets = {
            'message': Textarea(attrs={'rows':4})
        }