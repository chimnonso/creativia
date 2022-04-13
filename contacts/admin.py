from django.contrib import admin
from .models import Contact, Event, TechRequest
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_date')
    list_display_links = ('first_name', 'last_name', 'email', 'contact_date')
    list_filter = ('first_name', 'last_name', 'contact_date')


class EventAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'company_name')
    list_display_links = ('first_name', 'email')
    list_filter = ('first_name',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(TechRequest)