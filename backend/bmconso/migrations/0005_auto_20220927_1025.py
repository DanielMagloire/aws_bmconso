# Generated by Django 3.2.6 on 2022-09-27 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmconso', '0004_auto_20220927_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='hour_begin',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='rule',
            name='hour_end',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
