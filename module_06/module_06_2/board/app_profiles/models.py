from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    birthday = models.DateField()

    class Meta:
        db_table = 'users'
