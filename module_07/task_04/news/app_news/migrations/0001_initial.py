# Generated by Django 2.2 on 2022-05-07 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('comment', models.CharField(max_length=300, verbose_name='Комментарий')),
                ('news', models.CharField(max_length=150, verbose_name='Новость')),
            ],
            options={
                'db_table': 'commentaries',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Новость')),
                ('descriptions', models.CharField(max_length=2000, verbose_name='Содержание')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('refactor_date', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('flag_news', models.BooleanField(default=False, verbose_name='Активность')),
                ('comment_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newses', to='app_news.Commentaries', verbose_name='Комментарий')),
            ],
            options={
                'db_table': 'news',
                'ordering': ['created_date'],
            },
        ),
    ]
