"""App URLs"""

# Django
# AA Example App
from django.urls import path

from base_plugin import views

app_name: str = "base_plugin"

urlpatterns = [
    path("", views.index, name="index"),
]
