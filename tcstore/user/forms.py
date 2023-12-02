from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# class EditProfileForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email')


class EditProfileForm(forms.ModelForm):
    username = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.CharField(required=False)
    old_password = forms.CharField(widget=forms.PasswordInput, required=False)
    new_password = forms.CharField(widget=forms.PasswordInput, required=False)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'old_password', 'new_password', 'confirm_new_password']


# class ChangePasswordForm(forms.Form):
#     old_password = forms.CharField(widget=forms.PasswordInput)
#     new_password = forms.CharField(widget=forms.PasswordInput)
#     confirm_new_password = forms.CharField(widget=forms.PasswordInput)
