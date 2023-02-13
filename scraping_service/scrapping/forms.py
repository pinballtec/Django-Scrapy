from django import forms

from .models import City, Programming_Language


class FindForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), to_field_name='name')
    language = forms.ModelChoiceField(queryset=Programming_Language.objects.all(), to_field_name='name')