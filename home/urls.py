# home/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # This connects the root URL to the 'index' view
    path('naujienos/', views.naujienos, name='naujienos'),
    path('burelis/', views.burelis, name='burelis'),
    path('pamokos/', views.pamokos, name='pamokos'),
    path('kainos/', views.kainos, name='kainos'),
    path('kontaktai/', views.kontaktai, name='kontaktai'),
]
