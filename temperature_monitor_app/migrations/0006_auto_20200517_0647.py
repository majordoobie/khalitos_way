# Generated by Django 3.0.6 on 2020-05-17 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperature_monitor_app', '0005_auto_20200517_0630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relay',
            fields=[
                ('relay_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('daytime', models.BooleanField(choices=[(True, 'Daytime'), (False, 'Night time')], default=True, help_text='Should this relay power on during the day or night?')),
                ('gpio', models.IntegerField(default=-1, help_text='GPIO number, not the PIN!')),
                ('relay_state', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='lightread',
            name='decice_name',
        ),
        migrations.AddField(
            model_name='temperaturesensor',
            name='gpio',
            field=models.IntegerField(default=-1, help_text='GPIO number, not the PIN!'),
        ),
        migrations.AlterField(
            model_name='daytimecycle',
            name='daytime_end',
            field=models.TimeField(default=datetime.time(19, 0, 0, 861879), help_text='HH:MM:SS 24-Hour Format'),
        ),
        migrations.AlterField(
            model_name='daytimecycle',
            name='daytime_start',
            field=models.TimeField(default=datetime.time(7, 0, 0, 861580), help_text='HH:MM:SS 24-Hour Format'),
        ),
        migrations.AlterField(
            model_name='temperaturesensor',
            name='sensor_type',
            field=models.IntegerField(choices=[(11, 'DHT11'), (22, 'DHT22')], default=11, help_text='Sensor type to read'),
        ),
        migrations.DeleteModel(
            name='LightAccessory',
        ),
        migrations.DeleteModel(
            name='LightRead',
        ),
    ]
