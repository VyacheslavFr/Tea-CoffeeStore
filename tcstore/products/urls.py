from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_home_view, name='products_home'),
    path('<int:id>/', views.product_detailed_view, name='product_detailed')
]
