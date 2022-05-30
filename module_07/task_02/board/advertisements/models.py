from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', db_index=True)
    descriptions = models.CharField(max_length=1500, verbose_name='Описание')
    price = models.FloatField(default=0, verbose_name='Цена')
    price_exch = models.FloatField(default=72.58, verbose_name='доллар')
    create_start_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    create_end_at = models.DateTimeField(auto_now=True, verbose_name='Дата окончания публикации')
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    type_adv = models.CharField(max_length=25, default='Free', verbose_name='Тип объявления')
    heading_status = models.ForeignKey('Heading', on_delete=models.CASCADE,
                                       verbose_name='Рубрика', related_name='advertisements')
    users_status = models.ForeignKey('UsersInfo', on_delete=models.CASCADE,
                                     verbose_name='Пользователь', related_name='advertisements')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisements'
        ordering = ['title']


class Heading(models.Model):
    name = models.CharField(max_length=130, verbose_name='Рубрика', db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'heading'


class UsersInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО', db_index=True)
    mail_address = models.EmailField(max_length=100, verbose_name='Email адрес')
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'
