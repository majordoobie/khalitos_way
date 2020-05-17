# Generated by Django 3.0.5 on 2020-04-14 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LightSensors',
            fields=[
                ('device_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('turn_on_start', models.TimeField()),
                ('turn_on_end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureSensors',
            fields=[
                ('device_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('max_temperature', models.FloatField()),
                ('min_temperature', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureRead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_date', models.DateField(auto_now=True)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('device_online', models.BooleanField()),
                ('device_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temperature_monitor_app.TemperatureSensors')),
            ],
        ),
        migrations.CreateModel(
            name='LightRead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_date', models.DateField(auto_now=True)),
                ('powered_on', models.BooleanField()),
                ('device_online', models.BooleanField()),
                ('decice_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temperature_monitor_app.LightSensors')),
            ],
        ),
    ]