from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    descriptions = models.CharField(max_length=1000, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.IntegerField(verbose_name='Цена', default=0)
    view_count = models.FloatField(verbose_name='Количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisement')

    def __str__(self):
        return self.title


class Announcements(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категории')
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name='announcement')


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

