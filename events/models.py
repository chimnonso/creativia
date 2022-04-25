from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    email = models.EmailField("Email")
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=100)
    company_name = models.CharField("Company Name", max_length=100)
    # subject = models.CharField("Subject", max_length=250)
    contact_date = models.DateTimeField("Date Posted", default=timezone.now)

    def __str__(self):
        return self.email