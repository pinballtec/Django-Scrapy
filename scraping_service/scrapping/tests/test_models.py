from django.test import TestCase
# from django.urls import reverse

import random
import string


from ..models import City, Programming_Language, Job_Offers


def random_string(string_length=10):
    """Function to get random str to get random url"""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(string_length))


class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        City.objects.create(name='Kiev', slug='Test')

    def test_name_label(self):
        city = City.objects.get(id=1)
        field_label = city._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'City Name')

    def test_slug_label(self):
        city = City.objects.get(id=1)
        field_label = city._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')


class TestCaseModelProgrammingLanguage(TestCase):

    @classmethod
    def setUpTestData(cls):
        Programming_Language.objects.create(name='Go', slug='Test2')

    def test_name_label(self):
        name = Programming_Language.objects.get(id=1)
        field_label = name._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Programming Language')

    def test_slug_label(self):
        program = Programming_Language.objects.get(id=1)
        field_label = program._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')


class JobOffersTestCase(TestCase):
    def test_create_valid_job_offer(self):
        valid_url = 'https://www.example.com/' + ''.join(
            random.choices(string.ascii_letters, k=10)
        )
        valid_city = City.objects.create(name='New York')
        valid_language = Programming_Language.objects.create(name='Python')
        obj = Job_Offers(
            urls=valid_url,
            title='Software Developer',
            company='Example Company',
            description='A software developer position',
            city=valid_city,
            language=valid_language
        )
        obj.full_clean()
        obj.save()
        self.assertEqual(obj.urls, valid_url)
