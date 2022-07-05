from django.db import models


class Shop(models.Model):

    title = models.CharField(max_length=50, verbose_name='Название', db_index=True)
    code = models.CharField(max_length=35, verbose_name='Артикул')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.title}, {self.price}, {self.code}'

    class Meta:
        db_table = 'shops'
        ordering = ['title']
