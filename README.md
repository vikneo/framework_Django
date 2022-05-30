# framework_Django
Practical tasks

## Первые шаги для установки Django

* Устанавливаем виртуальное окружение

```html
python -m venv venv
```
* Активация вирт окружения
```html
..\venv\Scripts\activate
```

* Создаем файл requirements.txt и сразу открываем для записи
```html
copy con requirements.txt

Вносим изменения:
    Django==2.2
Выходим. Комбинация Ctrl+Z и Enter
```

* Устанавливаем Django
```html
pip install -r requirements.txt
```

## Создание проекта

* Создаем проект
```html
django-admin startproject "name_project"
```

* Переход в папку с проектом
```html
>cd "name_project"

```

* Создаем приложение в папке проекта
```html
python manage.py startapp "name_directory"
```

* Производим миграцию файлов и БД
```html
python manage.py migrate
```
