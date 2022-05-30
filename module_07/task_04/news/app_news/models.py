from django.db import models


class News(models.Model):
    name = models.CharField(max_length=250, verbose_name="Новость", db_index=True)
    descriptions = models.TextField(max_length=2000, verbose_name="Содержание")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    refactor_date = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")
    flag_news = models.BooleanField(default=False, verbose_name="Активность")

    def __str__(self):
        return f'{self.id}. {self.name}'

    def get_absolute_url(self):
        return f'/detail/{self.id}/'

    class Meta:
        db_table = 'news'
        ordering = ['created_date']


class Commentaries(models.Model):
    user_name = models.CharField(max_length=30, verbose_name="Имя")
    comment = models.CharField(max_length=300, verbose_name="Комментарий")
    news = models.ForeignKey("News", default=None, null=True, verbose_name='Новость', on_delete=models.CASCADE,
                             related_name="commentaries_news")

    def __str__(self):
        return f'{self.id}. {self.user_name}'

    class Meta:
        db_table = 'commentaries'
