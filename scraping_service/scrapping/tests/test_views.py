from django.test import TestCase
from django.urls import reverse
from ..models import Job_Offers, Programming_Language, City


class HomeViewTest(TestCase):
    def setUp(self):
        self.job_offer = Job_Offers.objects.create(
            urls='http://example-case11213214.com',
            title='Some Job Offer',
            company='Company',
            description='Some typical description to Job Offer',
            city=City.objects.create(name='Warsaw'),
            language=Programming_Language.objects.create(name='Js')
        )

    def test_home_view_uses_correct_template(self):
        """Testing correct template"""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'scrapping/home.html')

    def test_home_view_returns_all_job_offers(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.job_offer, response.context['object_list'])

    def test_home_view_class_method(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object_list'].model, Job_Offers)