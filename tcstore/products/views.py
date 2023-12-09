from django.shortcuts import render
from .models import Products


def products_home(request):
    products = Products.objects.all()
    return render(request, 'products/products_home.html', {'products': products})
