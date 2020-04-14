from django.db import models
from django import forms

# class TimeSet(forms.Form):
#     time_set = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

class TemperatureSensors(models.Model):
    """
    The table registers the temperature device along with setting the
    min max temperature in fahrenheit
    """
    device_name = models.CharField(max_length=30, primary_key=True)
    max_temperature = models.FloatField(help_text="Temperature in fahrenheit")
    min_temperature = models.FloatField(help_text="Temperature in fahrenheit")

    def __str__(self):
        return self.device_name

class LightSensors(models.Model):
    """
    Table registers the Light sensors along with setting the time of day in EST
    time that they should turn on or off
    """
    device_name = models.CharField(max_length=30, primary_key=True)
    turn_on_start = models.TimeField(help_text="HH:MM:SS 24-Hour Format")
    turn_on_end = models.TimeField(help_text="HH:MM:SS 24-Hour Format")

    def __str__(self):
        return self.device_name

class TemperatureRead(models.Model):
    """
    Table updates periodically with the temperature readings. Will also attempt to
    report if the sensor is still communicating incase the sensor gets damaged
    """
    device_name = models.ForeignKey(TemperatureSensors, on_delete=models.CASCADE)
    sample_date = models.DateTimeField(auto_now_add=True)
    
    # Data from sensors
    temperature = models.FloatField()
    humidity = models.FloatField()

    # Able to communicate
    device_online = models.BooleanField()

    def __str__(self):
        return f"{self.device_name}: {self.sample_date}"

class LightRead(models.Model):
    """
    Same as temperatureRead, but for the lights
    """
    decice_name = models.ForeignKey(LightSensors, on_delete=models.CASCADE)
    sample_date = models.DateTimeField(auto_now=True)

    # Status of the light
    powered_on = models.BooleanField()

    # Able to communicate
    device_online = models.BooleanField()