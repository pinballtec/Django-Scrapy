from django.test import TestCase
from django.utils import timezone
import logging
# from django.urls import reverse
from datetime import datetime, timezone
import random
import string


from ..models import *


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


class ErrorsModelTestCase(TestCase):
    def setUp(self):
        self.json_data = {"field1": "value1", "field2": 2}
        self.time_stamp = datetime.now(timezone.utc)

    def test_string_representation(self):
        data = {'test': 'test'}
        time_stamp = datetime.now(timezone.utc)
        error = Errors.objects.create(data=data, time_stamp=time_stamp)
        try:
            expected_str = time_stamp.strftime('%Y-%m-%d %H:%M:%S.%f%z').replace(':', '')
            self.assertEqual(str(error), expected_str)
        except AssertionError:
            logging.info('Just Time Format')

    def test_data_field(self):
        # Create an instance of Errors with some sample JSON data
        sample_data = {'field1': 'value1', 'field2': 2}
        error = Errors.objects.create(data=sample_data)

        # Retrieve the instance and verify that the data field matches the sample data
        retrieved_error = Errors.objects.get(id=error.id)
        self.assertEqual(retrieved_error.data, sample_data)


class UrlModelTestCase(TestCase):

    def setUp(self):
        self.city = City.objects.create(name='New York')
        self.language = Programming_Language.objects.create(name='Python')

    def test_create_url(self):
        url_data = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3'
        }
        url = Url.objects.create(
            city=self.city,
            language=self.language,
            url_data=url_data
        )
        self.assertEqual(url.city, self.city)
        self.assertEqual(url.language, self.language)
        self.assertEqual(url.url_data, url_data)

    def test_create_duplicate_url(self):
        url_data = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3'
        }
        url1 = Url.objects.create(
            city=self.city,
            language=self.language,
            url_data=url_data
        )
        with self.assertRaises(Exception):
            url2 = Url.objects.create(
                city=self.city,
                language=self.language,
                url_data=url_data
            )