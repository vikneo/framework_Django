from django.db import models

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(max_length=1500)
    descriptions = models.TextField()

    def __str__(self):
        return f'{self.title} {self.descriptions}'

