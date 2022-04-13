from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    email = models.EmailField("Email")
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=100)
    company_name = models.CharField("Company Name", max_length=100)
    # subject = models.CharField("Subject", max_length=250)
    message = models.TextField("Message")
    contact_date = models.DateTimeField("Date Posted", default=timezone.now)

    def __str__(self):
        return self.email



class Event(models.Model):
    email = models.EmailField("Email")
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=100)
    company_name = models.CharField("Company Name", max_length=100)
    # subject = models.CharField("Subject", max_length=250)
    contact_date = models.DateTimeField("Date Posted", default=timezone.now)

    def __str__(self):
        return self.email


class TechRequest(models.Model):
    email = models.EmailField("Email")
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=100)
    company_name = models.CharField("Company Name", max_length=100)
    message = models.TextField("Message", default="I would like to request this technology")
    tech_title = models.CharField("Technology Title", max_length=100)
    request_date = models.DateTimeField("Request Date", default=timezone.now)

    def __str__(self):
        return self.email