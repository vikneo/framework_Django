from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Название')
    city = models.CharField(max_length=35, verbose_name='Город')
    address = models.CharField(max_length=60, verbose_name='Адрес')

    def __str__(self):
        return f'{self.id}. {self.name} {self.city} {self.address}'

    class Meta:

        db_table = 'restaurant'


class Waiter(models.Model):

    STATUS_CHOICES = (
        ('a', 'Принят'),  # accept
        ('f', 'Уволен'),  # fire
        ('s', 'Больничный'),  # sick_list
        ('h', 'Отпуск'),  # holiday
    )
    first_name = models.CharField(max_length=30, db_index=True, verbose_name='Имя')
    second_name = models.CharField(max_length=30, db_index=True, verbose_name='Отчество')
    last_name = models.CharField(max_length=30, db_index=True, verbose_name='Фамилия')
    phone = models.CharField(max_length=15, verbose_name='№ телефона')
    mail_address = models.EmailField(verbose_name='Email адрес')
    age = models.IntegerField(verbose_name='Возраст', blank=True)
    sex = models.CharField(max_length=7, verbose_name='Пол', blank=True)
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    city = models.CharField(max_length=35, verbose_name='Город')
    education = models.CharField(max_length=100, verbose_name='Образование')
    country = models.CharField(max_length=50, verbose_name='Гражданство')
    employment_date = models.DateField(verbose_name='Дата трудоустройства')
    person_num = models.IntegerField(verbose_name='Табельный номер')
    salary = models.FloatField(verbose_name='Зарплата')
    status_employ = models.CharField(max_length=1, choices=STATUS_CHOICES, default='f')
    status = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='waiter_restaurant')

    def __str__(self):
        return f'{self.id}. {self.first_name} {self.last_name} {self.person_num}'

    class Meta:

        db_table = 'waiter'
