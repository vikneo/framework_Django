from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    birth_day = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=36)
    phone = models.CharField(max_length=16)
    discount = models.CharField(max_length=23)

    class Meta:
        db_table = 'profiles'
        ordering = ['user']
