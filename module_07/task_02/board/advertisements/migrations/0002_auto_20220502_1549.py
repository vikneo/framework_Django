# Generated by Django 2.2 on 2022-05-02 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['title']},
        ),
        migrations.RenameField(
            model_name='heading',
            old_name='heading',
            new_name='name',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='price_exch',
            field=models.FloatField(default=72.58, verbose_name='доллар'),
        ),
    ]
