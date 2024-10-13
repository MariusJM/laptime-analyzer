from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'landing/home.html')

def news(request):
    return render(request, 'news.html')

def projects(request):
    return render(request, 'projects.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')