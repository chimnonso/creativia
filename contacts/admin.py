from django.contrib import admin
from .models import Contact, Event, TechRequest
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    list_display_links = ('name', 'email', 'subject')
    list_filter = ('name',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'company_name', 'subject')
    list_display_links = ('first_name', 'email', 'subject')
    list_filter = ('first_name',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(TechRequest)