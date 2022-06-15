from django.db import models


class Vacancy(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    title = models.CharField(max_length=36, verbose_name='Заголовок')
    description = models.TextField(default='', verbose_name='Описание')
    publisher = models.CharField(max_length=30, verbose_name='Кто опубликовал')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    publisher_at = models.DateField(verbose_name='Дата публикации', blank=True, null=True)

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'
        permissions = (
            ("can_publish", "Можно опубликовать"),
        )

    def __str__(self):
        return self.title
