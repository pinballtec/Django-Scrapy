from django.test import TestCase
from django.contrib.auth import get_user_model
from authentication.forms import NewUserForm, UserLoginForm

User = get_user_model()


class NewUserFormTest(TestCase):
    def test_new_user_form_with_valid_data(self):
        form = NewUserForm(data={
            'email': 'testuser@example.com',
            'password': 'TestPassword123',
            'password2': 'TestPassword123'
        })
        self.assertTrue(form.is_valid())

    def test_new_user_form_with_password_mismatch(self):
        form = NewUserForm(data={
            'email': 'testuser@example.com',
            'password': 'TestPassword123',
            'password2': 'TestPassword321'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_new_user_form_with_missing_data(self):
        form = NewUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertIn('password', form.errors)
        self.assertIn('password2', form.errors)


class UserLoginFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            email='testuser@example.com',
            password='TestPassword123'
        )

    def test_user_login_form_with_valid_credentials(self):
        form = UserLoginForm(data={
            'email': 'testuser@example.com',
            'password': 'TestPassword123'
        })
        self.assertTrue(form.is_valid())

    def test_user_login_form_with_invalid_email(self):
        form = UserLoginForm(data={
            'email': 'invalid@example.com',
            'password': 'TestPassword123'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)

    def test_user_login_form_with_invalid_password(self):
        form = UserLoginForm(data={
            'email': 'testuser@example.com',
            'password': 'InvalidPassword123'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)

    def test_user_login_form_with_banned_user(self):
        self.user.is_active = False
        self.user.save()
        form = UserLoginForm(data={
            'email': 'testuser@example.com',
            'password': 'TestPassword123'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)