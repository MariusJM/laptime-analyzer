from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import News
from .forms import NewsForm


# Create your views here.
def index(request):
    # This function handles what happens when someone visits the home page
    return render(request, 'home/index.html')

def naujienos(request):
    return render(request, 'home/naujienos.html')

def burelis(request):
    return render(request, 'home/burelis.html')

def pamokos(request):
    return render(request, 'home/pamokos.html')

def kainos(request):
    return render(request, 'home/kainos.html')

def kontaktai(request):
    return render(request, 'home/kontaktai.html')


# Check if user is an admin
def is_admin(user):
    return user.is_staff

# Home view (Naujienos page)
def index(request):
    news = News.objects.all()  # Fetch all news articles
    return render(request, 'home/index.html', {'news': news})

# Create a news article (only for admins)
@login_required
@user_passes_test(is_admin)
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user  # Set the admin as the author
            news.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'home/create_news.html', {'form': form})
