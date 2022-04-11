from django.contrib import admin
from .models import Technology
# Register your models here.

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("title", "short_description", "date_posted")
    list_display_links = ("title", "short_description")
    list_filter = ("title", "date_posted")

admin.site.register(Technology, TechnologyAdmin)