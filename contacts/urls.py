from django.urls import path
from . import views

app_name = "contact"

urlpatterns = [
    path('contact/', views.contact, name="contact"),
    # path('event/', views.event, name="event"),
    path('tech_request/', views.tech_request, name="tech_request")
]