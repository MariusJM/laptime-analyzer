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
    path('create-news/', views.create_news, name='create_news'),
    path('track-layouts/', views.track_layouts, name='track_layouts'),  # List of track layouts
    path('track-layouts/<int:pk>/', views.track_layout_detail, name='track_layout_detail'),  # Detail view for a layout
]

