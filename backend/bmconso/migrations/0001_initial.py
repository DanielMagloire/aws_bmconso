# Generated by Django 3.2.6 on 2022-09-12 11:56

import bmconso.models
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.PositiveBigIntegerField(null=True)),
                ('num', models.CharField(default=bmconso.models.random_numstring, max_length=10, unique=True)),
                ('compl', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(default='', max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='Silo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wood_pci', models.FloatField(default=0)),
                ('wood_dens', models.FloatField(default=0)),
                ('limit_high', models.FloatField(default=100)),
                ('limit_low', models.FloatField(default=0)),
                ('boiler_count', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(3)])),
                ('cap', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=99)),
                ('sub', models.CharField(max_length=20, unique=True)),
                ('role', models.CharField(default='Utilisateur', max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='HeatingPlant',
            fields=[
                ('config', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bmconso.configuration')),
                ('silo_count', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(3)])),
                ('boiler_total', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9)])),
                ('is_coge', models.BooleanField(default=False)),
                ('power_coge', models.FloatField(default=0)),
                ('pilot_type', models.CharField(default='Maximum de chaudières', max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='IACrigen',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bmconso.user')),
                ('call_date', models.DateField(default=datetime.date.today)),
                ('call_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('config', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bmconso.configuration')),
                ('station', models.CharField(default='Abbeville (80)', max_length=34)),
                ('id_histo', models.PositiveIntegerField(default=7005)),
                ('id_prev', models.PositiveIntegerField(default=29592)),
                ('nom', models.CharField(default='abbeville', max_length=26)),
            ],
        ),
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('silo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bmconso.silo')),
                ('drop_min', models.PositiveIntegerField(default=0)),
                ('drop_max', models.PositiveIntegerField(default=0)),
                ('av', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Snapshot',
            fields=[
                ('silo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bmconso.silo')),
                ('goal', models.FloatField(default=0)),
                ('level', models.FloatField(default=0)),
                ('level_unit', models.CharField(default='m³', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveBigIntegerField(blank=True, null=True)),
                ('name', models.CharField(default='', max_length=50)),
                ('unit', models.CharField(default='W', max_length=3)),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmconso.configuration')),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_begin', models.DateField(default=datetime.date.today)),
                ('date_end', models.DateField(default=datetime.date.today)),
                ('hour_begin', models.PositiveIntegerField(default=13)),
                ('hour_end', models.PositiveIntegerField(default=13)),
                ('index', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(default='', max_length=50)),
                ('value', models.PositiveIntegerField(default=0)),
                ('silo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmconso.silo')),
            ],
        ),
        migrations.AddField(
            model_name='configuration',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bmconso.user'),
        ),
        migrations.CreateModel(
            name='Boiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output', models.FloatField(default=0)),
                ('power_nom', models.FloatField(default=0)),
                ('power_min', models.FloatField(default=0)),
                ('load', models.FloatField(default=0)),
                ('order', models.PositiveIntegerField()),
                ('silo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmconso.silo')),
            ],
        ),
        migrations.AddField(
            model_name='silo',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmconso.heatingplant'),
        ),
    ]