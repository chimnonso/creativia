from django.contrib import admin
from .models import Technology
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


class TechnologyAdmin(admin.ModelAdmin, DynamicArrayMixin): 
    list_display = ("title", "short_description", "date_posted")
    list_display_links = ("title", "short_description")
    list_filter = ("title", "date_posted")

admin.site.register(Technology, TechnologyAdmin)