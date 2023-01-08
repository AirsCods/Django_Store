from django.shortcuts import render
from products.models import ProductCategory, Products


# Create your views here.


def index(request):
    context = {
        'title': 'Store',
        'is_promotion': True,
    }
    return render(
        request,
        'products/index.html',
        context,
    )


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Products.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(
        request,
        'products/products.html',
        context,
    )
