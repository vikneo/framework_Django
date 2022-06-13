from django.db import models


class News(models.Model):
    STATUS_CHOICES = (
        ('a', "Активно"),
        ('n', 'Неактивно'),
    )

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    descriptions = models.CharField(max_length=500, verbose_name='Описание')
    created_at = models.DateField(auto_created=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата редактирования')
    activated = models.BooleanField(verbose_name='Активность', default=False)
    status = models.CharField(max_length=1, verbose_name='Статус', choices=STATUS_CHOICES, default='n')

    def __str__(self):
        return f'{self.title}'

    class Meta:

        db_table = 'news'
        ordering = ['created_at']
