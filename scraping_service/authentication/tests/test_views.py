from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..forms import NewUserForm, UserLoginForm
from ..views import register, login_page, logout_page


class AuthenticationViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpass123'
        )

    def test_register_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/register.html')
        form = response.context['form']
        self.assertIsInstance(form, NewUserForm)

        response = self.client.post(self.register_url, {
            'email': 'newuser@example.com',
            'password1': 'password',
            'password2': 'password'
        })
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(get_user_model().objects.count(), 2)

    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')
        form = response.context['form']
        self.assertIsInstance(form, UserLoginForm)

        response = self.client.post(self.login_url, self.user_data)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, reverse('login'))
        self.assertFalse(response.wsgi_request.user.is_authenticated)