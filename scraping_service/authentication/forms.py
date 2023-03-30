from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

from scrapping.models import City, Programming_Language

User = get_user_model()


class NewUserForm(forms.ModelForm):
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password one more time',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Password is not matching')
        return data['password2']


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email').strip()
        password = self.cleaned_data.get('password').strip()

        if email and password:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('User error!')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Password error!')
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('User is banned')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserUpdateForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(),
                                  to_field_name='name')

    language = forms.ModelChoiceField(queryset=Programming_Language.objects.all(),
                                      to_field_name='name')

    newsletter = forms.BooleanField(required=False, widget=forms.CheckboxInput, label='Newsletter')

    class Meta:
        model = User
        fields = ('city', 'language', 'newsletter')