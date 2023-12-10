from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.user_edit_profile_view, name='user_profile'),
    path('registration/', views.user_registration_view, name='user_registration'),
    # path('edit_profile/', views.user_edit_profile_view, name='user_edit_profile'),
    path('login/', views.user_login_view, name='user_login'),
    path('logout/', views.user_logout_view, name='user_logout'),
    path('change_password/', views.user_change_password_view, name='user_change_password'),
]
