from django.shortcuts import render

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