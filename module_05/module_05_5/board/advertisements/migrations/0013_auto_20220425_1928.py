# Generated by Django 2.2 on 2022-04-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0012_auto_20220425_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
    ]