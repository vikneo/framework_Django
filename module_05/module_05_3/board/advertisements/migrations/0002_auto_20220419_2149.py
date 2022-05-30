# Generated by Django 2.2 on 2022-04-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='price',
            field=models.FloatField(default=0, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='просмотры'),
        ),
    ]
