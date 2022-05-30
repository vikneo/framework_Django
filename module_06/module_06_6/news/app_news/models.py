from django.db import models


class News(models.Model):
    name = models.CharField(max_length=130, verbose_name='Статья')
    article = models.CharField(max_length=2000, verbose_name="Содержание")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", db_index=True)
    refactor_date = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")
    flag_news = models.BooleanField(default=False, verbose_name="Активность")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'news'
        ordering = ['created_date']


class Comments(models.Model):
    author = models.CharField(max_length=35, verbose_name='Имя пользователя')
    comment = models.CharField(max_length=500, verbose_name='Комментарий')
    news = models.ForeignKey('News', default=None, null=True, on_delete=models.CASCADE, related_name='comments_name')

    class Meta:
        db_table = 'comments'
