# Generated by Django 2.2 on 2022-05-25 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_fastfood', '0006_auto_20220525_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waiter',
            name='status_employ',
            field=models.CharField(choices=[('a', 'Принят'), ('f', 'Уволен'), ('s', 'Больничный'), ('h', 'Отпуск')], default='f', max_length=1),
        ),
    ]
