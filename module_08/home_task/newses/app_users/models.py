from django.contrib.auth.models import User
from django.db import models

from app_news.models import News


class Comments(models.Model):

    username = models.CharField(max_length=30, verbose_name='Имя', blank=True)
    users = models.ForeignKey(User, blank=True, verbose_name='Имя пользователя', on_delete=models.CASCADE)
    comments = models.CharField(max_length=300, verbose_name='Комментарий')
    news = models.ForeignKey(News, blank=True, verbose_name='Новость', on_delete=models.CASCADE,
                             related_name='user_news')

    class Meta:

        db_table = 'comments'
