from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path('', views.event, name="event"),
    path('download/', views.download_file, name="download")
]