from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
