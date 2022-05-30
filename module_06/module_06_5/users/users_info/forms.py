from django import forms
import datetime
from django.core.exceptions import ValidationError


class UserForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(min_length=8, max_length=20)
    first_name = forms.CharField()
    last_name = forms.CharField()
    birthday = forms.DateField()

    # Проверка дня рождения на количество лет ( пример на 18 лет)
    def clean_data(self):
        data = self.cleaned_data['birthday']
        today = datetime.date.today()
        year_delta = (today - data).days // 365
        print('=========: ', year_delta)
        if year_delta < 18:
            print(year_delta)
            raise ValidationError('Регистрироваться могут лица достигшие 18 лет!')
        return data

    # Проверка имени и фамилии на запрет регистрации ( Иван Иванов)
    def clean(self):
        clean_data = super(UserForm, self).clean()
        first_name = clean_data.get('first_name')
        last_name = clean_data.get('last_name')

        if first_name.lower() == 'иван' and last_name.lower() == 'иванов':
            # # первый вариант проверки
            # raise  ValidationError('Данные имя и фамилия запрещены для регистрации')
            # второй способ проверки
            msg = 'Данные имя и фамилия запрещены для регистрации'
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
