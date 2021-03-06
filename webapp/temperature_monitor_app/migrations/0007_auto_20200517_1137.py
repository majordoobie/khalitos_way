# Generated by Django 3.0.6 on 2020-05-17 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperature_monitor_app', '0006_auto_20200517_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='relay',
            name='control',
            field=models.CharField(choices=[('light', 'Lights'), ('heat', 'Heat Lamp')], default='light', help_text='Will this relay control lights or heat?', max_length=30),
        ),
        migrations.AlterField(
            model_name='daytimecycle',
            name='daytime_end',
            field=models.TimeField(default=datetime.time(19, 0, 0, 418745), help_text='HH:MM:SS 24-Hour Format'),
        ),
        migrations.AlterField(
            model_name='daytimecycle',
            name='daytime_start',
            field=models.TimeField(default=datetime.time(7, 0, 0, 418485), help_text='HH:MM:SS 24-Hour Format'),
        ),
    ]
