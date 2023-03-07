from django.test import TestCase, Client
from django.urls import reverse
from django.test import RequestFactory, TestCase
from ..models import Job_Offers, Programming_Language, City
from ..views import HomeView, ListView
from ..forms import FindForm
from django.urls import reverse


class ListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.city = City.objects.create(name='New York')
        self.language = Programming_Language.objects.create(name='Python')

        self.job_offer = Job_Offers.objects.create(
            urls='http://example.com',
            title='Software Engineer',
            company='ACME',
            description='Build software',
            city=self.city,
            language=self.language
        )

    def test_home_view_uses_correct_template(self):
        """Testing correct template"""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'scrapping/home.html')

    def test_home_view_filters_correctly(self):
        request = self.factory.get('/', {'city': 'New York'})
        response = ListView.as_view()(request)
        self.assertEqual(list(
            response.context_data['object_list']), [self.job_offer]
        )

        request = self.factory.get('/', {'p_language': 'Python'})
        response = ListView.as_view()(request)
        self.assertEqual(list(
            response.context_data['object_list']), [self.job_offer]
        )

        request = self.factory.get(
            '/', {'city': 'New York', 'p_language': 'Python'}
        )
        response = ListView.as_view()(request)
        self.assertEqual(list(
            response.context_data['object_list']), [self.job_offer]
        )


class HomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_home_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'scrapping/home.html')

    def test_home_view_contains_form(self):
        response = self.client.get(self.url)
        form = response.context.get('form')
        self.assertIsNotNone(form)
        self.assertEqual(form.__class__.__name__, 'FindForm')