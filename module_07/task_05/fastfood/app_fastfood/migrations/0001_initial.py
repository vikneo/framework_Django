# Generated by Django 2.2 on 2022-05-22 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=30, verbose_name='Название')),
                ('city', models.CharField(blank=True, max_length=35, verbose_name='Город')),
                ('address', models.CharField(blank=True, max_length=60, verbose_name='Адрес')),
            ],
            options={
                'db_table': 'restaurant',
            },
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, db_index=True, max_length=30, verbose_name='Имя')),
                ('second_name', models.CharField(blank=True, db_index=True, max_length=30, verbose_name='Отчество')),
                ('last_name', models.CharField(blank=True, db_index=True, max_length=30, verbose_name='Фамилия')),
                ('age', models.IntegerField(blank=True, verbose_name='Возраст')),
                ('sex', models.CharField(blank=True, max_length=7, verbose_name='Пол')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('city', models.CharField(max_length=35, verbose_name='Город')),
                ('education', models.CharField(max_length=100, verbose_name='Образование')),
                ('country', models.CharField(max_length=50, verbose_name='Гражданство')),
                ('employment_date', models.DateField(verbose_name='Дата трудоустройства')),
                ('person_num', models.IntegerField(verbose_name='Табельный номер')),
                ('salary', models.FloatField(verbose_name='Зарплата')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waiter_restaurant', to='app_fastfood.Restaurant')),
            ],
            options={
                'db_table': 'waiter',
            },
        ),
    ]
