from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html', context={})

def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products.html', context)

def add_product(request):
    return render(request, 'add_product.html', context={})