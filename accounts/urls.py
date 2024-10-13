# accounts/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login view
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    # Logout view - use `LOGOUT_REDIRECT_URL`
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Registration view
    path('register/', views.register, name='register'),
]
