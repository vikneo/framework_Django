# Generated by Django 2.2 on 2022-05-13 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0009_auto_20220511_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaries',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaries_news', to='app_news.News', verbose_name='Новость'),
        ),
    ]
