"""
URL configuration for erp_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('products', views.products, name="products"),
    path('add_product', views.add_product, name="add_product"),
    path('add_product_record/', views.add_product_record, name="add_product_record"),
    path('product_form/<int:id>', views.product_form, name="product_form"),
    path('delete_product/<int:id>', views.delete_product, name="delete_product"),
]
