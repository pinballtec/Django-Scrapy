from django.urls import reverse, resolve
from django.test import RequestFactory, TestCase
from ..views import register, login_page, logout_page, update_user_info


class AuthenticationUrlsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_register_url_resolves_to_register_view(self):
        url = reverse('register')
        view = resolve(url).func
        self.assertEqual(view, register)

    def test_login_url_resolves_to_login_view(self):
        url = reverse('login')
        view = resolve(url).func
        self.assertEqual(view, login_page)

    def test_logout_url_resolves_to_logout_view(self):
        url = reverse('logout')
        view = resolve(url).func
        self.assertEqual(view, logout_page)
# afgoUSADGHjklsa;GD