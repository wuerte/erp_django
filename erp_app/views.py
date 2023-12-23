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


def product_form(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_form_view.html', context= {'product': product})


def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect(reverse('products'))


def product_analytics(request):
    stock_valuation_list = Product.get_stock_valuation_list()
    context= {'svl': stock_valuation_list}
    return render(request, 'product_analysis.html', context)
