# Поля отношений
## Практическое задание
* Создайте модель Статус объявления с полем Название (Возможные значения: Черновик, Опубликовано, Архив) и добавьте внешний ключ на эту модель в Объявлении. Создайте миграцию и примените ее. Привяжите существующие объявления к статусу Черновик и попробуйте получить все записи объявлений из объекта статуса с использованием django shell.
* Создайте модель Тип объявления (Возможные значения: продам, куплю, сдам и т.д.) и свяжите ее с моделью Объявления. Создайте миграцию и примените ее. Привяжите существующие объявления к вновь созданным типам (добавьте их с использованием django shell) и попробуйте получить все записи объявлений из объекта типа.
* Добавьте атрибут related_name в поле статус, создайте и примените миграцию. Получите все связанные объявления статуса, используя related_name в django shell.
* Добавьте атрибут related_name в поле тип, создайте и примените миграцию. Получите все связанные объявления типа, используя related_name в django shell.

## Практическое решение
* Создайте модель Статус объявления с полем Название (Возможные значения: Черновик, Опубликовано, Архив) и добавьте внешний ключ на эту модель в Объявлении. Создайте миграцию и примените ее. Привяжите существующие объявления к статусу Черновик и попробуйте получить все записи объявлений из объекта статуса с использованием django shell.
```python
from advertisements.models import AdvertisementStatus
new_status = AdvertisementStatus(name='Черновик')
from advertisements.models import Advertisement
adv = Advertisement.objects.first()
# производим привязку объявления к статусу "Черновик"
adv.status = new_status
adv.save()
# проверим привязку объявления со статусом 'Черновик'
adv.status.name
>> 'Черновик'
# теперь можно вывести все объявления которые привязаны к статусу 'Черновик'
new_status.advertisement_set.all()
>> <QuerySet [<Advertisement: Продам>]>
```
* Создайте модель Тип объявления (Возможные значения: продам, куплю, сдам и т.д.) и свяжите ее с моделью Объявления. Создайте миграцию и примените ее. Привяжите существующие объявления к вновь созданным типам (добавьте их с использованием django shell) и попробуйте получить все записи объявлений из объекта типа.
```python
# для создания записей в таблицу "Тип объявления" создал скрипт script_generic_table
# для запуска скрипта введите команду:
python script_generic_table.py
# Подключаемся к базе данных
python manage.py shell
from advertisements.models import AdvertisementStatus
new_status = AdvertisementStatus(name='Объявления')
new_status.save()
from advertisements.models import Announcements
adv = Announcements.objects.first()
adv.status = new_status
adv.save()
# x4 записи сделать
# покажем все записи связанные со статусом "объявление"
new_status.announcements_set.all()
>> <QuerySet [<Announcements: Announcements object (1)>, <Announcements: Announcements object (2)>, <Announcements: Announcements object (3)>, <Announcements: Announcements object (4)>]>
```
* Добавьте атрибут related_name в поле статус, создайте и примените миграцию. Получите все связанные объявления статуса, используя related_name в django shell.
```python
# После добавления атрибута related_name='announcement' и миграции имеем:
from advertisements.models import AdvertisementStatus
status = AdvertisementStatus.objects.get(name='Объявления')
status.announcement.all()
```
* Добавьте атрибут related_name в поле тип, создайте и примените миграцию. Получите все связанные объявления типа, используя related_name в django shell.
```python
pass
```