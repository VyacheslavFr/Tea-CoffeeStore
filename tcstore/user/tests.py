from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import LoginForm


class UserLoginViewTestCase(TestCase):
    def test_user_login_valid_form(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        form_data = {'username': 'testuser', 'password': 'testpassword'}
        form = LoginForm(data=form_data)
        response = self.client.post(reverse('user_login'), data=form_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_user_login_invalid_form(self):
        form_data = {'username': 'testuser', 'password': 'wrongpassword'}
        form = LoginForm(data=form_data)
        response = self.client.post(reverse('user_login'), data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)


