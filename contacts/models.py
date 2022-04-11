from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
    email = models.EmailField("Email")
    name = models.CharField("Name", max_length=100)
    subject = models.CharField("Subject", max_length=250)
    message = models.TextField("Message")
    # contact_date = models.DateTimeField("Date Posted", default=datetime.now)

    def __str__(self):
        return self.email



class Event(models.Model):
    email = models.EmailField("Email")
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=100)
    company_name = models.CharField("Company Name", max_length=100)
    subject = models.CharField("Subject", max_length=250)
    # contact_date = models.DateTimeField("Date Posted", default=datetime.now)

    def __str__(self):
        return self.email


class TechRequest(models.Model):
    email = models.EmailField("Email")
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=100)
    company_name = models.CharField("Company Name", max_length=100)
    # subject = models.CharField("Subject", max_length=250)
    message = models.TextField("Message")
    tech_title = models.CharField("Technology Title", max_length=100)

    def __str__(self):
        return self.email