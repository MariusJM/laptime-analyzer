# landing/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
]