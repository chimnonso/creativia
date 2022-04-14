from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django_better_admin_arrayfield.models.fields import ArrayField
from datetime import datetime

# Create your models here.

class Technology(models.Model):
    title = models.CharField("Technology Name", max_length=150)
    short_description = models.CharField("Short Description", max_length=250)
    description = models.TextField("Description")
    date_posted = models.DateTimeField("Date Posted", default=datetime.now)
    details_list = ArrayField(models.CharField(max_length=400), blank=True, null=True)
    photo = models.ImageField("Upload Image", upload_to='photo/%Y/%m/%d', height_field=None, width_field=None, max_length=None)

    class Meta:
        ordering = ('-date_posted',)

    def __repr__(self):
        return f"<Technology {self.title}>"

    def __str__(self):
        return f"{self.title}"
