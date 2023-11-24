from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from .forms import EditProfileForm


def user_registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main/main.html')
    else:
        form = UserCreationForm()
    return render(request, 'user/user_registration.html', {'form': form})


def user_profile_view(request):
    return render(request, 'user/user_profile.html')


def user_edit_profile_view(request):
    user = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'user/user_edit_profile.html', {'form': form})
