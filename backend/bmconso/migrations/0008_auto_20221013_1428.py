# Generated by Django 3.2.6 on 2022-10-13 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmconso', '0007_auto_20221013_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='hour_begin',
            field=models.PositiveIntegerField(default=14),
        ),
        migrations.AlterField(
            model_name='rule',
            name='hour_end',
            field=models.PositiveIntegerField(default=14),
        ),
    ]