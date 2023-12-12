from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


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

def add_product_record(request):
    obj_name = request.POST['name']
    obj_price = request.POST['price']
    new_rec = Product(name=obj_name, price=obj_price)
    new_rec.save()
    return HttpResponseRedirect(reverse('products'))