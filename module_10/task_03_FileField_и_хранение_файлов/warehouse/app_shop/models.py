from django.db import models
from datetime import datetime


class Shop(models.Model):

    title = models.CharField(max_length=50, verbose_name='Название', db_index=True)
    code = models.CharField(max_length=35, verbose_name='Артикул')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.title}, {self.price}, {self.code}'

    class Meta:
        db_table = 'shops'
        ordering = ['title']


class File(models.Model):

    file = models.FileField(upload_to='file/')
    description = models.TextField(blank=True)
    create_at = models.DateField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     date = datetime.now().strftime('%d_%m_%Y-%H-%M-%S_')
    #     new_name = date + ".txt"
    #     print(self)
    #     self.name = new_name
    #     super(File, self).save(*args, **kwargs)
