# Generated by Django 2.2 on 2022-05-07 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0005_auto_20220507_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaries',
            name='news',
        ),
        migrations.AddField(
            model_name='commentaries',
            name='news',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='commentaries', to='app_news.News', verbose_name='Новость'),
            preserve_default=False,
        ),
    ]
