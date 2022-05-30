from django.db import models


class Advertisement(models.Model):

    title = models.CharField(max_length=300, verbose_name='Заголовок', db_index=True)
    descriptions = models.CharField(max_length=500, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена', default=0)
    view_count = models.IntegerField(verbose_name='Количество просмотров', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        pass


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
