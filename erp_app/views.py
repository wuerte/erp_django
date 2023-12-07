from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', context={})

def products(request):
    return render(request, 'products.html', context={})