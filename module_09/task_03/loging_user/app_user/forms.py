from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    username = forms.CharField(max_length=30, required=False, help_text='Логин')
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    email = forms.CharField(widget=forms.EmailInput, required=False, help_text='Почта')


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=35, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=35, required=False, help_text='Фамилия')
    birth_day = forms.DateField(required=True, help_text='Дата рождения')
    city = forms.CharField(max_length=36, required=False, help_text='Город')
    phone = forms.CharField(max_length=16, required=True, help_text='№ телефона')
    discount = forms.CharField(max_length=23, required=True, help_text='№ скидочной карты')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
