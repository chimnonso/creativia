from django.contrib import admin
from .models import Event
# Register your models here.



class EventAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'company_name', 'contact_date')
    list_display_links = ('first_name', 'email')
    list_filter = ('first_name', 'contact_date')

admin.site.register(Event, EventAdmin)