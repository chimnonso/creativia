from django.urls import path
from . import views

app_name = "technology"

urlpatterns = [
    path('', views.get_technologies, name="technologies"),
    path('<int:tech_id>/', views.details, name="details"),
]