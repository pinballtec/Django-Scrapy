from django.test import Client, TestCase


class HomeViewTestCase(TestCase):
    def setUp(self):
        """client setup for GET request"""
        self.client = Client()

    def test_url(self):
        """Test for url and correct template"""
        response = self.client.get('/scrapping_app/home/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scrapping/home.html')
