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
    obj_weight= request.POST['weight']
    obj_cost= request.POST['cost']
    obj_qty= request.POST['qty']
    new_rec = Product(name=obj_name, price=obj_price, cost=obj_cost, on_hand_qty = obj_qty, weight= obj_weight)
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


def customers(request):
    all_customers = Company.objects.all()
    return render(request, 'customers.html', context={'all_customers': all_customers})


def customer_form(request, id):
    customer = Company.objects.get(id=id)
    return render(request, 'customer_form_view.html', context= {'customer': customer})


def delete_customer(request, id):
    customer = Company.objects.get(id=id)
    customer.delete()
    return HttpResponseRedirect(reverse('customers'))


def add_customer(request):
    return render(request, 'add_customer.html', context={})


def add_customer_record(request):
    obj_name = request.POST['name']
    obj_nip = request.POST['nip']
    obj_mail= request.POST['mail']
    obj_phone= request.POST['phone']
    new_rec = Company(name=obj_name, nip=obj_nip, mail=obj_mail, phone= obj_phone)
    new_rec.save()
    return HttpResponseRedirect(reverse('customers'))


def orders(request):
    all_orders = Order.objects.all()
    return render(request, 'orders.html', context={'all_orders': all_orders})


def order_form(request, id):
    order= Order.objects.get(id=id)
    lines = OrderLine.objects.filter(order=id)
    context = {'order': order,
               'lines': lines
               }
    return render(request, 'order_form_view.html', context)


def delete_order(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return HttpResponseRedirect(reverse('orders'))