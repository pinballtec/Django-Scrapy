from django.test import TestCase
from ..forms import FindForm
from ..models import City, Programming_Language


class FindFormTestCase(TestCase):
    def setUp(self):
        """Setup for testCase"""
        self.city = City.objects.create(name='Киев')
        self.language = Programming_Language.objects.create(name='Python')
        # print(City.objects.all().values_list('id', 'name'))
        # print(Programming_Language.objects.all().values_list('id', 'name'))

    def test_form_valid(self):
        """ModelChoiceField, need to be used str instead of .pk"""
        form_data = {
            'city': str(self.city),
            'language': str(self.language),
        }
        form = FindForm(data=form_data)
        # print(form_data)
        # print(print(form.errors))
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {}
        form = FindForm(data=form_data)
        self.assertFalse(form.is_valid())
