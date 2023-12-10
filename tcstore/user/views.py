from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from .forms import EditProfileForm, LoginForm, ChangePasswordForm


def user_registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'user/user_registration.html', {'form': form})


def user_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'user/user_login.html', {'form': form})


@login_required
def user_profile_view(request):
    return render(request, 'user/user_profile.html')


@login_required
def user_edit_profile_view(request):
    user = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            if cleaned_data['username']:
                user.username = cleaned_data['username']
            if cleaned_data['first_name']:
                user.first_name = cleaned_data['first_name']
            if cleaned_data['last_name']:
                user.last_name = cleaned_data['last_name']
            user.save()
            return redirect('user_profile')
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'user/user_profile.html', {'form': form})


@login_required
def user_logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')


@login_required
def user_change_password_view(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('user_profile')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'user/user_change_password.html', {'form': form})
