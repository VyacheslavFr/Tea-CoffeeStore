from django.shortcuts import render


def products_home(request):
    return render(request, 'products/products_home.html')
