# home/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # This connects the root URL to the 'index' view
]
