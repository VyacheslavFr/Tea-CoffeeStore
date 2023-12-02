from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_home, name='products_home')
]