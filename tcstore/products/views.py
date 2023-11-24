from django.shortcuts import render


def products_home(request):
    return render(request, 'main/about.html')
