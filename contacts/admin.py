from django.contrib import admin
from .models import Contact, TechRequest
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_date')
    list_display_links = ('first_name', 'last_name', 'email', 'contact_date')
    list_filter = ('first_name', 'last_name', 'contact_date')



admin.site.register(Contact, ContactAdmin)
admin.site.register(TechRequest)