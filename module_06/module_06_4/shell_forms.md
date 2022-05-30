## Валидация форм

* #### Выполняется код в консоли shell
* вызов консоли
```python
..\board> python manage.py shell
```
```python
# импорт формы
from django import forms
# создаем форму
class AdvertisementForm(forms.Form):
    title = forms.CharField(min_length=3, max_length=20)
    descriptions = forms.CharField(min_length=10, max_length=200)
    price = forms.FloatField(min_value=1000, max_value=100000)

# создаем не корректный словарь
incorrect_adv = {
    'title': 'Продам',
    'descriptions': 'Дачу',
    'price': 50000
}
# Инициализируем форму
advertisement = AdvertisementForm(incorrect_adv)
advertisement.is_valid()
# вернется значение False
>> False
# заглянем в словарь ошибок
advertisement.errors
# вернется словарь с ошибками в данных
>> {'descriptions': ['Ensure this value has at least 10 characters (it has 4).']}
# видно, что ошибочные данные в поле "descriptions"
# вызовем форму в виде таблицы
advertisement.as_p()
>> '<p><label for="id_title">Title:</label> <input type="text" name="title" value="Продам" maxlength="20" minlength="3" required id="id_title"></p>\n<ul class="errorlist"><li>Ensure this value has at least 10 characters (it has 4).</li><
  /ul>\n<p><label for="id_descriptions">Descriptions:</label> <input type="text" name="descriptions" value="Дачу" maxlength="200" minlength="10" required id="id_descriptions"></p>\n<p><label for="id_price">Price:</label> <input type="nu
  mber" name="price" value="50000" min="1000" max="100000" step="any" required id="id_price"></p>'

# теперь введем валидные данные
correct_adv = {
    'title': 'Продам',
    'descriptions': 'Квартиру в новостройке',
    'price': 50000
}
# проинициализируем форму
advertisement = AdvertisementForm(correct_adv)
# снова проверим на валидность
advertisement.is_valid()
# вернется значение True
>> True
# заглянем в словарь ошибок
advertisement.errors
>> {}
# Словарь пуст, значит ошибок нет и данные валидны
# выведем форму в виде таблицы
advertisement.as_p()
>> '<p><label for="id_title">Title:</label> <input type="text" name="title" value="Продам" maxlength="20" minlength="3" required id="id_title"></p>\n<p><label for="id_descriptions">Descriptions:</label> <input type="text" name="descripti
 ons" value="Квартиру в новостройке" maxlength="200" minlength="10" required id="id_descriptions"></p>\n<p><label for="id_price">Price:</label> <input type="number" name="price" value="50000" min="1000" max="100000" step="any" required
 id="id_price"></p>'
# Ошибки отсутствуют

```