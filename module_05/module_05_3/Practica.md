# Свойство полей
##Практическое задание

* создайте пять записей в модели Advertisement (Например: Сдается квартира, Продам автомобиль, Законное списание долгов, Продам дом, Приму в дар кота);
* отфильтруйте результат запроса по заголовку по частичному и полному совпадению;
* отсортируйте результат запроса по заголовку (используйте метод order_by());
* отсортируйте результат запроса по заголовку и верните первые 3 записи (используйте срезы);
* получите суммарное количество записей в модели Advertisement;
* проверьте, имеются ли записи в модели Advertisement (используйте метод exists())

## Практическое решение

* подключение к базе данных
```python
from advertisements.models import *
```

* запрос на создание пяти записей в модели Advertisement
```python
Advertisement(title='name', descriptions='desc') # в скобках 5 наименований
```
* создадим переменную для вывода всех записей из базы
```python
answer = Advertisement.objects.all()
```
* отфильтруйте результат запроса по заголовку по частичному совпадению
```python
Advertisement.objects.filter(title__icontains='Прод')
>> <QuerySet [<Advertisement: Продажа>]>
```
* отфильтруйте результат запроса по заголовку по полному совпадению
```python
Advertisement.objects.filter(title='Продажа')
# тоже самое
Advertisement.objects.filter(title__exact='Продажа')
>> <QuerySet [<Advertisement: Продажа>]>
```
* отсортируйте результат запроса по заголовку
```python
Advertisement.objects.counter('title')
# или через переменную answer
answer.order_by('title')
>> <QuerySet [<Advertisement: Продажа>, <Advertisement: Разное>, <Advertisement: Транспорт>, <Advertisement: Услуги>, <Advertisement: Услуги>]>
```
* отсортируйте результат запроса по заголовку и верните первые 3 записи (используйте срезы)
```python
Advertisement.objects.all()[:3]
# или через переменную answer
answer[:3]
>> <QuerySet [<Advertisement: Продажа>, <Advertisement: Услуги>, <Advertisement: Транспорт>]>
```
* получите суммарное количество записей в модели Advertisement
```python
ADvertisement.objects.all().count()
>> 5
```
* проверьте, имеются ли записи в модели Advertisement (используйте метод exists())
```python
Advertisement.objects.exists()
>> True
```