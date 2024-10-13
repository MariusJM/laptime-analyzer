from django.shortcuts import render

# Create your views here.
def index(request):
    # This function handles what happens when someone visits the home page
    return render(request, 'home/index.html')