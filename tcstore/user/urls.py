from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.user_profile_view, name='user_profile'),
    path('registration/', views.user_registration_view, name='user_registration'),
    path('edit_profile/', views.user_edit_profile_view, name='user_edit_profile'),
]
