from django.db import models


class Vacancy(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    title = models.CharField(max_length=36, verbose_name='Заголовок')
    description = models.TextField(default='', verbose_name='Описание')
    publisher = models.CharField(max_length=30, verbose_name='Кто опубликовал')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    publisher_at = models.DateField(verbose_name='Дата публикации', blank=True, null=True)

    class Meta:
        db_table = 'vacancy'
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'
        permissions = (
            ("can_publish", "Можно опубликовать"),
            ("can_change", 'Можно изменять'),
            ("can_add", 'Можно добавить'),
            ("can_view", 'Можно просматривать'),
        )

    def __str__(self):
        return self.title


class Resume(models.Model):
    title = models.CharField(max_length=36, verbose_name='Заголовок')
    description = models.TextField(default="", verbose_name='Описание')
    create_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    publisher_at = models.DateField(blank=True, null=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'resume'
        verbose_name = 'резюме'
        verbose_name_plural = 'резюме'
        permissions = (
            ("can_publish", 'Можно опубликовать'),
            ("can_change", 'Можно изменять'),
            ("can_add", 'Можно добавить'),
            ("can_view", 'Можно просматривать'),
        )
