from django.test import TestCase
from ..models import City, Programming_Language


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


class TestCaseModelProgramming_Language(TestCase):

    @classmethod
    def setUpTestData(cls):
        Programming_Language.objects.create(name='Go', slug='Test2')

    def test_name_label(self):
        city = Programming_Language.objects.get(id=1)
        field_label = city._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Programming Language')

    def test_slug_label(self):
        city = Programming_Language.objects.get(id=1)
        field_label = city._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')

    # def setUp(self):
    #     print("setUp: Run once for every test method to setup clean data.")
    #     pass
    #
    # def test_false_is_false(self):
    #     print("Method: test_false_is_false.")
    #     self.assertFalse(False)
    #
    # def test_false_is_true(self):
    #     print("Method: test_false_is_true.")
    #     self.assertTrue(True)
    #
    # def test_one_plus_one_equals_two(self):
    #     print("Method: test_one_plus_one_equals_two.")
    #     self.assertEqual(1 + 1, 2)
