from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    descriptions = models.CharField(max_length=1000, verbose_name='Описание')
    price = models.FloatField(default=0, verbose_name='Цена')

    class Meta:
        db_table = 'advertisements'

