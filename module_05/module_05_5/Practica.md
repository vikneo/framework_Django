## Метаданные моделей и индексы

* Напишите программу для добавления нескольких сотен тысяч записей (500 тысяч) в таблицу с объявлениями, замерьте время на выборку одной записи с фильтром по полю title.
* Добавьте индекс на поле title, замерьте время на выборку одной записи с фильтром по полю title.
* Сделайте запрос к таблице объявлений с сортировкой по полю created_at, результаты замерьте. Добавьте индекс на поле created_at и выполните запрос снова. Результаты сравните с результатами до создания индекса.
### Практика
* Напишите программу для добавления нескольких сотен тысяч записей (500 тысяч) в таблицу с объявлениями, замерьте время на выборку одной записи с фильтром по полю title.
```python
# в корневой папке запускаем скрипт на добавление нескольких тысяч объявлений в БД \module_05_5\fill_db.py
>python fill_db.py
# В базе данных проводим поиск
SELECT * FROM advertisement WHERE title='Продам'
# время поиска в базе составляет 16мс
```
* Добавьте индекс на поле title, замерьте время на выборку одной записи с фильтром по полю title.
```python

# в моделе Advertisement в поле title добавляем db_index=True
# в классе Meta добавляем атрибут operating = ['title'] и делаем миграцию
> python manage.py makemigrations
> python manage.py migrate

# В базе данных проводим поиск
SELECT * FROM advertisement WHERE title='Продам'
# время поиска в базе составляет 6мс
```
* Сделайте запрос к таблице объявлений с сортировкой по полю created_at, результаты замерьте. Добавьте индекс на поле created_at и выполните запрос снова. Результаты сравните с результатами до создания индекса.
```python
# В базе данных проводим поиск
SELECT * FROM advertisement WHERE created_at='2022-04-25 18:47:29'
# время поиска в базе составляет 25мс

# в моделе Advertisement в поле created добавляем db_index=True
# в классе Meta добавляем атрибут operating = ['created_at'] и делаем миграцию
> python manage.py makemigrations
> python manage.py migrate

# В базе данных проводим поиск
SELECT * FROM advertisement WHERE created_at='2022-04-25 18:47:29'
# время поиска в базе составляет 16мс
```