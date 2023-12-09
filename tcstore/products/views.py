from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Products


def products_home_view(request):
    products = Products.objects.all()
    return render(request, 'products/products_home.html', {'products': products})


@login_required
def product_detailed_view(request, id):
    product = get_object_or_404(Products, id=id)
    print(product.product_name)
    return render(request, 'products/product_detailed.html', {'product': product})
